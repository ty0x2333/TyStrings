import os
import re
import codecs
import subprocess
import tempfile
import shutil
from .tylogger import logger

DEFAULT_ENCODING = 'utf16'


class Strings(object):
    def __init__(self, encoding=DEFAULT_ENCODING, aliases=None):
        self.encoding = encoding if encoding else DEFAULT_ENCODING
        self.__references = {}
        self.aliases = aliases if aliases else []
        self.temp_dir = None

    def generate(self, files, dst):
        """generate strings
        :param dst: destination directory
        :param files: input files
        :return generate strings dicts
        """
        dst_dir = os.path.abspath(dst)
        results = {}
        if self.temp_dir is None:
            logger.process('Generating Strings...')
            self.__generate_strings_temp_file(files)
            logger.done('Generated Strings')

        for filename in os.listdir(self.temp_dir):
            logger.debug('generated %s' % filename)
            reference = self.parsing(os.path.join(dst_dir, filename), encoding=self.encoding)
            self.__references[filename] = reference
        logger.done('Generated Reference')
        for k, v in self.__references.items():
            logger.info('%s count: %d' % (k, len(v)))

        for basename, ref in self.__references.items():
            target_abspath = os.path.join(dst_dir, basename)
            dirname = os.path.dirname(target_abspath)
            if not os.path.exists(dirname):
                os.makedirs(dirname)
            shutil.copy(os.path.join(self.temp_dir, basename), target_abspath)
            results[basename] = self.translate(target_abspath, ref, self.encoding)

        return results

    def __generate_strings_temp_file(self, source_files):
        """run `genstrings` script. generate `.strings` files to a temp directory.
        :param source_files: input files
        :return: temp directory
        """
        script = 'genstrings'
        for filename in source_files:
            script += ' %s' % filename

        if len(self.aliases) > 0:
            script += ' -s'
            for alias in self.aliases:
                script += ' %s' % alias

        temp_dir = tempfile.mkdtemp()
        self.__run_script('%s -o %s' % (script, temp_dir))
        self.temp_dir = temp_dir
        return temp_dir

    def __del__(self):
        if self.temp_dir:
            shutil.rmtree(self.temp_dir, ignore_errors=True)

    @staticmethod
    def __run_script(script):
        logger.debug('run: %s' % script)
        process = subprocess.Popen(script, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        output = ''
        while process.poll() is None:
            line = process.stdout.readline()
            if line:
                output += line
                logger.debug(line.strip())
        logger.finished(process.returncode)

        return process.returncode, output

    @staticmethod
    def parsing(filename, encoding=DEFAULT_ENCODING):
        """parsing `.strings` file.
        :param filename: .strings filename
        :param encoding: file encoding
        :return: reference
        """
        reference = dict((elem[0], elem[1]) for elem in Strings.__reference_generator(filename, encoding))
        return reference

    @staticmethod
    def parsing_elems(filename, encoding=DEFAULT_ENCODING):
        return list(Strings.__reference_generator(filename, encoding))

    @staticmethod
    def __reference_generator(filename, encoding=DEFAULT_ENCODING):
        if os.path.exists(filename):
            line_end = [0]
            contents = ''
            with codecs.open(filename, mode='r', encoding=encoding if encoding else DEFAULT_ENCODING) as f:
                for line in f.readlines():
                    contents += line
                    line_end.append(len(contents))
            prog = re.compile(r"\s*\"(?P<key>.*?)\"\s*=\s*\"(?P<value>[\s\S]*?)\"\s*;", re.MULTILINE)
            for match in prog.finditer(contents):
                key = match.group('key')
                key_start = match.start('key')
                value = match.group('value')
                match.groupdict()
                line_no = next(i for i in range(len(line_end)) if line_end[i] > key_start)
                yield (key, value, line_no)

    @property
    def generated_filenames(self):
        """generated strings files basenames
        e.g.: 'Localizable.strings'
        :return: strings filenames
        """
        return self.__references.keys()

    @staticmethod
    def translate(dst, reference, encoding=DEFAULT_ENCODING):
        """translate strings file by reference
        :param dst: destination strings file
        :param reference: translation reference
        :param encoding: file encoding
        :return: result dict
        """
        result = {}
        translated = []
        try:
            f = codecs.open(dst, "r", DEFAULT_ENCODING)
            lines = f.readlines()
            for (index, line) in enumerate(lines):
                match = re.match(r'"(?P<key>.*?)" = "(?P<value>.*?)";', line)
                if match is not None:
                    key = match.group('key')
                    value = match.group('value')
                    answer = reference.get(key, None)

                    if answer is not None:
                        if reference[key] != value:
                            line = '"%s" = "%s";\n' % (key, answer)
                            lines[index] = line
                            translated.append(key)
                        result[key] = answer
                    else:
                        result[key] = value
            f.close()

            logger.done('Translated: %s' % dst)
            logger.info('count: %d' % len(translated))
            for k in translated:
                logger.debug('%s => %s' % (k, result[k]))

            f = codecs.open(dst, "w+", encoding=encoding)
            f.writelines(lines)
            f.flush()
            f.close()
            return result
            # logger.addition('Write strings file to: %s' % self.filename)
        except Exception as e:
            logger.error(e)
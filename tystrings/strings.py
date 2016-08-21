import os
import re
import codecs
import subprocess
import tempfile
import shutil
from . import logger

DEFAULT_ENCODING = 'utf16'


class Strings(object):
    def __init__(self, dst_dir, encoding=DEFAULT_ENCODING, aliases=None):
        self.destination = os.path.abspath(dst_dir)
        self.encoding = encoding
        self.__references = {}
        self.aliases = aliases if aliases else []

    def generate(self, files):
        """generate strings
        :param files: input files
        :return generate strings dicts
        """
        results = {}
        script = 'genstrings'
        for filename in files:
            script += ' %s' % filename

        if len(self.aliases) > 0:
            script += ' -s'
            for alias in self.aliases:
                script += ' %s' % alias

        logger.done('Generated Strings')
        temp_dir = tempfile.mkdtemp()
        try:
            self.__run_script('%s -o %s' % (script, temp_dir))
            logger.debug('')
            for filename in os.listdir(temp_dir):
                logger.debug('generated %s' % filename)
                reference = self.generate_reference(os.path.join(self.destination, filename))
                self.__references[filename] = reference
            logger.done('Generated Reference')
            for k, v in self.__references.items():
                logger.info('%s count: %d' % (k, len(v)))

            for basename, ref in self.__references.items():
                target_abspath = os.path.join(self.destination, basename)
                dirname = os.path.dirname(target_abspath)
                if not os.path.exists(dirname):
                    os.makedirs(dirname)
                shutil.copy(os.path.join(temp_dir, basename), target_abspath)
                results[basename] = self.__translate(target_abspath, ref)
        finally:
            shutil.rmtree(temp_dir)
        return results

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

    def generate_reference(self, filename):
        """generate reference from strings file.
        :param filename: .strings filename
        :return: reference
        """
        reference = {}
        if os.path.exists(filename):
            f = codecs.open(filename, "r", encoding=self.encoding)
            prog = re.compile(r"\s*\"(?P<key>.*?)\"\s*=\s*\"(?P<value>.*?)\"\s*;")
            lines = f.readlines()
            for line in lines:
                match = prog.match(line)
                if match is not None:
                    key = match.group('key')
                    value = match.group('value')
                    reference[key] = value
            f.close()
        return reference

    @property
    def generated_filenames(self):
        """generated strings files basenames
        e.g.: 'Localizable.strings'
        :return: strings filenames
        """
        return self.__references.keys()

    def __translate(self, dst, reference):
        """translate strings file by reference
        :param dst: destination strings file
        :param reference: translation reference
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
            logger.debug('')
            for k in translated:
                logger.debug('%s => %s' % (k, result[k]))

            f = codecs.open(dst, "w+", encoding=self.encoding)
            f.writelines(lines)
            f.flush()
            f.close()
            return result
            # logger.addition('Write strings file to: %s' % self.filename)
        except Exception as e:
            logger.error(e)
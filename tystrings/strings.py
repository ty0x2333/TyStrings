import os
import re
import codecs
import subprocess
import tempfile
import shutil
from . import logger


class Strings(object):
    def __init__(self, dst_dir, encoding='utf_16_le'):
        self.destination = os.path.abspath(dst_dir)
        self.encoding = encoding
        self.__references = {}

    def generate(self, files, update_reference=True):
        script = 'genstrings'
        for filename in files:
            script += ' %s' % filename

        logger.done('Generated Strings')
        temp_dir = tempfile.mkdtemp()
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
                os.mkdir(dirname)
            shutil.copy(os.path.join(temp_dir, basename), target_abspath)
            self.__translate(target_abspath, ref)

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
            for line in f:
                match = re.match(r'"(?P<key>.*?)" = "(?P<value>.*?)";', line)
                if match is not None:
                    key = match.group('key')
                    value = match.group('value')
                    reference[key] = value
            f.close()
        return reference

    def __translate(self, dst, reference):
        translated = {}
        try:
            f = codecs.open(dst, "r", encoding=self.encoding)
            lines = f.readlines()
            for (index, line) in enumerate(lines):
                match = re.match(r'"(?P<key>.*?)" = "(?P<value>.*?)";', line)
                if match is not None:
                    key = match.group('key')
                    result = reference.get(key, None)

                    if result is not None:
                        value = match.group('value')
                        if reference[key] != value:
                            line = '"%s" = "%s";\n' % (key, result)
                            lines[index] = line
                            translated[key] = result
            f.close()

            logger.done('Translated: %s' % dst)
            logger.info('count: %d' % len(translated))
            logger.debug('')
            for k in translated.keys():
                logger.debug('%s => %s' % (k, translated[k]))

            f = codecs.open(dst, "w+", encoding=self.encoding)
            f.writelines(lines)
            f.flush()
            f.close()
            # logger.addition('Write strings file to: %s' % self.filename)
        except Exception as e:
            logger.error(e)
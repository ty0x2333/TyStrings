import os
import re
import codecs
import subprocess
from . import logger

STRING_FILE = 'Localizable.strings'


class Strings(object):
    def __init__(self, target_dir, encoding='utf_16_le'):
        self.__dir = target_dir
        self.encoding = encoding
        self.filename = os.path.join(target_dir if target_dir else '', STRING_FILE)
        self.__reference = {}

    def generate(self, files):
        self.update_reference()
        script = 'genstrings'
        for filename in files:
            script += ' %s' % filename
        self.__run_script('%s -o %s' % (script, self.__dir if self.__dir else '.'))
        self.__translate()

    @staticmethod
    def __run_script(script):
        logger.debug('\nrun: %s' % script)
        process = subprocess.Popen(script, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        output = ''
        while process.poll() is None:
            line = process.stdout.readline()
            if line:
                output += line
                logger.debug(line.strip())
        logger.finished(process.returncode)

        return process.returncode, output

    def update_reference(self):
        self.__reference = {}
        if os.path.exists(self.filename):
            f = codecs.open(self.filename, "r", encoding=self.encoding)
            for line in f:
                match = re.match(r'"(?P<key>.*?)" = "(?P<value>.*?)";', line)
                if match is not None:
                    key = match.group('key')
                    value = match.group('value')
                    self.__reference[key] = value
            f.close()
        logger.done('Generated Reference')
        logger.info('count: %r' % len(self.__reference))

    def __translate(self):
        sum = 0
        translated = {}
        try:
            f = codecs.open(self.filename, "r", encoding=self.encoding)
            lines = f.readlines()
            for (index, line) in enumerate(lines):
                match = re.match(r'"(?P<key>.*?)" = "(?P<value>.*?)";', line)
                if match is not None:
                    key = match.group('key')
                    result = self.__reference.get(key, None)

                    if result is not None:
                        value = match.group('value')
                        if self.__reference[key] != value:
                            line = '"%s" = "%s";\n' % (key, result)
                            lines[index] = line
                            sum += 1
                            translated[key] = result
            f.close()

            logger.done('Translated Strings')
            logger.info('count: %r' % sum)
            logger.debug('')
            for k in translated.keys():
                logger.debug('%s => %s' % (k, translated[k]))

            f = codecs.open(self.filename, "w+", encoding=self.encoding)
            f.writelines(lines)
            f.flush()
            f.close()
            logger.addition('Write strings file to: %s' % self.filename)
        except Exception as e:
            logger.error(e)
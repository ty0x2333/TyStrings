# -*- encoding: utf-8 -*-
import re
import codecs
import argparse
import os
import logging
import subprocess
__author__ = 'luckytianyiyan@gmail.com'


STRING_FILE = 'Localizable.strings'
DEFAULT_ENCODING = 'utf_16_le'


class Strings(object):
    def __init__(self, dir):
        self.__dir = dir
        self.filename = os.path.join(dir if dir else '', STRING_FILE)
        self.__reference = {}

    def generate(self, input):
        self.__reference = self.__generate_reference()
        self.__run_script('genstrings %s -o %s' % (input, self.__dir))
        self.__translate()

    @staticmethod
    def __run_script(script, display_output=True):
        if display_output:
            logging.info('%s' % script)
            logging.info('---')
        process = subprocess.Popen(script, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        output = ''
        while process.poll() is None:
            line = process.stdout.readline()
            if line:
                output += line
                if display_output:
                    logging.info(line.strip())
        if display_output:
            logging.info('process finished with %s\n' % ('success' if
                                                         process.returncode == 0 or process.returncode is None else
                                                         ('exit code %r' % process.returncode)))

        return process.returncode, output

    def __generate_reference(self):
        result = {}
        if os.path.exists(self.filename):
            f = codecs.open(self.filename, "r", encoding=DEFAULT_ENCODING)
            for line in f:
                match = re.match(r'"(?P<key>.*?)" = "(?P<value>.*?)";', line)
                if match is not None:
                    key = match.group('key')
                    value = match.group('value')
                    result[key] = value
                    logging.debug('%s: %s' % (key, value))
            f.close()
        return result

    def __translate(self):
        if os.path.exists(self.filename):
            f = codecs.open(self.filename, "r", encoding=DEFAULT_ENCODING)
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
                            logging.debug('translate %s to %s' % (value, result))
            f.close()

            f = codecs.open(self.filename, "w+", encoding=DEFAULT_ENCODING)
            f.writelines(lines)
            f.flush()
            f.close()


def arg_parser():
    description = r"""
  _______     _____ _        _
 |__   __|   / ____| |      (_)
    | |_   _| (___ | |_ _ __ _ _ __   __ _ ___
    | | | | |\___ \| __| '__| | '_ \ / _` / __|
    | | |_| |____) | |_| |  | | | | | (_| \__ \
    |_|\__, |_____/ \__|_|  |_|_| |_|\__, |___/
        __/ |                         __/ |
       |___/                         |___/
    """
    parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter, description=description)
    parser.add_argument('filename', help='Objective-C source file. (.m file)')
    parser.add_argument('-o', '--output', dest="dir", help='place output files in \'dir\'')

    return parser


def main():
    parser = arg_parser()
    args = parser.parse_args()

    logging.basicConfig(level=logging.DEBUG, format='%(message)s', )

    if os.path.isdir(args.filename):
        parser.error('%s is a directory' % args.filename)

    strings = Strings(args.dir)

    strings.generate(input=args.filename)

    # logging.debug('\nsource strings count: %r\n' % len(source))

if __name__ == '__main__':
    main()
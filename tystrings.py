# -*- encoding: utf-8 -*-
import re
import codecs
import argparse
import os
import logging
import subprocess
__author__ = 'luckytianyiyan@gmail.com'


STRING_FILE = 'Localizable.strings'


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


def convert_strings(filename):
    result = {}
    if os.path.exists(filename):
        f = codecs.open(filename, "r", encoding='utf_16')
        for line in f:
            match = re.match(r'"(?P<key>.*?)" = "(?P<value>.*?)";', line)
            if match is not None:
                key = match.group('key')
                value = match.group('value')
                result[key] = value
                logging.debug('%s: %s' % (key, value))
        f.close()
    return result


def translate(filename, dic):
    if os.path.exists(filename):
        f = codecs.open(filename, "r", encoding='utf_16_le')
        lines = f.readlines()
        for (index, line) in enumerate(lines):
            match = re.match(r'"(?P<key>.*?)" = "(?P<value>.*?)";', line)
            if match is not None:
                key = match.group('key')
                result = dic.get(key, None)

                if result is not None:
                    value = match.group('value')
                    if dic[key] != value:
                        line = '"%s" = "%s";\n' % (key, result)
                        lines[index] = line
                        logging.debug('translate %s to %s' % (value, result))
        f.close()

        f = codecs.open(filename, "w+", encoding='utf_16_le')
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

    return parser


def main():
    parser = arg_parser()
    args = parser.parse_args()

    logging.basicConfig(level=logging.DEBUG, format='%(message)s', )

    if os.path.isdir(args.filename):
        parser.error('%s is a directory' % args.filename)

    output = STRING_FILE
    source = convert_strings(output)

    logging.debug('\nsource strings count: %r\n' % len(source))

    __run_script('genstrings %s' % args.filename)

    translate(output, source)


if __name__ == '__main__':
    main()
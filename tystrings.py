# -*- encoding: utf-8 -*-
import re
import codecs
import argparse
import os
import logging
import subprocess
__author__ = 'luckytianyiyan@gmail.com'


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

    source = {}
    if os.path.isdir(args.filename):
        parser.error('%s is a directory' % args.filename)

    __run_script('genstrings %s' % args.filename)

    # f = codecs.open(args.filename, "r", encoding='utf_16')
    # for line in f:
    #     match = re.match(r'"(?P<key>.*?)" = "(?P<value>.*?)";', line)
    #     if match is not None:
    #         # print match.group('key'), match.group('value')
    #         source[match.group('key')] = match.group('value')
    #
    # print source

if __name__ == '__main__':
    main()
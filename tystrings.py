# -*- encoding: utf-8 -*-
import re
import codecs
import argparse
__author__ = 'luckytianyiyan@gmail.com'


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

    return parser


def main():
    parser = arg_parser()
    args = parser.parse_args()
    source = {}
    f = codecs.open('Localizable.strings', "r", encoding='utf_16')
    for line in f:
        match = re.match(r'"(?P<key>.*?)" = "(?P<value>.*?)";', line)
        if match is not None:
            # print match.group('key'), match.group('value')
            source[match.group('key')] = match.group('value')

    print source


if __name__ == '__main__':
    main()
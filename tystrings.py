# -*- encoding: utf-8 -*-
import re
import codecs
__author__ = 'luckytianyiyan@gmail.com'


def main():
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
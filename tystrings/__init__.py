#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import argparse
import os
import logging
from . import tylogger
__author__ = 'luckytianyiyan@gmail.com'
__version__ = '0.2.0'


logging.setLoggerClass(tylogger.TyLogger)

logger = logging.getLogger('tystrings')

from .strings import Strings


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
    parser.add_argument('--version', action='version', version=__version__)
    parser.add_argument('files', metavar='file', nargs='+', help='source file .[mc]')
    parser.add_argument('-a', '--aliases', nargs='+', help='aliases')
    parser.add_argument('-o', '--output', dest='dir', help='place output files in \'dir\'')
    parser.add_argument('-v', '--verbose', action="store_true", dest="verbose", help="show more debugging information")
    parser.add_argument('--utf8', action="store_true", dest="utf8", help="read files use encoding UTF-8")

    return parser


def main():
    parser = arg_parser()
    args = parser.parse_args()

    if args.verbose:
        logger.setLevel(logging.DEBUG)

    for filename in args.files:
        if not os.path.exists(filename):
            parser.error('%s not exists' % filename)
        if os.path.isdir(filename):
            parser.error('%s is a directory' % filename)

    strings = Strings(args.dir if args.dir else '.', aliases=args.aliases)

    if args.utf8:
        strings.encoding = 'utf8'

    strings.generate(args.files)

    logger.success('have fun!')

if __name__ == '__main__':
    main()

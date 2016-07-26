#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import argparse
import os
import logging
__author__ = 'luckytianyiyan@gmail.com'
__version__ = '0.1.0'

# Colors
BLUE = '\033[1;94m'
GREEN = '\033[1;92m'
YELLOW = '\033[93m'
RED = '\033[91m'
HIGH_LIGHT = '\033[1;97m'
ENDC = '\033[0m'

# Format
STEP_FORMAT = '==> ' + HIGH_LIGHT + '{}' + ENDC
DONE_FORMAT = BLUE + STEP_FORMAT
SUCCESS_FORMAT = GREEN + STEP_FORMAT

# Emoji
BEER_EMOJI = u'\U0001F37A '
BEERS_EMOJI = u'\U0001F37B '


logger = logging.getLogger('tystrings')
handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)

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
    parser.add_argument('-o', '--output', dest='dir', help='place output files in \'dir\'')
    parser.add_argument('-v', '--verbose', action="store_true", dest="verbose", help="show more debugging information")

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

    strings = Strings(args.dir)

    strings.generate(args.files)

    logger.info(BEERS_EMOJI + HIGH_LIGHT + ' have fun!' + ENDC)

if __name__ == '__main__':
    main()

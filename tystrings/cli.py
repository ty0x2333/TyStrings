import argparse
import os
import logging
from . import __version__
from .tylogger import logger
from .strings import Strings
from .translator import Translator


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
    parser.add_argument('-o', '--output', nargs='+', dest='destinations', help='place output files in dirs')
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

    dsts = args.destinations if args.destinations else ["."]

    strings = Strings(aliases=args.aliases)
    if args.utf8:
        strings.encoding = 'utf8'
    for dst in dsts:
        strings.generate(files=args.files, dst=dst)

    logger.success('have fun!')


def translate_arg_parser():
    parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('source', help='source `.strings` file')
    parser.add_argument('destination', help='destination, a file or directory')
    parser.add_argument('--dst-lang', required=True, help='destination language')
    parser.add_argument('--version', action='version', version=__version__)
    parser.add_argument('-s', '--src-lang', help='source language')
    parser.add_argument('-v', '--verbose', action="store_true", dest="verbose", help="show more debugging information")
    parser.add_argument('--utf8', action="store_true", dest="utf8", help="use encoding UTF-8")
    return parser


def translate():
    parser = translate_arg_parser()
    args = parser.parse_args()
    if args.verbose:
        logger.setLevel(logging.DEBUG)
    translator = Translator(args.source, lang=args.src_lang)
    translator.translate(args.destination, dst_lang=args.dst_lang)
    logger.success('have fun!')

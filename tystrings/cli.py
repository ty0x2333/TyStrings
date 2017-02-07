import argparse
import os
import logging
import collections
from .version import __version__
from .tylogger import logger
from .strings import Strings
from .translator import Translator
from tabulate import tabulate


def parent_parser():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('-v', '--verbose', action="store_true", dest="verbose", help="show more debugging information")
    parser.add_argument('--utf8', action="store_true", dest="utf8", help="use encoding UTF-8")
    return parser


def extant_file(x):
    if not os.path.exists(x):
        # Argparse uses the ArgumentTypeError to give a rejection message like:
        # error: argument input: x does not exist
        raise argparse.ArgumentTypeError("{0} does not exist".format(x))
    elif os.path.isdir(x):
        raise argparse.ArgumentTypeError("{0} is a directory".format(x))
    return x


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
    subparsers = parser.add_subparsers(title='subcommands', dest='action')

    generate_parser = subparsers.add_parser('generate', parents=[parent_parser()],
                                            help='generate `.strings` file from source code files.')
    generate_parser.add_argument('files', metavar='file', nargs='+', help='source file .[mc]', type=extant_file)
    generate_parser.add_argument('-a', '--aliases', nargs='+', help='aliases')
    generate_parser.add_argument('-o', '--output', nargs='+', dest='destinations', help='place output files in dirs')

    translate_parser = subparsers.add_parser('translate', parents=[parent_parser()],
                                             help='using Baidu Translate Service to translate `.strings` file.')
    translate_parser.add_argument('source', help='source `.strings` file')
    translate_parser.add_argument('destination', help='destination, a file or directory')
    translate_parser.add_argument('--dst-lang', required=True, help='destination language')
    translate_parser.add_argument('-s', '--src-lang', help='source language')

    lint_parser = subparsers.add_parser('lint', parents=[parent_parser()],
                                        help='Validates a `.strings` file.')
    lint_parser.add_argument('file', help='`.strings` file', type=extant_file)

    diff_parser = subparsers.add_parser('diff', parents=[parent_parser()],
                                        help='Compare `.strings` files line by line.')
    diff_parser.add_argument('file1', type=extant_file)
    diff_parser.add_argument('file2', type=extant_file)
    diff_parser.add_argument('-k', '--only-key', action="store_true", help="Only keys are compared")
    return parser


def main(argv=None):
    parser = arg_parser()
    args = parser.parse_args(argv)

    if args.verbose:
        logger.setLevel(logging.DEBUG)

    if args.action == 'generate':
        generate(args=args)
    elif args.action == 'translate':
        translate(args=args)
    elif args.action == 'lint':
        lint(args=args)
    elif args.action == 'diff':
        diff(args=args)

    exit(0)


def generate(args):
    dsts = args.destinations if args.destinations else ["."]

    strings = Strings(aliases=args.aliases, encoding=args.utf8)
    for dst in dsts:
        strings.generate(files=args.files, dst=dst)
    logger.success('have fun!')


def translate(args):
    translator = Translator(args.source, lang=args.src_lang)
    translateds = translator.translate(args.destination, dst_lang=args.dst_lang)
    rows = []
    for k in translateds.keys():
        (s, d) = translateds[k]
        rows.append([k, s, d])
    if rows:
        logger.done('Finished')
        logger.info(tabulate(rows, headers=['Key', 'Value', 'Result']))
    logger.success('have fun!')


def lint(args):
    logger.process('Parsing Source Reference...')
    elems = Strings.parsing_elems(filename=args.file, encoding='utf8' if args.utf8 else None)
    logger.process('Check Duplicate Keys...')
    duplicates = []
    for item, count in collections.Counter([e[0] for e in elems]).items():
        if count > 1:
            duplicates.append((item, count))

    if duplicates:
        table = []
        table_file = []
        logger.info('Find the following:')
        for key, count in duplicates:
            table.append([key, count])
            for elem in elems:
                if elem[0] == key:
                    table_file.append([elem[2], elem[0], elem[1]])
        logger.info(tabulate(table, headers=['Key', 'Count'], showindex='always', tablefmt="orgtbl"))
        logger.debug('Detail:')
        logger.debug(tabulate(table_file, headers=['Line', 'Key', 'Value'], tablefmt="orgtbl"))
        logger.error('Duplicate Keys')
        exit(1)

    logger.success('lint success')


def diff(args):
    def __generator(elems1, elems2, only_key, prefix):
        for elem in elems1:
            if not next((e for e in elems2 if e[0] == elem[0] and (only_key or e[1] == elem[1])), False):
                yield (prefix, elem[2], '', elem[0], elem[1])

    encoding = 'utf8' if args.utf8 else None
    logger.process('Parsing File1 Reference...')
    file1_elems = Strings.parsing_elems(filename=args.file1, encoding=encoding)
    logger.process('Parsing File2 Reference...')
    file2_elems = Strings.parsing_elems(filename=args.file2, encoding=encoding)
    logger.process('Comparing...')

    diff_adds = list(__generator(file1_elems, file2_elems, args.only_key, '+'))
    diff_subs = list(__generator(file2_elems, file1_elems, args.only_key, '-'))
    diffs = diff_adds + diff_subs
    diffs.sort(key=lambda obj: obj[1] if obj[1] else obj[2])
    logger.diffs(diffs)


if __name__ == '__main__':
    main()
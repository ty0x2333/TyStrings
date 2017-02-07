from .tyformatter import *
from colorama import Fore, Style
from tabulate import tabulate

# Emoji
BEER_EMOJI = u'\U0001F37A '
BEERS_EMOJI = u'\U0001F37B '
GHOST_EMOJI = u'\U0001F47B  '

# Log Level
PROCESS = 11
DONE = 12
SUCCESS = 13
ADDITION = 14


class TyLogger(logging.Logger):

    def __init__(self, name, level=logging.NOTSET):
        logging.Logger.__init__(self, name, level)

        logging.addLevelName(DONE, 'DONE')
        logging.addLevelName(SUCCESS, 'SUCCESS')
        handler = logging.StreamHandler()
        handler.setLevel(logging.DEBUG)
        handler.setFormatter(TyFormatter())
        self.addHandler(handler)
        self.setLevel(logging.INFO)

    def process(self, msg, *args, **kwargs):
        self._log(PROCESS, msg, args, **kwargs)

    def done(self, msg, *args, **kwargs):
        self._log(DONE, msg, args, **kwargs)

    def success(self, msg, *args, **kwargs):
        self._log(SUCCESS, BEERS_EMOJI + ' ' + Fore.LIGHTWHITE_EX + msg + Fore.RESET, args, **kwargs)

    def addition(self, msg, *args, **kwargs):
        self._log(ADDITION, BEERS_EMOJI + ' ' + Fore.LIGHTWHITE_EX + msg + Fore.RESET, args, **kwargs)

    def finished(self, return_code, *args, **kwargs):
        self.debug(BEER_EMOJI + ' process finished with %s' % ('success' if
                   return_code == 0 or return_code is None else ('exit code %r' % return_code)), *args, **kwargs)

    def diffs(self, diffs, *args, **kwargs):
        def __coloring(elem, color):
            return tuple(['%s%s%s' % (color, item, Style.RESET_ALL)
                          for item in list(elem)])
        rows = [__coloring(item, Fore.LIGHTGREEN_EX if item[0] == '+' else Fore.LIGHTRED_EX) for item in diffs]
        self.info(tabulate(rows,
                           tablefmt="psql", headers=['', 'File1', 'File2', 'Key', 'Value']), *args, **kwargs)



logging.setLoggerClass(TyLogger)

logger = logging.getLogger('tystrings')
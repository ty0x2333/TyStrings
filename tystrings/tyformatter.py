import logging
import tylogger
from colorama import Fore


class TyFormatter(logging.Formatter):
    ERROR_FORMAT = Fore.LIGHTRED_EX + 'Error' + Fore.RESET + ': %(message)s'
    WARNING_FORMAT = Fore.LIGHTYELLOW_EX + 'Warning' + Fore.RESET + ': %(message)s'
    STEP_FORMAT = '==> ' + Fore.LIGHTWHITE_EX + '%(message)s' + Fore.RESET
    PROCESS_FORMAT = Fore.LIGHTBLUE_EX + '>>> ' + Fore.LIGHTWHITE_EX + '%(message)s' + Fore.RESET
    DONE_FORMAT = Fore.LIGHTBLUE_EX + STEP_FORMAT
    ADDITION_FORMAT = Fore.LIGHTGREEN_EX + STEP_FORMAT

    def __init__(self, fmt=None, datefmt=None):
        logging.Formatter.__init__(self, fmt=fmt, datefmt=datefmt)
        self._default_fmt = self._fmt
        self._fmts = {
            logging.DEBUG: self._default_fmt,
            logging.WARNING: TyFormatter.WARNING_FORMAT,
            logging.ERROR: TyFormatter.ERROR_FORMAT,
            tylogger.PROCESS: TyFormatter.PROCESS_FORMAT,
            tylogger.DONE: TyFormatter.DONE_FORMAT,
            tylogger.ADDITION: TyFormatter.ADDITION_FORMAT
        }

    def __fmt_with_level(self, level):
        return self._fmts.get(level, self._default_fmt)

    def format(self, record):
        self._fmt = self.__fmt_with_level(record.levelno)
        return logging.Formatter.format(self, record)
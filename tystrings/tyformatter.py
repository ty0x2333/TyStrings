import logging
import tylogger

# Colors
BLUE = '\033[1;94m'
GREEN = '\033[1;92m'
HIGH_LIGHT = '\033[1;97m'
RED = '\033[1;91m'
YELLOW = '\033[1;93m'
ENDC = '\033[0m'


class TyFormatter(logging.Formatter):
    ERROR_FORMAT = RED + 'Error' + ENDC + ': %(message)s'
    WARNING_FORMAT = YELLOW + 'Warning' + ENDC + ': %(message)s'
    STEP_FORMAT = '==> ' + HIGH_LIGHT + '%(message)s' + ENDC
    DONE_FORMAT = BLUE + STEP_FORMAT
    ADDITION_FORMAT = GREEN + STEP_FORMAT

    def __init__(self, fmt=None, datefmt=None):
        logging.Formatter.__init__(self, fmt=fmt, datefmt=datefmt)
        self._default_fmt = self._fmt
        self._fmts = {
            logging.DEBUG: self._default_fmt,
            logging.WARNING: TyFormatter.WARNING_FORMAT,
            logging.ERROR: TyFormatter.ERROR_FORMAT,
            tylogger.DONE: TyFormatter.DONE_FORMAT,
            tylogger.ADDITION: TyFormatter.ADDITION_FORMAT
        }

    def __fmt_with_level(self, level):
        return self._fmts.get(level, self._default_fmt)

    def format(self, record):
        self._fmt = self.__fmt_with_level(record.levelno)
        return logging.Formatter.format(self, record)
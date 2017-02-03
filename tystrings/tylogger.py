from .tyformatter import *
from colorama import Fore

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

logging.setLoggerClass(TyLogger)

logger = logging.getLogger('tystrings')
from .tyformatter import *

# Emoji
BEER_EMOJI = u'\U0001F37A '
BEERS_EMOJI = u'\U0001F37B '

# Log Level
DONE = 11
SUCCESS = 12
ADDITION = 13


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

    def done(self, msg, *args, **kwargs):
        self._log(DONE, msg, args, **kwargs)

    def success(self, msg, *args, **kwargs):
        self._log(SUCCESS, BEERS_EMOJI + ' ' + HIGH_LIGHT + msg + ENDC, args, **kwargs)

    def addition(self, msg, *args, **kwargs):
        self._log(ADDITION, BEERS_EMOJI + ' ' + HIGH_LIGHT + msg + ENDC, args, **kwargs)

    def finished(self, return_code, *args, **kwargs):
        self.debug(BEER_EMOJI + ' process finished with %s' % ('success' if
                   return_code == 0 or return_code is None else ('exit code %r' % return_code)), *args, **kwargs)
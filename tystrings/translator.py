import shutil
import os
import logging
from .tylogger import logger, GHOST_EMOJI
from .strings import Strings, DEFAULT_ENCODING
from .baidu import BaiduTranslator


logging.getLogger("requests").setLevel(logger.level)


class Translator(object):
    def __init__(self, source, lang='auto', encoding=DEFAULT_ENCODING):
        self.file = os.path.abspath(source)
        self.language = lang
        self.encoding = encoding

    def translate(self, dst, dst_lang):
        translateds = {}
        dst_abspath = os.path.abspath(dst)
        logger.process('Parsing Source Reference...')
        reference = Strings.parsing(self.file, self.encoding)
        logger.process('Parsing Destination Reference...')
        dst_reference = Strings.parsing(dst_abspath, self.encoding)
        # for test, from Baidu Translate Open API Demo
        appid = '20151113000005349'
        secretKey = 'osubCEzlGjzvw8qdQc41'

        logger.process('Translating...')
        diff_reference_keys = list(set(reference) - set(dst_reference))
        logger.info('total number of words: %s' % len(diff_reference_keys))
        if not diff_reference_keys:
            logger.warning(GHOST_EMOJI + 'There is no need for translation.')
            return translateds

        diff_reference = []
        for k in diff_reference_keys:
            diff_reference.append(reference[k])
        logger.process('Translating by Baidu Translator...')
        translator = BaiduTranslator(appid, secretKey)
        result = translator.translate_list(diff_reference, dst_lang=dst_lang, src_lang=self.language)
        for s, d in result.items():
            for k in diff_reference_keys:
                if reference[k] == s:
                    reference[k] = d
                    translateds[k] = (s, d)

        dirname = os.path.dirname(dst_abspath)
        if not os.path.exists(dirname):
            os.makedirs(dirname)
        shutil.copy(self.file, dst_abspath)
        Strings.translate(dst_abspath, reference)
        return translateds

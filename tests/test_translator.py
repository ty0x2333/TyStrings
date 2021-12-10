import unittest

from tystrings import *


class TranslatorCase(unittest.TestCase):
    def setUp(self):
        self.file = 'tests/example/strings/base_translator.strings'
        self.reference_key = ['translator.test.0']
        self.app_id = '20160709000024959'
        self.secret_key = 'ke4UYwwvvgV9iQEIVjrC'

    def test_init(self):
        encoding = 'utf8'
        language = 'en'
        instance = Translator(source=self.file, lang=language, encoding=encoding,
                              app_id=self.app_id, secret_key=self.secret_key)
        self.assertEqual(instance.file, os.path.abspath(self.file))
        self.assertEqual(instance.language, language)
        self.assertEqual(instance.encoding, encoding)

    def test_default_init(self):
        instance = Translator(source='', app_id=self.app_id, secret_key=self.secret_key)
        self.assertEqual(instance.language, 'auto')
        self.assertEqual(instance.encoding, 'utf16')

    def test_translate(self):
        dst = 'tests/output/translator/base_translator.strings'
        instance = Translator(source=self.file, lang='en', app_id=self.app_id, secret_key=self.secret_key)
        instance.translate(dst=dst, dst_lang='zh')
        self.assertTrue(os.path.exists(dst))
        result = Strings.parsing(dst, encoding=instance.encoding)
        for k in self.reference_key:
            self.assertTrue(k in result)
        # cleanup
        os.remove(dst)

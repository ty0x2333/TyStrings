import unittest
import os
from tystrings import *


class TranslatorCase(unittest.TestCase):
    def setUp(self):
        self.file = 'tests/example/strings/base_translator.strings'
        self.reference_key = ['translator.test.0']

    def test_init(self):
        encoding = 'utf8'
        language = 'en'
        translator = Translator(source=self.file, lang=language, encoding=encoding)
        self.assertEqual(translator.file, os.path.abspath(self.file))
        self.assertEqual(translator.language, language)
        self.assertEqual(translator.encoding, encoding)

    def test_default_init(self):
        translator = Translator(source='')
        self.assertEqual(translator.language, 'auto')
        self.assertEqual(translator.encoding, 'utf16')

    def test_translate(self):
        dst = 'tests/output/translator/base_translator.strings'
        translator = Translator(source=self.file, lang='en')
        translator.translate(dst=dst, dst_lang='zh')
        self.assertTrue(os.path.exists(dst))
        result = Strings.parsing(dst, encoding=translator.encoding)
        for k in self.reference_key:
            self.assertTrue(k in result)
        # cleanup
        os.remove(dst)

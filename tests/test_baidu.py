import unittest
from tystrings import BaiduTranslator


class BaiduTranslatorTest(unittest.TestCase):
    def setUp(self):
        self.app_id = '20151113000005349'
        self.secretKey = 'osubCEzlGjzvw8qdQc41'

    def test_translate(self):
        translator = BaiduTranslator(app_id=self.app_id, secret_key=self.secretKey)
        result = translator.translate('Dog', dst_lang='zh', src_lang='en')
        self.assertTrue('Dog' in result.keys())

    def test_translate_without_src_language(self):
        translator = BaiduTranslator(app_id=self.app_id, secret_key=self.secretKey)
        result = translator.translate('Dog', dst_lang='zh')
        self.assertTrue('Dog' in result.keys())

    def test_translate_nothing(self):
        translator = BaiduTranslator(app_id=self.app_id, secret_key=self.secretKey)
        result = translator.translate('', dst_lang='zh')
        self.assertFalse(result)

    def test_translate_list(self):
        translator = BaiduTranslator(app_id=self.app_id, secret_key=self.secretKey)
        result = translator.translate_list(['Dog', 'Cat'], dst_lang='zh', src_lang='en')
        self.assertTrue('Dog' in result.keys())
        self.assertTrue('Cat' in result.keys())

    def test_translate_list_without_src_language(self):
        translator = BaiduTranslator(app_id=self.app_id, secret_key=self.secretKey)
        result = translator.translate_list(['Dog', 'Cat'], dst_lang='zh')
        self.assertTrue('Dog' in result.keys())
        self.assertTrue('Cat' in result.keys())


if __name__ == '__main__':
    unittest.main()

import unittest
from tystrings import *


class ParsingTest(unittest.TestCase):
    def setUp(self):
        self.strings = Strings()

    def test_base(self):
        result = Strings.parsing('tests/example/strings/base.strings')
        self.assertDictEqual(result, self._result(2))

    def test_utf8(self):
        result = Strings.parsing('tests/example/strings/utf8.strings', encoding='utf8')
        self.assertDictEqual(result, self._result(2))

    def test_comment(self):
        result = Strings.parsing('tests/example/strings/comment.strings')
        self.assertDictEqual(result, self._result(3))

    def test_space(self):
        result = Strings.parsing('tests/example/strings/space.strings')
        self.assertDictEqual(result, self._result(4))

    @staticmethod
    def _result(count):
        result = {}

        for i in range(0, count):
            result['parsing.test.%s' % i] = 'Test%s' % i

        return result
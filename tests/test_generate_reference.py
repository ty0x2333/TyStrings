import unittest
from tystrings import *


class GenerateReferenceTest(unittest.TestCase):
    def setUp(self):
        self.strings = Strings('tests/output/generate')

    def test_base(self):
        reference = self.strings.generate_reference('tests/example/strings/base.strings')
        self.assertDictEqual(reference, self._reference(2))

    def test_space(self):
        reference = self.strings.generate_reference('tests/example/strings/space.strings')
        self.assertDictEqual(reference, self._reference(3))

    @staticmethod
    def _reference(count):
        reference = {}

        for i in range(0, count):
            reference['generate.reference.test.%s' % i] = 'Test%s' % i

        return reference
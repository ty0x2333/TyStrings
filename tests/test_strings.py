import unittest
from tystrings import *
import shutil


class StringsTest(unittest.TestCase):
    def setUp(self):
        logger.level = logging.DEBUG
        self.addCleanup(self.cleanup)
        self.strings = Strings('tests/output')

    def test_generate(self):
        self.strings.generate(['tests/example/IntegrationDemo.m'])
        filenames = self.strings.generated_filenames
        self.assertTrue('Localizable.strings' in filenames)
        self.assertTrue('IntegrationTable.strings' in filenames)
        self.assertTrue(os.path.exists('tests/output/Localizable.strings'))
        self.assertTrue(os.path.exists('tests/output/IntegrationTable.strings'))

    def cleanup(self):
        if os.path.exists(self.strings.destination):
            shutil.rmtree(self.strings.destination)
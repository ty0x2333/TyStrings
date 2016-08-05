import unittest
from tystrings import *
import shutil


class StringsTest(unittest.TestCase):
    def setUp(self):
        logger.level = logging.DEBUG
        # self.addCleanup(self.cleanup)

    def test_generate(self):
        strings = Strings('tests/output/generate')
        strings.generate(['tests/example/IntegrationDemo.m'])
        filenames = strings.generated_filenames
        self.assertTrue('Localizable.strings' in filenames)
        self.assertTrue('IntegrationTable.strings' in filenames)
        self.assertTrue(os.path.exists('tests/output/generate/Localizable.strings'))
        self.assertTrue(os.path.exists('tests/output/generate/IntegrationTable.strings'))


    # def cleanup(self):
    #     dst = os.path.abspath('tests/output')
    #     if os.path.exists(dst):
    #         shutil.rmtree(dst)
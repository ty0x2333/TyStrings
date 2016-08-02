import unittest
from tystrings import *


class StringsTest(unittest.TestCase):
    def setUp(self):
        logger.level = logging.DEBUG
        self.addCleanup(self.cleanup)
        self.strings = Strings('')
        if os.path.exists(self.strings.filename):
            os.remove(self.strings.filename)

    def test_generate(self):
        self.strings.generate(['TyStringTest/TyStringTest/AppDelegate.m'])
        self.assertTrue(os.path.exists(self.strings.filename))

    def cleanup(self):
        if os.path.exists(self.strings.filename):
            os.remove(self.strings.filename)


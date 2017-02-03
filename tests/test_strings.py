import unittest
from tystrings import *
import shutil


class StringsTest(unittest.TestCase):
    def setUp(self):
        pass
        # logger.level = logging.DEBUG
        # self.addCleanup(self.cleanup)

    def test_generate(self):
        strings = Strings()
        strings.generate(['tests/example/IntegrationDemo.m'], dst='tests/output/generate')
        filenames = strings.generated_filenames
        self.assertTrue('Localizable.strings' in filenames)
        self.assertTrue('IntegrationTable.strings' in filenames)
        self.assertTrue(os.path.exists('tests/output/generate/Localizable.strings'))
        self.assertTrue(os.path.exists('tests/output/generate/IntegrationTable.strings'))

    def test_define(self):
        strings = Strings(aliases=['LOCALIZED', 'LOCALIZED_2'])
        results = strings.generate(['tests/example/DefineDemo.m'], 'tests/output/define')
        keys = results['Localizable.strings'].keys()
        self.assertTrue('Define.localizedString.define' in keys)
        self.assertTrue('Define.localizedString.define.2' in keys)
        self.assertTrue('Define.localizedString' in keys)

    def test_function(self):
        strings = Strings(aliases=['LocalizedFunctionDemoString'])
        results = strings.generate(['tests/example/FunctionDemo.m'], 'tests/output/function')
        keys = results['Localizable.strings'].keys()
        self.assertTrue('Function.localizedString.function' in keys)
        self.assertTrue('Function.localizedString' in keys)

    # def cleanup(self):
    #     dst = os.path.abspath('tests/output')
    #     if os.path.exists(dst):
    #         shutil.rmtree(dst)
import unittest

from tystrings import *


class StringsTest(unittest.TestCase):
    def setUp(self):
        pass
        # logger.level = logging.DEBUG
        # self.addCleanup(self.cleanup)

    def test_generate(self):
        instance = Strings()
        instance.generate(['tests/example/IntegrationDemo.m'], dst='tests/output/generate')
        filenames = instance.generated_filenames
        self.assertTrue('Localizable.strings' in filenames)
        self.assertTrue('IntegrationTable.strings' in filenames)
        self.assertTrue(os.path.exists('tests/output/generate/Localizable.strings'))
        self.assertTrue(os.path.exists('tests/output/generate/IntegrationTable.strings'))

    def test_define(self):
        instance = Strings(aliases=['LOCALIZED', 'LOCALIZED_2'])
        results = instance.generate(['tests/example/DefineDemo.m'], 'tests/output/define')
        keys = results['Localizable.strings'].keys()
        self.assertTrue('Define.localizedString.define' in keys)
        self.assertTrue('Define.localizedString.define.2' in keys)
        self.assertTrue('Define.localizedString' in keys)

    def test_function(self):
        instance = Strings(aliases=['LocalizedFunctionDemoString'])
        results = instance.generate(['tests/example/FunctionDemo.m'], 'tests/output/function')
        keys = results['Localizable.strings'].keys()
        self.assertTrue('Function.localizedString.function' in keys)
        self.assertTrue('Function.localizedString' in keys)

    # def cleanup(self):
    #     dst = os.path.abspath('tests/output')
    #     if os.path.exists(dst):
    #         shutil.rmtree(dst)

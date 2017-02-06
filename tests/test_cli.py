import unittest
import sys
import tempfile
import subprocess
import os
from shutil import rmtree
from tystrings import cli


class CLIBaseTest(unittest.TestCase):
    def setUp(self):
        self.temp_path = tempfile.mkdtemp()
        self.cwd = self.temp_path

    def tearDown(self):
        rmtree(self.temp_path)

    def call(self, *new_args, **kwargs):
        pass

    def test_base(self):
        self.assertEqual(0, self.call('-h'))
        self.assertEqual(0, self.call('--version'))

    def test_diff(self):
        subcommand = 'diff'
        self.assertEqual(0, self.call(subcommand, '-h'))

        file1 = os.path.abspath('tests/example/strings/diff1.strings')
        file2 = os.path.abspath('tests/example/strings/diff2.strings')
        self.assertEqual(0, self.call(subcommand, file1, file2, '-v'))

    def test_lint(self):
        subcommand = 'lint'
        self.assertEqual(0, self.call(subcommand, '-h'))

        dst = os.path.abspath('tests/example/strings/lint.strings')
        self.assertEqual(1, self.call(subcommand, dst, '-v'))

        dst = os.path.abspath('tests/example/strings/base.strings')
        self.assertEqual(0, self.call(subcommand, dst, '-v'))

    def test_translate(self):
        subcommand = 'translate'
        self.assertEqual(0, self.call(subcommand, '-h'))

        src = os.path.abspath('tests/example/strings/base_translator.strings')
        dst = os.path.join(self.cwd, 'base_translator.strings')
        dst_lang = 'zh'
        src_lang = 'en'

        self.assertEqual(0, self.call(subcommand, src, dst, '--dst-lang', dst_lang, '--src-lang', src_lang))
        self.assertTrue(os.path.exists(dst))
        os.remove(dst)

        self.assertEqual(0, self.call(subcommand, src, dst, '--dst-lang', dst_lang))
        self.assertTrue(os.path.exists(dst))

    def test_generate(self):
        subcommand = 'generate'
        self.assertEqual(0, self.call(subcommand, '-h'))

        src = os.path.abspath('tests/example/IntegrationDemo.m')
        dst = os.path.join(self.cwd, 'generate')

        # input directory
        self.assertEqual(2, self.call(subcommand, self.cwd, '-o', dst))
        # file not exists
        self.assertEqual(2, self.call(subcommand, 'xxxxxxx', '-o', dst))

        generated_path = os.path.join(dst, 'Localizable.strings')
        self.assertEqual(0, self.call(subcommand, src, '-o', dst))
        self.assertTrue(os.path.exists(generated_path))
        rmtree(dst)

        self.assertEqual(0, self.call(subcommand, src, '-o', dst, '--utf8'))
        self.assertTrue(os.path.exists(generated_path))


# class CLITests(CLIBaseTest):
#     def call(self, *new_args, **kwargs):
#         with tempfile.TemporaryFile() as out:
#             args = (sys.executable, '-m', 'tystrings.cli') + new_args
#             return subprocess.call(args, stdout=out, stderr=out, cwd=self.cwd, **kwargs)
#             # return subprocess.call(args, cwd=self.cwd, **kwargs)


class CLIWhiteTests(CLIBaseTest):
    def call(self, *new_args, **kwargs):
        with self.assertRaises(BaseException) as cm:
            cli.main(list(new_args))
        return cm.exception.code

# ignore base class
del(CLIBaseTest)

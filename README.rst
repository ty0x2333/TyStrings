.. code-block::

  _______     _____ _        _
 |__   __|   / ____| |      (_)
    | |_   _| (___ | |_ _ __ _ _ __   __ _ ___
    | | | | |\___ \| __| '__| | '_ \ / _` / __|
    | | |_| |____) | |_| |  | | | | | (_| \__ \
    |_|\__, |_____/ \__|_|  |_|_| |_|\__, |___/
        __/ |                         __/ |
       |___/                         |___/



strings file generation / translation tool for iOS

|pypi| |build| |coverage| |license|

Installation
============

.. code-block:: bash

  $ sudo pip install tystrings

Usage
-------
.. code-block:: bash

  $ tystrings -h
    usage: tystrings [-h] [--version] {generate,translate} ...

      _______     _____ _        _
     |__   __|   / ____| |      (_)
        | |_   _| (___ | |_ _ __ _ _ __   __ _ ___
        | | | | |\___ \| __| '__| | '_ \ / _` / __|
        | | |_| |____) | |_| |  | | | | | (_| \__ \
        |_|\__, |_____/ \__|_|  |_|_| |_|\__, |___/
            __/ |                         __/ |
           |___/                         |___/


    optional arguments:
      -h, --help            show this help message and exit
      --version             show program's version number and exit

    subcommands:
      {generate,translate}
        generate            generate `.strings` file from source code files.
        translate           using Baidu Translate Service to translate `.strings` file.

To run tystrings over all .m files in your project, you can invoke it, for example, like this:

.. code-block:: bash

  tystrings generate $(find . -name \*.m) -o en.lproj zh.lprog -v

translate .strings file to another language:

.. code-block:: bash

  tystrings translate en.lproj/Localizable.strings zh-Hans.lproj/Localizable.strings --src-lang en --dst-lang zh

.. |pypi| image:: https://img.shields.io/pypi/v/TyStrings.svg?maxAge=2592000
   :target: https://pypi.python.org/pypi/TyStrings
   :alt: Python Package Index

.. |license| image:: https://img.shields.io/github/license/luckytianyiyan/TyStrings.svg?maxAge=2592000
   :target: LICENSE
   :alt: MIT License

.. |build| image:: https://img.shields.io/travis/luckytianyiyan/TyStrings.svg?maxAge=2592000
   :target: https://travis-ci.org/luckytianyiyan/TyStrings
   :alt: Continuous Integration

.. |coverage| image:: https://coveralls.io/repos/github/luckytianyiyan/TyStrings/badge.svg
   :target: https://coveralls.io/github/luckytianyiyan/TyStrings
   :alt: Coverage Testing Results

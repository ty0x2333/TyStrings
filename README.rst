.. code-block::

  _______     _____ _        _
 |__   __|   / ____| |      (_)
    | |_   _| (___ | |_ _ __ _ _ __   __ _ ___
    | | | | |\___ \| __| '__| | '_ \ / _` / __|
    | | |_| |____) | |_| |  | | | | | (_| \__ \
    |_|\__, |_____/ \__|_|  |_|_| |_|\__, |___/
        __/ |                         __/ |
       |___/                         |___/



strings file generation tool for iOS

|pypi| |build| |coverage| |license|

Installation
============

.. code-block:: bash

  $ sudo pip install tystrings

Usage
-------
.. code-block:: bash

  $ tystrings -h
  usage: tystrings [-h] [--version] [-a ALIASES [ALIASES ...]] [-o DIR] [-v]
               file [file ...]

   _______     _____ _        _
  |__   __|   / ____| |      (_)
     | |_   _| (___ | |_ _ __ _ _ __   __ _ ___
     | | | | |\___ \| __| '__| | '_ \ / _` / __|
     | | |_| |____) | |_| |  | | | | | (_| \__ \
     |_|\__, |_____/ \__|_|  |_|_| |_|\__, |___/
         __/ |                         __/ |
        |___/                         |___/


   positional arguments:
   file                  source file .[mc]

   optional arguments:
   -h, --help            show this help message and exit
   --version             show program's version number and exit
   -a ALIASES [ALIASES ...], --aliases ALIASES [ALIASES ...]
                         aliases
   -o DIR, --output DIR  place output files in 'dir'
   -v, --verbose         show more debugging information

To run genstrings over all .m files in your project, you can invoke it, for example, like this:

.. code-block:: bash

  find . -name *.m | xargs tystrings -o en.lproj


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

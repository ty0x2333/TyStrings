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

Installation
============

.. code-block:: bash

  $ sudo pip install tystrings

Options
-------
.. code-block:: bash

  $ tystrings -h
    usage: tystrings [-h] [--version] [-o DIR] [-v] file [file ...]

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
      -o DIR, --output DIR  place output files in 'dir'
      -v, --verbose         show more debugging information

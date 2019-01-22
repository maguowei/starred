Starred
=======

.. image:: https://travis-ci.org/1132719438/starred.svg?branch=master
    :target: https://travis-ci.org/1132719438/starred
    :alt: Travis CI Status

.. image:: https://requires.io/github/1132719438/starred/requirements.svg?branch=master
     :target: https://requires.io/github/1132719438/starred/requirements/?branch=master
     :alt: Requirements Status

Install
-------

starred requires Python version 3.x

.. code:: bash

    $ git clone https://github.com/1132719438/starred
    $ pip3 install ./starred
    $ starred --username 1132719438 --output README.md


Usage
-----

.. code:: bash

    $ starred --help

    Usage: starred [OPTIONS]

      GitHub starred

      creating your own Awesome List used GitHub stars!

      example:     starred --username 1132719438 --output README.md

    Options:
      --username TEXT    GitHub username
      --token TEXT       GitHub token
      --sort             sort by language with stars, date or name
      --repository TEXT  repository name
      --message TEXT     commit message
      --output TEXT      output file name with path(print to stdout if not set)
      --launch           launch to Github after update repository
      --type             output repository information in table or list
      --version          Show the version and exit.
      --help             Show this message and exit.

Demo
----

.. code:: bash

    # automatically create the repository
    $ export GITHUB_TOKEN=<yourtoken>
    $ starred --username <yourname> --repository <repositoryname>

-  `Stars <https://github.com/1132719438/Stars>`__

FAQ
---

#. Generate new token

   goto `Personal access tokens <https://github.com/settings/tokens>`__

#. Why do I need a token?

   -  For unauthenticated requests, the rate limit is 60 requests per
      hour.
      see `Rate
      Limiting <https://developer.github.com/v3/#rate-limiting>`__
   -  The token must be passed together when you want to automatically
      create the repository.


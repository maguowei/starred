Starred
=======

.. image:: https://travis-ci.org/maguowei/starred.svg?branch=master
    :target: https://travis-ci.org/maguowei/starred
    :alt: Travis CI Status

.. image:: https://requires.io/github/maguowei/starred/requirements.svg?branch=master
     :target: https://requires.io/github/maguowei/starred/requirements/?branch=master
     :alt: Requirements Status

Install
-------

.. code:: bash

    $ pip install starred
    $ starred --username maguowei --sort > README.md

Usage
-----

.. code:: bash

    $ starred --help

    Usage: starred [OPTIONS]

      GitHub starred

      creating your own Awesome List used GitHub stars!

      example:     starred --username maguowei --sort > README.md

    Options:
      --username TEXT    GitHub username
      --token TEXT       GitHub token
      --sort             sort by language
      --repository TEXT  repository name
      --message TEXT     commit message
      --version          Show the version and exit.
      --help             Show this message and exit.

Demo
----

.. code:: bash

    # automatically create the repository
    $ export GITHUB_TOKEN=yourtoken
    $ starred --username yourname --repository awesome-stars --sort

-  `awesome-stars <https://github.com/maguowei/awesome-stars>`__

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

#. Install the master branch version

   .. code:: bash

      $ pip install -e git+https://github.com/maguowei/starred#egg=starred

"""
Starred
-----

Easy to Setup
`````````````

Install:
.. code:: bash
    $ pip install starred
    $ starred --username maguowei --sort > README.md

Links
`````

* `website <https://github.com/maguowei/starred>`_

"""


from setuptools import find_packages, setup

setup(
    name='starred',
    version='1.0.4',
    url='https://github.com/maguowei/starred',
    license='The MIT License (MIT)',
    author='maguowei',
    author_email='imaguowei@gmail.com',
    description='GitHub starred: make your own awesome lists page by GitHub star!',
    long_description=__doc__,
    py_modules=['starred'],
    platforms='any',
    install_requires=[
        'click==6.6',
        'github3.py==1.0.0a4',
    ],
    entry_points='''
        [console_scripts]
        starred=starred:starred
    ''',
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ),
)

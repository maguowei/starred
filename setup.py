from setuptools import find_packages, setup

setup(
    name='starred',
    version='1.0.2',
    url='https://github.com/maguowei/starred',
    license='The MIT License (MIT)',
    author='maguowei',
    author_email='imaguowei@gmail.com',
    description='''GitHub starred
     make your own awesome lists page by GitHub star!

     example:
        starred --username maguowei --sort > README.md
    ''',
    py_modules=['starred'],
    install_requires=[
        'click==6.6',
        'github3.py==1.0.0a4',
    ],
    entry_points='''
        [console_scripts]
        starred=starred:starred
    ''',
    classifiers=(
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ),
)

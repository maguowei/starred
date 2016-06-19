from setuptools import find_packages, setup

setup(
    name='starred',
    version='0.2.0',
    url='https://github.com/maguowei/starred',
    license='The MIT License (MIT)',
    author='maguowei',
    author_email='imaguowei@gmail.com',
    description='record github starred and change history',
    py_modules=['starred'],
    scripts=['starred.py'],
    install_requires=[
        'click==6.6',
        'github3.py==1.0.0a4',
    ],
    classifiers=(
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ),
)

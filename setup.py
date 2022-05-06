from setuptools import setup, find_packages
from os import path
from starred import VERSION


this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md')) as f:
    long_description = f.read()


setup(
    name='starred',
    version=VERSION,
    url='https://github.com/maguowei/starred',
    license='MIT',
    author='maguowei',
    author_email='imaguowei@gmail.com',
    keywords='GitHub starred',
    description='creating your own Awesome List used GitHub stars!',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    platforms='any',
    python_requires='>=3.7',
    install_requires=[
        'click==8.1.3',
        'requests==2.27.1',
        'github3.py==3.2.0',
    ],
    entry_points={
        'console_scripts': [
            'starred=starred.starred:starred'
        ]
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
)

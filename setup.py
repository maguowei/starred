from setuptools import setup, find_packages
from starred import VERSION

with open('README.rst') as f:
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
    packages=find_packages(),
    platforms='any',
    install_requires=[
        'click==7.0',
        'github3.py==1.3.0',
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
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)

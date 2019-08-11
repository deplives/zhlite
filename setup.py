# -*- coding: UTF-8 -*-
import setuptools
from zhlite import __version__, __author__, __email__


setuptools.setup(
    name="zhlite",
    version=__version__,
    author=__author__,
    author_email=__email__,
    description="zhihu lite client",
    license="MIT",
    url="https://github.com/deplives/zhlite",
    packages=['zhlite'],
    install_requires=[
        'requests==2.21.0',
        'beautifulsoup4==4.7.1',
        'lxml==4.3.4',
        'PyExecJS==1.5.1',
        'Pillow==6.0.0'
    ],
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]

)
from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.1'
DESCRIPTION = 'This app is a lil framework for PyQt5 like bootstrap for HTML5'
LONG_DESCRIPTION = 'A package that allows to build simple PyQt5 apps faster and cooler.'

# Setting up
setup(
    name="PyCutee",
    version=VERSION,
    author="Codingrule",
    author_email="<ioumih32@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['PyQt5'],
    keywords=['python', 'framework', 'pyqt5', 'frontend', 'customize', 'UI'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
# -*- coding: utf-8 -*-
"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages

# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

from django_states import __version__, __name__, __author__

name = "pivotal_" + __name__
base_url = "https://github.com/pivotal-energy-solutions/django-states2"

# Get the long description from the README file
with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

# Arguments marked as "Required" below must be included for upload to PyPI.
# Fields marked as "Optional" may be commented out.

setup(
    name=name,
    version=__version__,
    description="State machine for django models",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=base_url,  # Optional
    download_url="{0}/archive/{1}.tar.gz".format(base_url, __version__),
    author=__author__,  # Optional
    author_email="sklass@pivotalenergysolutions.com",  # Optional
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 2.2",
        "Framework :: Django :: 3.0",
        "Framework :: Django :: 3.1",
        "Framework :: Django :: 3.2",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Utilities",
    ],
    python_requires=">=3.8.*",
    keywords="django state-machine",  # Optional
    packages=find_packages(exclude=["contrib", "docs", "demo_app"]),  # Required
    install_requires=["Django>=2.2", "six"],  # Optional
    project_urls={  # Optional
        "Bug Reports": "{}/issues".format(base_url),
        "Say Thanks!": "https://saythanks.io/to/rh0dium",
        "Original Source": "https://github.com/vikingco/django-states2",
    },
)

import os
from setuptools import setup, find_packages

import django_states


setup(
    name="django-states",
    version=django_states.__version__,
    url='https://github.com/citylive/django-states2',
    license='BSD',
    description="State machine for django models",
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.rst')).read(),
    author='Jonathan Slenders, Gert van Gool, Maarten Timmerman, Steven (rh0dium)',
    author_email='jonathan.slenders@mobilevikings.com',
    packages=find_packages('.'),
    #package_dir={'': 'templates/*'},
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Operating System :: OS Independent',
        'Environment :: Web Environment',
        'Framework :: Django',
    ],
)

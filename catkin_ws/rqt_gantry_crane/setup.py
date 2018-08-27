#!/usr/bin/env python2

from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

d = generate_distutils_setup(
    packages=['rqt_gantry_crane'],
    package_dir={'': 'src'},
    scripts=['scripts/rqt_gantry_crane']
)

setup(**d)

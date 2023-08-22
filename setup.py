import os
from setuptools import Extension, setup
setup(ext_modules=[Extension('mypackage.simple',
                                 [os.path.join('mypackage', 'simple.c')])])

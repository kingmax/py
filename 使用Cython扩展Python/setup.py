import setuptools
from distutils.core import setup
from Cython.Build import cythonize

setup(ext_modules = cythonize("hello.pyx"))
setup(ext_modules = cythonize("fib.pyx"))
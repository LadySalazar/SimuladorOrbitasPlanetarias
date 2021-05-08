from distutils.core import setup, Extension
from Cython.Build import cythonize
import numpy

exts = (cythonize('cy_simulador.pyx'))

setup(ext_modules=exts,include_dirs=[numpy.get_include()])
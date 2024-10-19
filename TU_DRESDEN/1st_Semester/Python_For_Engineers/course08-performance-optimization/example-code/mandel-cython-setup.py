"script for conversion of cython-code to c-code"

from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
import numpy # to get includes


setup(
    cmdclass = {'build_ext': build_ext},
    ext_modules = [Extension("mandelcy", ["mandel-cython.pyx"], )],
    include_dirs = [numpy.get_include(),],
)

import sysconfig

from numpy import get_include as np_include
from setuptools import Extension, setup

FREE_THREADED_PYTHON = sysconfig.get_config_var("Py_GIL_DISABLED") == 1

MACROS = []
if not FREE_THREADED_PYTHON:
    MACROS.append(("Py_LIMITED_API", 0x03090000))  # PY_VERSION_HEX for 3.9

ext_modules = [
    Extension(
        "stsci.image._combine",
        ["src/_combinemodule.c"],
        include_dirs=[np_include()],
        define_macros=MACROS,
        py_limited_api=not FREE_THREADED_PYTHON,
    ),
]

SETUPTOOLS_OPTIONS = {}
if not FREE_THREADED_PYTHON:
    SETUPTOOLS_OPTIONS["bdist_wheel"] = {"py_limited_api": "cp39"}

setup(
    ext_modules=ext_modules,
    options=SETUPTOOLS_OPTIONS,
)

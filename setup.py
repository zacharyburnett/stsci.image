from numpy import get_include as np_include
from setuptools import Extension, setup

MACROS = [
    ("Py_LIMITED_API", 0x03090000),  # PY_VERSION_HEX for 3.9
]

ext_modules = [
    Extension(
        "stsci.image._combine",
        ["src/_combinemodule.c"],
        include_dirs=[np_include()],
        define_macros=MACROS,
    ),
]

setup(
    ext_modules=ext_modules,
    options={'bdist_wheel': {'py_limited_api': 'cp39'}},
)

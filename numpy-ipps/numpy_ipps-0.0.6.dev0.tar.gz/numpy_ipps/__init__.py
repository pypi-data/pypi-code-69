"""Numpy Intel IPP signal."""

import logging as _logging

import pkg_resources as _pkg_resources

import numpy_ipps._detail.debug as _debug
import numpy_ipps._detail.libipp as _libipp
import numpy_ipps.support as _support
from numpy_ipps.complex import *
from numpy_ipps.conversion import *
from numpy_ipps.exponential import *
from numpy_ipps.fft import *
from numpy_ipps.floating import *
from numpy_ipps.initialization import *
from numpy_ipps.integer import *
from numpy_ipps.logical import *
from numpy_ipps.rounding import *
from numpy_ipps.special import *
from numpy_ipps.trigonometric import *


__version__ = _pkg_resources.get_distribution(__name__).version

__title__ = "numpy_ipps"
__description__ = "Numpy Intel IPP signal."
__uri__ = "https://gitlab.com/fblanchet/numpy_ipps"

__author__ = "Florian Blanchet"
__email__ = "florian.blanchet@supoptique.org"
__license__ = "Apache Software License"
__copyright__ = "2020 Florian Blanchet"

__all__ = ["__version__"]


status = _libipp.ipp_core.ippInit()
_debug.assert_status(status, message="Init", name=__name__)

_logging.getLogger(__name__).info(
    "Intel IPP signal version {5} [{6}] for CPU target: {3}.".format(
        *_debug.safe_call(_support.library_version)
    )
)

_logging.getLogger(__name__).info(
    "CPU frequency: {:.3f} GHz.".format(
        _debug.safe_call(_support.cpu_frequency) * 1e-9
    )
)

_logging.getLogger(__name__).info("CPU cache information:")
for _cache_type, _cache_level, _cache_size in _debug.safe_call(
    _support.cache_params
):
    _logging.getLogger(__name__).info(
        "\tL{} {} cache: {:.3f} MB".format(
            _cache_level, _cache_type, _cache_size * 1e-6
        )
    )

_logging.getLogger(__name__).info("CPU features:")
for _feature in sorted(_debug.safe_call(_support.cpu_features)):
    _logging.getLogger(__name__).info("\t{}".format(_feature))

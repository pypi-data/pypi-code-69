"""Policies for tag dispatching."""
import ctypes as _ctypes
import enum as _enum

import numpy as _numpy


default_candidates = (
    _numpy.int8,
    _numpy.uint8,
    _numpy.int16,
    _numpy.uint16,
    _numpy.int32,
    _numpy.uint32,
    _numpy.int64,
    _numpy.uint64,
    _numpy.float32,
    _numpy.float64,
    _numpy.complex64,
    _numpy.complex128,
)
int_candidates = (
    _numpy.int8,
    _numpy.uint8,
    _numpy.int16,
    _numpy.uint16,
    _numpy.int32,
    _numpy.uint32,
    _numpy.int64,
    _numpy.uint64,
)
float_candidates = (
    _numpy.float32,
    _numpy.float64,
    _numpy.complex64,
    _numpy.complex128,
)
real_candidates = (
    _numpy.int8,
    _numpy.uint8,
    _numpy.int16,
    _numpy.uint16,
    _numpy.int32,
    _numpy.uint32,
    _numpy.int64,
    _numpy.uint64,
    _numpy.float32,
    _numpy.float64,
)
complex_candidates = (
    _numpy.complex64,
    _numpy.complex128,
)
no_complex_candidates = (
    _numpy.float32,
    _numpy.float64,
)


class Accuracy(_enum.Enum):
    """Accuracies enumeration."""

    LEVEL_1 = 1
    LEVEL_2 = 2
    LEVEL_3 = 3


default_accuracies = (Accuracy.LEVEL_1, Accuracy.LEVEL_3, Accuracy.LEVEL_2)


class TagPolicy(_enum.Enum):
    """Tag policies enumeration."""

    KEEP = 1
    UNSIGNED = 2
    SIGNED = 3
    FLOAT = 4
    DOWN_KEEP = 5
    DOWN_UNSIGNED = 6
    DOWN_SIGNED = 7
    SCALE_KEEP = 8
    SCALE_UNSIGNED = 9
    SCALE_SIGNED = 10
    INTEGER_SIGNED = 11
    INTEGER_UNSIGNED = 12


class TagAttr(_enum.IntEnum):
    """Int enumeration for tag attributes."""

    NAME = 0
    UTYPE = 1
    STYPE = 2
    FTYPE = 3
    DOWN = 4


down_tags = (
    TagPolicy.DOWN_KEEP,
    TagPolicy.DOWN_UNSIGNED,
    TagPolicy.DOWN_SIGNED,
)

scales_tags = (
    TagPolicy.SCALE_KEEP,
    TagPolicy.SCALE_UNSIGNED,
    TagPolicy.SCALE_SIGNED,
)


class Policies:
    """Policy class."""

    __slots__ = (
        "bytes1",
        "bytes2",
        "bytes4",
        "bytes8",
    )

    def __init__(
        self,
        bytes1=TagPolicy.KEEP,
        bytes2=TagPolicy.KEEP,
        bytes4=TagPolicy.KEEP,
        bytes8=TagPolicy.KEEP,
    ):
        self.bytes1 = (bytes1, _ctypes.c_uint8, _ctypes.c_int8, None, None)
        self.bytes2 = (
            bytes2,
            _ctypes.c_uint16,
            _ctypes.c_int16,
            None,
            _ctypes.c_int8,
        )
        self.bytes4 = (
            bytes4,
            _ctypes.c_uint32,
            _ctypes.c_int32,
            _numpy.ctypeslib.as_ctypes_type(_numpy.float32),
            _ctypes.c_int16,
        )
        self.bytes8 = (
            bytes8,
            _ctypes.c_uint64,
            _ctypes.c_int64,
            _numpy.ctypeslib.as_ctypes_type(_numpy.float64),
            _ctypes.c_int32,
        )


keep_all = Policies()
unsigned_all = Policies(
    bytes1=TagPolicy.UNSIGNED,
    bytes2=TagPolicy.UNSIGNED,
    bytes4=TagPolicy.INTEGER_UNSIGNED,
    bytes8=TagPolicy.INTEGER_UNSIGNED,
)
signed_all = Policies(
    bytes1=TagPolicy.SIGNED,
    bytes2=TagPolicy.SIGNED,
    bytes4=TagPolicy.INTEGER_SIGNED,
    bytes8=TagPolicy.INTEGER_SIGNED,
)
scaled_all = Policies(
    bytes1=TagPolicy.SCALE_KEEP,
    bytes2=TagPolicy.SCALE_KEEP,
    bytes4=TagPolicy.SCALE_KEEP,
    bytes8=TagPolicy.SCALE_KEEP,
)

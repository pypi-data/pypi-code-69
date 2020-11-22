# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.1
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.


from . import _LabelErodeDilatePython



from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _itkLabelSetDilateImageFilterPython
else:
    import _itkLabelSetDilateImageFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkLabelSetDilateImageFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkLabelSetDilateImageFilterPython.SWIG_PyStaticMethod_New

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


import itk.ITKCommonBasePython
import itk.pyBasePython
import itk.itkLabelSetMorphBaseImageFilterPython
import itk.itkImageToImageFilterAPython
import itk.itkVectorImagePython
import itk.stdcomplexPython
import itk.itkImagePython
import itk.itkMatrixPython
import itk.itkVectorPython
import itk.itkFixedArrayPython
import itk.vnl_vector_refPython
import itk.vnl_vectorPython
import itk.vnl_matrixPython
import itk.vnl_matrix_fixedPython
import itk.itkCovariantVectorPython
import itk.itkPointPython
import itk.itkRGBAPixelPython
import itk.itkSymmetricSecondRankTensorPython
import itk.itkRGBPixelPython
import itk.itkSizePython
import itk.itkImageRegionPython
import itk.itkIndexPython
import itk.itkOffsetPython
import itk.itkVariableLengthVectorPython
import itk.itkImageToImageFilterCommonPython
import itk.itkImageSourcePython
import itk.itkImageSourceCommonPython

def itkLabelSetDilateImageFilterID2ID2_New():
    return itkLabelSetDilateImageFilterID2ID2.New()

class itkLabelSetDilateImageFilterID2ID2(itk.itkLabelSetMorphBaseImageFilterPython.itkLabelSetMorphBaseImageFilterID2TRUEID2):
    r"""Proxy of C++ itkLabelSetDilateImageFilterID2ID2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkLabelSetDilateImageFilterPython.itkLabelSetDilateImageFilterID2ID2___New_orig__)
    Clone = _swig_new_instance_method(_itkLabelSetDilateImageFilterPython.itkLabelSetDilateImageFilterID2ID2_Clone)
    __swig_destroy__ = _itkLabelSetDilateImageFilterPython.delete_itkLabelSetDilateImageFilterID2ID2
    cast = _swig_new_static_method(_itkLabelSetDilateImageFilterPython.itkLabelSetDilateImageFilterID2ID2_cast)

    def New(*args, **kargs):
        """New() -> itkLabelSetDilateImageFilterID2ID2

        Create a new object of the class itkLabelSetDilateImageFilterID2ID2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLabelSetDilateImageFilterID2ID2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkLabelSetDilateImageFilterID2ID2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkLabelSetDilateImageFilterID2ID2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkLabelSetDilateImageFilterID2ID2 in _itkLabelSetDilateImageFilterPython:
_itkLabelSetDilateImageFilterPython.itkLabelSetDilateImageFilterID2ID2_swigregister(itkLabelSetDilateImageFilterID2ID2)
itkLabelSetDilateImageFilterID2ID2___New_orig__ = _itkLabelSetDilateImageFilterPython.itkLabelSetDilateImageFilterID2ID2___New_orig__
itkLabelSetDilateImageFilterID2ID2_cast = _itkLabelSetDilateImageFilterPython.itkLabelSetDilateImageFilterID2ID2_cast


def itkLabelSetDilateImageFilterID3ID3_New():
    return itkLabelSetDilateImageFilterID3ID3.New()

class itkLabelSetDilateImageFilterID3ID3(itk.itkLabelSetMorphBaseImageFilterPython.itkLabelSetMorphBaseImageFilterID3TRUEID3):
    r"""Proxy of C++ itkLabelSetDilateImageFilterID3ID3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkLabelSetDilateImageFilterPython.itkLabelSetDilateImageFilterID3ID3___New_orig__)
    Clone = _swig_new_instance_method(_itkLabelSetDilateImageFilterPython.itkLabelSetDilateImageFilterID3ID3_Clone)
    __swig_destroy__ = _itkLabelSetDilateImageFilterPython.delete_itkLabelSetDilateImageFilterID3ID3
    cast = _swig_new_static_method(_itkLabelSetDilateImageFilterPython.itkLabelSetDilateImageFilterID3ID3_cast)

    def New(*args, **kargs):
        """New() -> itkLabelSetDilateImageFilterID3ID3

        Create a new object of the class itkLabelSetDilateImageFilterID3ID3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLabelSetDilateImageFilterID3ID3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkLabelSetDilateImageFilterID3ID3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkLabelSetDilateImageFilterID3ID3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkLabelSetDilateImageFilterID3ID3 in _itkLabelSetDilateImageFilterPython:
_itkLabelSetDilateImageFilterPython.itkLabelSetDilateImageFilterID3ID3_swigregister(itkLabelSetDilateImageFilterID3ID3)
itkLabelSetDilateImageFilterID3ID3___New_orig__ = _itkLabelSetDilateImageFilterPython.itkLabelSetDilateImageFilterID3ID3___New_orig__
itkLabelSetDilateImageFilterID3ID3_cast = _itkLabelSetDilateImageFilterPython.itkLabelSetDilateImageFilterID3ID3_cast


def itkLabelSetDilateImageFilterIF2IF2_New():
    return itkLabelSetDilateImageFilterIF2IF2.New()

class itkLabelSetDilateImageFilterIF2IF2(itk.itkLabelSetMorphBaseImageFilterPython.itkLabelSetMorphBaseImageFilterIF2TRUEIF2):
    r"""Proxy of C++ itkLabelSetDilateImageFilterIF2IF2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkLabelSetDilateImageFilterPython.itkLabelSetDilateImageFilterIF2IF2___New_orig__)
    Clone = _swig_new_instance_method(_itkLabelSetDilateImageFilterPython.itkLabelSetDilateImageFilterIF2IF2_Clone)
    __swig_destroy__ = _itkLabelSetDilateImageFilterPython.delete_itkLabelSetDilateImageFilterIF2IF2
    cast = _swig_new_static_method(_itkLabelSetDilateImageFilterPython.itkLabelSetDilateImageFilterIF2IF2_cast)

    def New(*args, **kargs):
        """New() -> itkLabelSetDilateImageFilterIF2IF2

        Create a new object of the class itkLabelSetDilateImageFilterIF2IF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLabelSetDilateImageFilterIF2IF2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkLabelSetDilateImageFilterIF2IF2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkLabelSetDilateImageFilterIF2IF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkLabelSetDilateImageFilterIF2IF2 in _itkLabelSetDilateImageFilterPython:
_itkLabelSetDilateImageFilterPython.itkLabelSetDilateImageFilterIF2IF2_swigregister(itkLabelSetDilateImageFilterIF2IF2)
itkLabelSetDilateImageFilterIF2IF2___New_orig__ = _itkLabelSetDilateImageFilterPython.itkLabelSetDilateImageFilterIF2IF2___New_orig__
itkLabelSetDilateImageFilterIF2IF2_cast = _itkLabelSetDilateImageFilterPython.itkLabelSetDilateImageFilterIF2IF2_cast


def itkLabelSetDilateImageFilterIF3IF3_New():
    return itkLabelSetDilateImageFilterIF3IF3.New()

class itkLabelSetDilateImageFilterIF3IF3(itk.itkLabelSetMorphBaseImageFilterPython.itkLabelSetMorphBaseImageFilterIF3TRUEIF3):
    r"""Proxy of C++ itkLabelSetDilateImageFilterIF3IF3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkLabelSetDilateImageFilterPython.itkLabelSetDilateImageFilterIF3IF3___New_orig__)
    Clone = _swig_new_instance_method(_itkLabelSetDilateImageFilterPython.itkLabelSetDilateImageFilterIF3IF3_Clone)
    __swig_destroy__ = _itkLabelSetDilateImageFilterPython.delete_itkLabelSetDilateImageFilterIF3IF3
    cast = _swig_new_static_method(_itkLabelSetDilateImageFilterPython.itkLabelSetDilateImageFilterIF3IF3_cast)

    def New(*args, **kargs):
        """New() -> itkLabelSetDilateImageFilterIF3IF3

        Create a new object of the class itkLabelSetDilateImageFilterIF3IF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLabelSetDilateImageFilterIF3IF3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkLabelSetDilateImageFilterIF3IF3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkLabelSetDilateImageFilterIF3IF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkLabelSetDilateImageFilterIF3IF3 in _itkLabelSetDilateImageFilterPython:
_itkLabelSetDilateImageFilterPython.itkLabelSetDilateImageFilterIF3IF3_swigregister(itkLabelSetDilateImageFilterIF3IF3)
itkLabelSetDilateImageFilterIF3IF3___New_orig__ = _itkLabelSetDilateImageFilterPython.itkLabelSetDilateImageFilterIF3IF3___New_orig__
itkLabelSetDilateImageFilterIF3IF3_cast = _itkLabelSetDilateImageFilterPython.itkLabelSetDilateImageFilterIF3IF3_cast


def itkLabelSetDilateImageFilterISS2ISS2_New():
    return itkLabelSetDilateImageFilterISS2ISS2.New()

class itkLabelSetDilateImageFilterISS2ISS2(itk.itkLabelSetMorphBaseImageFilterPython.itkLabelSetMorphBaseImageFilterISS2TRUEISS2):
    r"""Proxy of C++ itkLabelSetDilateImageFilterISS2ISS2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkLabelSetDilateImageFilterPython.itkLabelSetDilateImageFilterISS2ISS2___New_orig__)
    Clone = _swig_new_instance_method(_itkLabelSetDilateImageFilterPython.itkLabelSetDilateImageFilterISS2ISS2_Clone)
    __swig_destroy__ = _itkLabelSetDilateImageFilterPython.delete_itkLabelSetDilateImageFilterISS2ISS2
    cast = _swig_new_static_method(_itkLabelSetDilateImageFilterPython.itkLabelSetDilateImageFilterISS2ISS2_cast)

    def New(*args, **kargs):
        """New() -> itkLabelSetDilateImageFilterISS2ISS2

        Create a new object of the class itkLabelSetDilateImageFilterISS2ISS2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLabelSetDilateImageFilterISS2ISS2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkLabelSetDilateImageFilterISS2ISS2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkLabelSetDilateImageFilterISS2ISS2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkLabelSetDilateImageFilterISS2ISS2 in _itkLabelSetDilateImageFilterPython:
_itkLabelSetDilateImageFilterPython.itkLabelSetDilateImageFilterISS2ISS2_swigregister(itkLabelSetDilateImageFilterISS2ISS2)
itkLabelSetDilateImageFilterISS2ISS2___New_orig__ = _itkLabelSetDilateImageFilterPython.itkLabelSetDilateImageFilterISS2ISS2___New_orig__
itkLabelSetDilateImageFilterISS2ISS2_cast = _itkLabelSetDilateImageFilterPython.itkLabelSetDilateImageFilterISS2ISS2_cast


def itkLabelSetDilateImageFilterISS3ISS3_New():
    return itkLabelSetDilateImageFilterISS3ISS3.New()

class itkLabelSetDilateImageFilterISS3ISS3(itk.itkLabelSetMorphBaseImageFilterPython.itkLabelSetMorphBaseImageFilterISS3TRUEISS3):
    r"""Proxy of C++ itkLabelSetDilateImageFilterISS3ISS3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkLabelSetDilateImageFilterPython.itkLabelSetDilateImageFilterISS3ISS3___New_orig__)
    Clone = _swig_new_instance_method(_itkLabelSetDilateImageFilterPython.itkLabelSetDilateImageFilterISS3ISS3_Clone)
    __swig_destroy__ = _itkLabelSetDilateImageFilterPython.delete_itkLabelSetDilateImageFilterISS3ISS3
    cast = _swig_new_static_method(_itkLabelSetDilateImageFilterPython.itkLabelSetDilateImageFilterISS3ISS3_cast)

    def New(*args, **kargs):
        """New() -> itkLabelSetDilateImageFilterISS3ISS3

        Create a new object of the class itkLabelSetDilateImageFilterISS3ISS3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLabelSetDilateImageFilterISS3ISS3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkLabelSetDilateImageFilterISS3ISS3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkLabelSetDilateImageFilterISS3ISS3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkLabelSetDilateImageFilterISS3ISS3 in _itkLabelSetDilateImageFilterPython:
_itkLabelSetDilateImageFilterPython.itkLabelSetDilateImageFilterISS3ISS3_swigregister(itkLabelSetDilateImageFilterISS3ISS3)
itkLabelSetDilateImageFilterISS3ISS3___New_orig__ = _itkLabelSetDilateImageFilterPython.itkLabelSetDilateImageFilterISS3ISS3___New_orig__
itkLabelSetDilateImageFilterISS3ISS3_cast = _itkLabelSetDilateImageFilterPython.itkLabelSetDilateImageFilterISS3ISS3_cast


def itkLabelSetDilateImageFilterIUC2IUC2_New():
    return itkLabelSetDilateImageFilterIUC2IUC2.New()

class itkLabelSetDilateImageFilterIUC2IUC2(itk.itkLabelSetMorphBaseImageFilterPython.itkLabelSetMorphBaseImageFilterIUC2TRUEIUC2):
    r"""Proxy of C++ itkLabelSetDilateImageFilterIUC2IUC2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkLabelSetDilateImageFilterPython.itkLabelSetDilateImageFilterIUC2IUC2___New_orig__)
    Clone = _swig_new_instance_method(_itkLabelSetDilateImageFilterPython.itkLabelSetDilateImageFilterIUC2IUC2_Clone)
    __swig_destroy__ = _itkLabelSetDilateImageFilterPython.delete_itkLabelSetDilateImageFilterIUC2IUC2
    cast = _swig_new_static_method(_itkLabelSetDilateImageFilterPython.itkLabelSetDilateImageFilterIUC2IUC2_cast)

    def New(*args, **kargs):
        """New() -> itkLabelSetDilateImageFilterIUC2IUC2

        Create a new object of the class itkLabelSetDilateImageFilterIUC2IUC2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLabelSetDilateImageFilterIUC2IUC2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkLabelSetDilateImageFilterIUC2IUC2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkLabelSetDilateImageFilterIUC2IUC2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkLabelSetDilateImageFilterIUC2IUC2 in _itkLabelSetDilateImageFilterPython:
_itkLabelSetDilateImageFilterPython.itkLabelSetDilateImageFilterIUC2IUC2_swigregister(itkLabelSetDilateImageFilterIUC2IUC2)
itkLabelSetDilateImageFilterIUC2IUC2___New_orig__ = _itkLabelSetDilateImageFilterPython.itkLabelSetDilateImageFilterIUC2IUC2___New_orig__
itkLabelSetDilateImageFilterIUC2IUC2_cast = _itkLabelSetDilateImageFilterPython.itkLabelSetDilateImageFilterIUC2IUC2_cast


def itkLabelSetDilateImageFilterIUC3IUC3_New():
    return itkLabelSetDilateImageFilterIUC3IUC3.New()

class itkLabelSetDilateImageFilterIUC3IUC3(itk.itkLabelSetMorphBaseImageFilterPython.itkLabelSetMorphBaseImageFilterIUC3TRUEIUC3):
    r"""Proxy of C++ itkLabelSetDilateImageFilterIUC3IUC3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkLabelSetDilateImageFilterPython.itkLabelSetDilateImageFilterIUC3IUC3___New_orig__)
    Clone = _swig_new_instance_method(_itkLabelSetDilateImageFilterPython.itkLabelSetDilateImageFilterIUC3IUC3_Clone)
    __swig_destroy__ = _itkLabelSetDilateImageFilterPython.delete_itkLabelSetDilateImageFilterIUC3IUC3
    cast = _swig_new_static_method(_itkLabelSetDilateImageFilterPython.itkLabelSetDilateImageFilterIUC3IUC3_cast)

    def New(*args, **kargs):
        """New() -> itkLabelSetDilateImageFilterIUC3IUC3

        Create a new object of the class itkLabelSetDilateImageFilterIUC3IUC3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLabelSetDilateImageFilterIUC3IUC3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkLabelSetDilateImageFilterIUC3IUC3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkLabelSetDilateImageFilterIUC3IUC3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkLabelSetDilateImageFilterIUC3IUC3 in _itkLabelSetDilateImageFilterPython:
_itkLabelSetDilateImageFilterPython.itkLabelSetDilateImageFilterIUC3IUC3_swigregister(itkLabelSetDilateImageFilterIUC3IUC3)
itkLabelSetDilateImageFilterIUC3IUC3___New_orig__ = _itkLabelSetDilateImageFilterPython.itkLabelSetDilateImageFilterIUC3IUC3___New_orig__
itkLabelSetDilateImageFilterIUC3IUC3_cast = _itkLabelSetDilateImageFilterPython.itkLabelSetDilateImageFilterIUC3IUC3_cast


def itkLabelSetDilateImageFilterIUS2IUS2_New():
    return itkLabelSetDilateImageFilterIUS2IUS2.New()

class itkLabelSetDilateImageFilterIUS2IUS2(itk.itkLabelSetMorphBaseImageFilterPython.itkLabelSetMorphBaseImageFilterIUS2TRUEIUS2):
    r"""Proxy of C++ itkLabelSetDilateImageFilterIUS2IUS2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkLabelSetDilateImageFilterPython.itkLabelSetDilateImageFilterIUS2IUS2___New_orig__)
    Clone = _swig_new_instance_method(_itkLabelSetDilateImageFilterPython.itkLabelSetDilateImageFilterIUS2IUS2_Clone)
    __swig_destroy__ = _itkLabelSetDilateImageFilterPython.delete_itkLabelSetDilateImageFilterIUS2IUS2
    cast = _swig_new_static_method(_itkLabelSetDilateImageFilterPython.itkLabelSetDilateImageFilterIUS2IUS2_cast)

    def New(*args, **kargs):
        """New() -> itkLabelSetDilateImageFilterIUS2IUS2

        Create a new object of the class itkLabelSetDilateImageFilterIUS2IUS2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLabelSetDilateImageFilterIUS2IUS2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkLabelSetDilateImageFilterIUS2IUS2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkLabelSetDilateImageFilterIUS2IUS2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkLabelSetDilateImageFilterIUS2IUS2 in _itkLabelSetDilateImageFilterPython:
_itkLabelSetDilateImageFilterPython.itkLabelSetDilateImageFilterIUS2IUS2_swigregister(itkLabelSetDilateImageFilterIUS2IUS2)
itkLabelSetDilateImageFilterIUS2IUS2___New_orig__ = _itkLabelSetDilateImageFilterPython.itkLabelSetDilateImageFilterIUS2IUS2___New_orig__
itkLabelSetDilateImageFilterIUS2IUS2_cast = _itkLabelSetDilateImageFilterPython.itkLabelSetDilateImageFilterIUS2IUS2_cast


def itkLabelSetDilateImageFilterIUS3IUS3_New():
    return itkLabelSetDilateImageFilterIUS3IUS3.New()

class itkLabelSetDilateImageFilterIUS3IUS3(itk.itkLabelSetMorphBaseImageFilterPython.itkLabelSetMorphBaseImageFilterIUS3TRUEIUS3):
    r"""Proxy of C++ itkLabelSetDilateImageFilterIUS3IUS3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkLabelSetDilateImageFilterPython.itkLabelSetDilateImageFilterIUS3IUS3___New_orig__)
    Clone = _swig_new_instance_method(_itkLabelSetDilateImageFilterPython.itkLabelSetDilateImageFilterIUS3IUS3_Clone)
    __swig_destroy__ = _itkLabelSetDilateImageFilterPython.delete_itkLabelSetDilateImageFilterIUS3IUS3
    cast = _swig_new_static_method(_itkLabelSetDilateImageFilterPython.itkLabelSetDilateImageFilterIUS3IUS3_cast)

    def New(*args, **kargs):
        """New() -> itkLabelSetDilateImageFilterIUS3IUS3

        Create a new object of the class itkLabelSetDilateImageFilterIUS3IUS3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLabelSetDilateImageFilterIUS3IUS3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkLabelSetDilateImageFilterIUS3IUS3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkLabelSetDilateImageFilterIUS3IUS3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkLabelSetDilateImageFilterIUS3IUS3 in _itkLabelSetDilateImageFilterPython:
_itkLabelSetDilateImageFilterPython.itkLabelSetDilateImageFilterIUS3IUS3_swigregister(itkLabelSetDilateImageFilterIUS3IUS3)
itkLabelSetDilateImageFilterIUS3IUS3___New_orig__ = _itkLabelSetDilateImageFilterPython.itkLabelSetDilateImageFilterIUS3IUS3___New_orig__
itkLabelSetDilateImageFilterIUS3IUS3_cast = _itkLabelSetDilateImageFilterPython.itkLabelSetDilateImageFilterIUS3IUS3_cast


import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def label_set_dilate_image_filter(*args, **kwargs):
    """Procedural interface for LabelSetDilateImageFilter"""
    import itk
    instance = itk.LabelSetDilateImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def label_set_dilate_image_filter_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.LabelSetDilateImageFilter, itkTemplate.itkTemplate):
        filter_object = itk.LabelSetDilateImageFilter.values()[0]
    else:
        filter_object = itk.LabelSetDilateImageFilter

    label_set_dilate_image_filter.__doc__ = filter_object.__doc__
    label_set_dilate_image_filter.__doc__ += "\n Args are Input(s) to the filter.\n"
    label_set_dilate_image_filter.__doc__ += "\n Available Keyword Arguments:\n"
    if isinstance(itk.LabelSetDilateImageFilter, itkTemplate.itkTemplate):
        label_set_dilate_image_filter.__doc__ += itkHelpers.filter_args(filter_object)[0]
        label_set_dilate_image_filter.__doc__ += "\n"
        label_set_dilate_image_filter.__doc__ += itkHelpers.filter_args(filter_object)[1]
    else:
        label_set_dilate_image_filter.__doc__ += "".join([
            "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
            for item in dir(filter_object)
            if item.startswith("Set")])




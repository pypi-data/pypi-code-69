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
    from . import _itkLabelSetErodeImageFilterPython
else:
    import _itkLabelSetErodeImageFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkLabelSetErodeImageFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkLabelSetErodeImageFilterPython.SWIG_PyStaticMethod_New

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


import itk.itkLabelSetMorphBaseImageFilterPython
import itk.itkImageToImageFilterAPython
import itk.itkImageRegionPython
import itk.ITKCommonBasePython
import itk.pyBasePython
import itk.itkSizePython
import itk.itkIndexPython
import itk.itkOffsetPython
import itk.itkImagePython
import itk.itkRGBPixelPython
import itk.itkFixedArrayPython
import itk.itkPointPython
import itk.itkVectorPython
import itk.vnl_vector_refPython
import itk.vnl_vectorPython
import itk.vnl_matrixPython
import itk.stdcomplexPython
import itk.itkSymmetricSecondRankTensorPython
import itk.itkMatrixPython
import itk.vnl_matrix_fixedPython
import itk.itkCovariantVectorPython
import itk.itkRGBAPixelPython
import itk.itkVectorImagePython
import itk.itkVariableLengthVectorPython
import itk.itkImageToImageFilterCommonPython
import itk.itkImageSourcePython
import itk.itkImageSourceCommonPython

def itkLabelSetErodeImageFilterID2ID2_New():
    return itkLabelSetErodeImageFilterID2ID2.New()

class itkLabelSetErodeImageFilterID2ID2(itk.itkLabelSetMorphBaseImageFilterPython.itkLabelSetMorphBaseImageFilterID2FALSEID2):
    r"""Proxy of C++ itkLabelSetErodeImageFilterID2ID2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkLabelSetErodeImageFilterPython.itkLabelSetErodeImageFilterID2ID2___New_orig__)
    Clone = _swig_new_instance_method(_itkLabelSetErodeImageFilterPython.itkLabelSetErodeImageFilterID2ID2_Clone)
    __swig_destroy__ = _itkLabelSetErodeImageFilterPython.delete_itkLabelSetErodeImageFilterID2ID2
    cast = _swig_new_static_method(_itkLabelSetErodeImageFilterPython.itkLabelSetErodeImageFilterID2ID2_cast)

    def New(*args, **kargs):
        """New() -> itkLabelSetErodeImageFilterID2ID2

        Create a new object of the class itkLabelSetErodeImageFilterID2ID2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLabelSetErodeImageFilterID2ID2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkLabelSetErodeImageFilterID2ID2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkLabelSetErodeImageFilterID2ID2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkLabelSetErodeImageFilterID2ID2 in _itkLabelSetErodeImageFilterPython:
_itkLabelSetErodeImageFilterPython.itkLabelSetErodeImageFilterID2ID2_swigregister(itkLabelSetErodeImageFilterID2ID2)
itkLabelSetErodeImageFilterID2ID2___New_orig__ = _itkLabelSetErodeImageFilterPython.itkLabelSetErodeImageFilterID2ID2___New_orig__
itkLabelSetErodeImageFilterID2ID2_cast = _itkLabelSetErodeImageFilterPython.itkLabelSetErodeImageFilterID2ID2_cast


def itkLabelSetErodeImageFilterID3ID3_New():
    return itkLabelSetErodeImageFilterID3ID3.New()

class itkLabelSetErodeImageFilterID3ID3(itk.itkLabelSetMorphBaseImageFilterPython.itkLabelSetMorphBaseImageFilterID3FALSEID3):
    r"""Proxy of C++ itkLabelSetErodeImageFilterID3ID3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkLabelSetErodeImageFilterPython.itkLabelSetErodeImageFilterID3ID3___New_orig__)
    Clone = _swig_new_instance_method(_itkLabelSetErodeImageFilterPython.itkLabelSetErodeImageFilterID3ID3_Clone)
    __swig_destroy__ = _itkLabelSetErodeImageFilterPython.delete_itkLabelSetErodeImageFilterID3ID3
    cast = _swig_new_static_method(_itkLabelSetErodeImageFilterPython.itkLabelSetErodeImageFilterID3ID3_cast)

    def New(*args, **kargs):
        """New() -> itkLabelSetErodeImageFilterID3ID3

        Create a new object of the class itkLabelSetErodeImageFilterID3ID3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLabelSetErodeImageFilterID3ID3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkLabelSetErodeImageFilterID3ID3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkLabelSetErodeImageFilterID3ID3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkLabelSetErodeImageFilterID3ID3 in _itkLabelSetErodeImageFilterPython:
_itkLabelSetErodeImageFilterPython.itkLabelSetErodeImageFilterID3ID3_swigregister(itkLabelSetErodeImageFilterID3ID3)
itkLabelSetErodeImageFilterID3ID3___New_orig__ = _itkLabelSetErodeImageFilterPython.itkLabelSetErodeImageFilterID3ID3___New_orig__
itkLabelSetErodeImageFilterID3ID3_cast = _itkLabelSetErodeImageFilterPython.itkLabelSetErodeImageFilterID3ID3_cast


def itkLabelSetErodeImageFilterIF2IF2_New():
    return itkLabelSetErodeImageFilterIF2IF2.New()

class itkLabelSetErodeImageFilterIF2IF2(itk.itkLabelSetMorphBaseImageFilterPython.itkLabelSetMorphBaseImageFilterIF2FALSEIF2):
    r"""Proxy of C++ itkLabelSetErodeImageFilterIF2IF2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkLabelSetErodeImageFilterPython.itkLabelSetErodeImageFilterIF2IF2___New_orig__)
    Clone = _swig_new_instance_method(_itkLabelSetErodeImageFilterPython.itkLabelSetErodeImageFilterIF2IF2_Clone)
    __swig_destroy__ = _itkLabelSetErodeImageFilterPython.delete_itkLabelSetErodeImageFilterIF2IF2
    cast = _swig_new_static_method(_itkLabelSetErodeImageFilterPython.itkLabelSetErodeImageFilterIF2IF2_cast)

    def New(*args, **kargs):
        """New() -> itkLabelSetErodeImageFilterIF2IF2

        Create a new object of the class itkLabelSetErodeImageFilterIF2IF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLabelSetErodeImageFilterIF2IF2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkLabelSetErodeImageFilterIF2IF2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkLabelSetErodeImageFilterIF2IF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkLabelSetErodeImageFilterIF2IF2 in _itkLabelSetErodeImageFilterPython:
_itkLabelSetErodeImageFilterPython.itkLabelSetErodeImageFilterIF2IF2_swigregister(itkLabelSetErodeImageFilterIF2IF2)
itkLabelSetErodeImageFilterIF2IF2___New_orig__ = _itkLabelSetErodeImageFilterPython.itkLabelSetErodeImageFilterIF2IF2___New_orig__
itkLabelSetErodeImageFilterIF2IF2_cast = _itkLabelSetErodeImageFilterPython.itkLabelSetErodeImageFilterIF2IF2_cast


def itkLabelSetErodeImageFilterIF3IF3_New():
    return itkLabelSetErodeImageFilterIF3IF3.New()

class itkLabelSetErodeImageFilterIF3IF3(itk.itkLabelSetMorphBaseImageFilterPython.itkLabelSetMorphBaseImageFilterIF3FALSEIF3):
    r"""Proxy of C++ itkLabelSetErodeImageFilterIF3IF3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkLabelSetErodeImageFilterPython.itkLabelSetErodeImageFilterIF3IF3___New_orig__)
    Clone = _swig_new_instance_method(_itkLabelSetErodeImageFilterPython.itkLabelSetErodeImageFilterIF3IF3_Clone)
    __swig_destroy__ = _itkLabelSetErodeImageFilterPython.delete_itkLabelSetErodeImageFilterIF3IF3
    cast = _swig_new_static_method(_itkLabelSetErodeImageFilterPython.itkLabelSetErodeImageFilterIF3IF3_cast)

    def New(*args, **kargs):
        """New() -> itkLabelSetErodeImageFilterIF3IF3

        Create a new object of the class itkLabelSetErodeImageFilterIF3IF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLabelSetErodeImageFilterIF3IF3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkLabelSetErodeImageFilterIF3IF3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkLabelSetErodeImageFilterIF3IF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkLabelSetErodeImageFilterIF3IF3 in _itkLabelSetErodeImageFilterPython:
_itkLabelSetErodeImageFilterPython.itkLabelSetErodeImageFilterIF3IF3_swigregister(itkLabelSetErodeImageFilterIF3IF3)
itkLabelSetErodeImageFilterIF3IF3___New_orig__ = _itkLabelSetErodeImageFilterPython.itkLabelSetErodeImageFilterIF3IF3___New_orig__
itkLabelSetErodeImageFilterIF3IF3_cast = _itkLabelSetErodeImageFilterPython.itkLabelSetErodeImageFilterIF3IF3_cast


def itkLabelSetErodeImageFilterISS2ISS2_New():
    return itkLabelSetErodeImageFilterISS2ISS2.New()

class itkLabelSetErodeImageFilterISS2ISS2(itk.itkLabelSetMorphBaseImageFilterPython.itkLabelSetMorphBaseImageFilterISS2FALSEISS2):
    r"""Proxy of C++ itkLabelSetErodeImageFilterISS2ISS2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkLabelSetErodeImageFilterPython.itkLabelSetErodeImageFilterISS2ISS2___New_orig__)
    Clone = _swig_new_instance_method(_itkLabelSetErodeImageFilterPython.itkLabelSetErodeImageFilterISS2ISS2_Clone)
    __swig_destroy__ = _itkLabelSetErodeImageFilterPython.delete_itkLabelSetErodeImageFilterISS2ISS2
    cast = _swig_new_static_method(_itkLabelSetErodeImageFilterPython.itkLabelSetErodeImageFilterISS2ISS2_cast)

    def New(*args, **kargs):
        """New() -> itkLabelSetErodeImageFilterISS2ISS2

        Create a new object of the class itkLabelSetErodeImageFilterISS2ISS2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLabelSetErodeImageFilterISS2ISS2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkLabelSetErodeImageFilterISS2ISS2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkLabelSetErodeImageFilterISS2ISS2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkLabelSetErodeImageFilterISS2ISS2 in _itkLabelSetErodeImageFilterPython:
_itkLabelSetErodeImageFilterPython.itkLabelSetErodeImageFilterISS2ISS2_swigregister(itkLabelSetErodeImageFilterISS2ISS2)
itkLabelSetErodeImageFilterISS2ISS2___New_orig__ = _itkLabelSetErodeImageFilterPython.itkLabelSetErodeImageFilterISS2ISS2___New_orig__
itkLabelSetErodeImageFilterISS2ISS2_cast = _itkLabelSetErodeImageFilterPython.itkLabelSetErodeImageFilterISS2ISS2_cast


def itkLabelSetErodeImageFilterISS3ISS3_New():
    return itkLabelSetErodeImageFilterISS3ISS3.New()

class itkLabelSetErodeImageFilterISS3ISS3(itk.itkLabelSetMorphBaseImageFilterPython.itkLabelSetMorphBaseImageFilterISS3FALSEISS3):
    r"""Proxy of C++ itkLabelSetErodeImageFilterISS3ISS3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkLabelSetErodeImageFilterPython.itkLabelSetErodeImageFilterISS3ISS3___New_orig__)
    Clone = _swig_new_instance_method(_itkLabelSetErodeImageFilterPython.itkLabelSetErodeImageFilterISS3ISS3_Clone)
    __swig_destroy__ = _itkLabelSetErodeImageFilterPython.delete_itkLabelSetErodeImageFilterISS3ISS3
    cast = _swig_new_static_method(_itkLabelSetErodeImageFilterPython.itkLabelSetErodeImageFilterISS3ISS3_cast)

    def New(*args, **kargs):
        """New() -> itkLabelSetErodeImageFilterISS3ISS3

        Create a new object of the class itkLabelSetErodeImageFilterISS3ISS3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLabelSetErodeImageFilterISS3ISS3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkLabelSetErodeImageFilterISS3ISS3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkLabelSetErodeImageFilterISS3ISS3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkLabelSetErodeImageFilterISS3ISS3 in _itkLabelSetErodeImageFilterPython:
_itkLabelSetErodeImageFilterPython.itkLabelSetErodeImageFilterISS3ISS3_swigregister(itkLabelSetErodeImageFilterISS3ISS3)
itkLabelSetErodeImageFilterISS3ISS3___New_orig__ = _itkLabelSetErodeImageFilterPython.itkLabelSetErodeImageFilterISS3ISS3___New_orig__
itkLabelSetErodeImageFilterISS3ISS3_cast = _itkLabelSetErodeImageFilterPython.itkLabelSetErodeImageFilterISS3ISS3_cast


def itkLabelSetErodeImageFilterIUC2IUC2_New():
    return itkLabelSetErodeImageFilterIUC2IUC2.New()

class itkLabelSetErodeImageFilterIUC2IUC2(itk.itkLabelSetMorphBaseImageFilterPython.itkLabelSetMorphBaseImageFilterIUC2FALSEIUC2):
    r"""Proxy of C++ itkLabelSetErodeImageFilterIUC2IUC2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkLabelSetErodeImageFilterPython.itkLabelSetErodeImageFilterIUC2IUC2___New_orig__)
    Clone = _swig_new_instance_method(_itkLabelSetErodeImageFilterPython.itkLabelSetErodeImageFilterIUC2IUC2_Clone)
    __swig_destroy__ = _itkLabelSetErodeImageFilterPython.delete_itkLabelSetErodeImageFilterIUC2IUC2
    cast = _swig_new_static_method(_itkLabelSetErodeImageFilterPython.itkLabelSetErodeImageFilterIUC2IUC2_cast)

    def New(*args, **kargs):
        """New() -> itkLabelSetErodeImageFilterIUC2IUC2

        Create a new object of the class itkLabelSetErodeImageFilterIUC2IUC2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLabelSetErodeImageFilterIUC2IUC2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkLabelSetErodeImageFilterIUC2IUC2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkLabelSetErodeImageFilterIUC2IUC2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkLabelSetErodeImageFilterIUC2IUC2 in _itkLabelSetErodeImageFilterPython:
_itkLabelSetErodeImageFilterPython.itkLabelSetErodeImageFilterIUC2IUC2_swigregister(itkLabelSetErodeImageFilterIUC2IUC2)
itkLabelSetErodeImageFilterIUC2IUC2___New_orig__ = _itkLabelSetErodeImageFilterPython.itkLabelSetErodeImageFilterIUC2IUC2___New_orig__
itkLabelSetErodeImageFilterIUC2IUC2_cast = _itkLabelSetErodeImageFilterPython.itkLabelSetErodeImageFilterIUC2IUC2_cast


def itkLabelSetErodeImageFilterIUC3IUC3_New():
    return itkLabelSetErodeImageFilterIUC3IUC3.New()

class itkLabelSetErodeImageFilterIUC3IUC3(itk.itkLabelSetMorphBaseImageFilterPython.itkLabelSetMorphBaseImageFilterIUC3FALSEIUC3):
    r"""Proxy of C++ itkLabelSetErodeImageFilterIUC3IUC3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkLabelSetErodeImageFilterPython.itkLabelSetErodeImageFilterIUC3IUC3___New_orig__)
    Clone = _swig_new_instance_method(_itkLabelSetErodeImageFilterPython.itkLabelSetErodeImageFilterIUC3IUC3_Clone)
    __swig_destroy__ = _itkLabelSetErodeImageFilterPython.delete_itkLabelSetErodeImageFilterIUC3IUC3
    cast = _swig_new_static_method(_itkLabelSetErodeImageFilterPython.itkLabelSetErodeImageFilterIUC3IUC3_cast)

    def New(*args, **kargs):
        """New() -> itkLabelSetErodeImageFilterIUC3IUC3

        Create a new object of the class itkLabelSetErodeImageFilterIUC3IUC3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLabelSetErodeImageFilterIUC3IUC3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkLabelSetErodeImageFilterIUC3IUC3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkLabelSetErodeImageFilterIUC3IUC3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkLabelSetErodeImageFilterIUC3IUC3 in _itkLabelSetErodeImageFilterPython:
_itkLabelSetErodeImageFilterPython.itkLabelSetErodeImageFilterIUC3IUC3_swigregister(itkLabelSetErodeImageFilterIUC3IUC3)
itkLabelSetErodeImageFilterIUC3IUC3___New_orig__ = _itkLabelSetErodeImageFilterPython.itkLabelSetErodeImageFilterIUC3IUC3___New_orig__
itkLabelSetErodeImageFilterIUC3IUC3_cast = _itkLabelSetErodeImageFilterPython.itkLabelSetErodeImageFilterIUC3IUC3_cast


def itkLabelSetErodeImageFilterIUS2IUS2_New():
    return itkLabelSetErodeImageFilterIUS2IUS2.New()

class itkLabelSetErodeImageFilterIUS2IUS2(itk.itkLabelSetMorphBaseImageFilterPython.itkLabelSetMorphBaseImageFilterIUS2FALSEIUS2):
    r"""Proxy of C++ itkLabelSetErodeImageFilterIUS2IUS2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkLabelSetErodeImageFilterPython.itkLabelSetErodeImageFilterIUS2IUS2___New_orig__)
    Clone = _swig_new_instance_method(_itkLabelSetErodeImageFilterPython.itkLabelSetErodeImageFilterIUS2IUS2_Clone)
    __swig_destroy__ = _itkLabelSetErodeImageFilterPython.delete_itkLabelSetErodeImageFilterIUS2IUS2
    cast = _swig_new_static_method(_itkLabelSetErodeImageFilterPython.itkLabelSetErodeImageFilterIUS2IUS2_cast)

    def New(*args, **kargs):
        """New() -> itkLabelSetErodeImageFilterIUS2IUS2

        Create a new object of the class itkLabelSetErodeImageFilterIUS2IUS2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLabelSetErodeImageFilterIUS2IUS2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkLabelSetErodeImageFilterIUS2IUS2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkLabelSetErodeImageFilterIUS2IUS2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkLabelSetErodeImageFilterIUS2IUS2 in _itkLabelSetErodeImageFilterPython:
_itkLabelSetErodeImageFilterPython.itkLabelSetErodeImageFilterIUS2IUS2_swigregister(itkLabelSetErodeImageFilterIUS2IUS2)
itkLabelSetErodeImageFilterIUS2IUS2___New_orig__ = _itkLabelSetErodeImageFilterPython.itkLabelSetErodeImageFilterIUS2IUS2___New_orig__
itkLabelSetErodeImageFilterIUS2IUS2_cast = _itkLabelSetErodeImageFilterPython.itkLabelSetErodeImageFilterIUS2IUS2_cast


def itkLabelSetErodeImageFilterIUS3IUS3_New():
    return itkLabelSetErodeImageFilterIUS3IUS3.New()

class itkLabelSetErodeImageFilterIUS3IUS3(itk.itkLabelSetMorphBaseImageFilterPython.itkLabelSetMorphBaseImageFilterIUS3FALSEIUS3):
    r"""Proxy of C++ itkLabelSetErodeImageFilterIUS3IUS3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkLabelSetErodeImageFilterPython.itkLabelSetErodeImageFilterIUS3IUS3___New_orig__)
    Clone = _swig_new_instance_method(_itkLabelSetErodeImageFilterPython.itkLabelSetErodeImageFilterIUS3IUS3_Clone)
    __swig_destroy__ = _itkLabelSetErodeImageFilterPython.delete_itkLabelSetErodeImageFilterIUS3IUS3
    cast = _swig_new_static_method(_itkLabelSetErodeImageFilterPython.itkLabelSetErodeImageFilterIUS3IUS3_cast)

    def New(*args, **kargs):
        """New() -> itkLabelSetErodeImageFilterIUS3IUS3

        Create a new object of the class itkLabelSetErodeImageFilterIUS3IUS3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLabelSetErodeImageFilterIUS3IUS3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkLabelSetErodeImageFilterIUS3IUS3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkLabelSetErodeImageFilterIUS3IUS3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkLabelSetErodeImageFilterIUS3IUS3 in _itkLabelSetErodeImageFilterPython:
_itkLabelSetErodeImageFilterPython.itkLabelSetErodeImageFilterIUS3IUS3_swigregister(itkLabelSetErodeImageFilterIUS3IUS3)
itkLabelSetErodeImageFilterIUS3IUS3___New_orig__ = _itkLabelSetErodeImageFilterPython.itkLabelSetErodeImageFilterIUS3IUS3___New_orig__
itkLabelSetErodeImageFilterIUS3IUS3_cast = _itkLabelSetErodeImageFilterPython.itkLabelSetErodeImageFilterIUS3IUS3_cast


import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def label_set_erode_image_filter(*args, **kwargs):
    """Procedural interface for LabelSetErodeImageFilter"""
    import itk
    instance = itk.LabelSetErodeImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def label_set_erode_image_filter_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.LabelSetErodeImageFilter, itkTemplate.itkTemplate):
        filter_object = itk.LabelSetErodeImageFilter.values()[0]
    else:
        filter_object = itk.LabelSetErodeImageFilter

    label_set_erode_image_filter.__doc__ = filter_object.__doc__
    label_set_erode_image_filter.__doc__ += "\n Args are Input(s) to the filter.\n"
    label_set_erode_image_filter.__doc__ += "\n Available Keyword Arguments:\n"
    if isinstance(itk.LabelSetErodeImageFilter, itkTemplate.itkTemplate):
        label_set_erode_image_filter.__doc__ += itkHelpers.filter_args(filter_object)[0]
        label_set_erode_image_filter.__doc__ += "\n"
        label_set_erode_image_filter.__doc__ += itkHelpers.filter_args(filter_object)[1]
    else:
        label_set_erode_image_filter.__doc__ += "".join([
            "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
            for item in dir(filter_object)
            if item.startswith("Set")])




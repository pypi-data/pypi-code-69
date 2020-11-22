# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.1
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.


from . import _FixedPointInverseDisplacementFieldPython



from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _itkFixedPointInverseDisplacementFieldImageFilterPython
else:
    import _itkFixedPointInverseDisplacementFieldImageFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkFixedPointInverseDisplacementFieldImageFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkFixedPointInverseDisplacementFieldImageFilterPython.SWIG_PyStaticMethod_New

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
import itk.itkPointPython
import itk.itkFixedArrayPython
import itk.itkVectorPython
import itk.vnl_vectorPython
import itk.stdcomplexPython
import itk.vnl_matrixPython
import itk.vnl_vector_refPython
import itk.itkSizePython
import itk.itkImageToImageFilterAPython
import itk.itkVectorImagePython
import itk.itkIndexPython
import itk.itkOffsetPython
import itk.itkImagePython
import itk.itkRGBAPixelPython
import itk.itkSymmetricSecondRankTensorPython
import itk.itkMatrixPython
import itk.vnl_matrix_fixedPython
import itk.itkCovariantVectorPython
import itk.itkImageRegionPython
import itk.itkRGBPixelPython
import itk.itkVariableLengthVectorPython
import itk.itkImageSourcePython
import itk.itkImageSourceCommonPython
import itk.itkImageToImageFilterCommonPython

def itkFixedPointInverseDisplacementFieldImageFilterIVF22IVF22_New():
    return itkFixedPointInverseDisplacementFieldImageFilterIVF22IVF22.New()

class itkFixedPointInverseDisplacementFieldImageFilterIVF22IVF22(itk.itkImageToImageFilterAPython.itkImageToImageFilterIVF22IVF22):
    r"""Proxy of C++ itkFixedPointInverseDisplacementFieldImageFilterIVF22IVF22 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkFixedPointInverseDisplacementFieldImageFilterPython.itkFixedPointInverseDisplacementFieldImageFilterIVF22IVF22___New_orig__)
    Clone = _swig_new_instance_method(_itkFixedPointInverseDisplacementFieldImageFilterPython.itkFixedPointInverseDisplacementFieldImageFilterIVF22IVF22_Clone)
    SetNumberOfIterations = _swig_new_instance_method(_itkFixedPointInverseDisplacementFieldImageFilterPython.itkFixedPointInverseDisplacementFieldImageFilterIVF22IVF22_SetNumberOfIterations)
    GetNumberOfIterations = _swig_new_instance_method(_itkFixedPointInverseDisplacementFieldImageFilterPython.itkFixedPointInverseDisplacementFieldImageFilterIVF22IVF22_GetNumberOfIterations)
    SetSize = _swig_new_instance_method(_itkFixedPointInverseDisplacementFieldImageFilterPython.itkFixedPointInverseDisplacementFieldImageFilterIVF22IVF22_SetSize)
    GetSize = _swig_new_instance_method(_itkFixedPointInverseDisplacementFieldImageFilterPython.itkFixedPointInverseDisplacementFieldImageFilterIVF22IVF22_GetSize)
    SetOutputSpacing = _swig_new_instance_method(_itkFixedPointInverseDisplacementFieldImageFilterPython.itkFixedPointInverseDisplacementFieldImageFilterIVF22IVF22_SetOutputSpacing)
    GetOutputSpacing = _swig_new_instance_method(_itkFixedPointInverseDisplacementFieldImageFilterPython.itkFixedPointInverseDisplacementFieldImageFilterIVF22IVF22_GetOutputSpacing)
    SetOutputOrigin = _swig_new_instance_method(_itkFixedPointInverseDisplacementFieldImageFilterPython.itkFixedPointInverseDisplacementFieldImageFilterIVF22IVF22_SetOutputOrigin)
    OutputHasNumericTraitsCheck = _itkFixedPointInverseDisplacementFieldImageFilterPython.itkFixedPointInverseDisplacementFieldImageFilterIVF22IVF22_OutputHasNumericTraitsCheck
    
    SameDimensionCheck = _itkFixedPointInverseDisplacementFieldImageFilterPython.itkFixedPointInverseDisplacementFieldImageFilterIVF22IVF22_SameDimensionCheck
    
    __swig_destroy__ = _itkFixedPointInverseDisplacementFieldImageFilterPython.delete_itkFixedPointInverseDisplacementFieldImageFilterIVF22IVF22
    cast = _swig_new_static_method(_itkFixedPointInverseDisplacementFieldImageFilterPython.itkFixedPointInverseDisplacementFieldImageFilterIVF22IVF22_cast)

    def New(*args, **kargs):
        """New() -> itkFixedPointInverseDisplacementFieldImageFilterIVF22IVF22

        Create a new object of the class itkFixedPointInverseDisplacementFieldImageFilterIVF22IVF22 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkFixedPointInverseDisplacementFieldImageFilterIVF22IVF22.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkFixedPointInverseDisplacementFieldImageFilterIVF22IVF22.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkFixedPointInverseDisplacementFieldImageFilterIVF22IVF22.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkFixedPointInverseDisplacementFieldImageFilterIVF22IVF22 in _itkFixedPointInverseDisplacementFieldImageFilterPython:
_itkFixedPointInverseDisplacementFieldImageFilterPython.itkFixedPointInverseDisplacementFieldImageFilterIVF22IVF22_swigregister(itkFixedPointInverseDisplacementFieldImageFilterIVF22IVF22)
itkFixedPointInverseDisplacementFieldImageFilterIVF22IVF22___New_orig__ = _itkFixedPointInverseDisplacementFieldImageFilterPython.itkFixedPointInverseDisplacementFieldImageFilterIVF22IVF22___New_orig__
itkFixedPointInverseDisplacementFieldImageFilterIVF22IVF22_cast = _itkFixedPointInverseDisplacementFieldImageFilterPython.itkFixedPointInverseDisplacementFieldImageFilterIVF22IVF22_cast


def itkFixedPointInverseDisplacementFieldImageFilterIVF33IVF33_New():
    return itkFixedPointInverseDisplacementFieldImageFilterIVF33IVF33.New()

class itkFixedPointInverseDisplacementFieldImageFilterIVF33IVF33(itk.itkImageToImageFilterAPython.itkImageToImageFilterIVF33IVF33):
    r"""Proxy of C++ itkFixedPointInverseDisplacementFieldImageFilterIVF33IVF33 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkFixedPointInverseDisplacementFieldImageFilterPython.itkFixedPointInverseDisplacementFieldImageFilterIVF33IVF33___New_orig__)
    Clone = _swig_new_instance_method(_itkFixedPointInverseDisplacementFieldImageFilterPython.itkFixedPointInverseDisplacementFieldImageFilterIVF33IVF33_Clone)
    SetNumberOfIterations = _swig_new_instance_method(_itkFixedPointInverseDisplacementFieldImageFilterPython.itkFixedPointInverseDisplacementFieldImageFilterIVF33IVF33_SetNumberOfIterations)
    GetNumberOfIterations = _swig_new_instance_method(_itkFixedPointInverseDisplacementFieldImageFilterPython.itkFixedPointInverseDisplacementFieldImageFilterIVF33IVF33_GetNumberOfIterations)
    SetSize = _swig_new_instance_method(_itkFixedPointInverseDisplacementFieldImageFilterPython.itkFixedPointInverseDisplacementFieldImageFilterIVF33IVF33_SetSize)
    GetSize = _swig_new_instance_method(_itkFixedPointInverseDisplacementFieldImageFilterPython.itkFixedPointInverseDisplacementFieldImageFilterIVF33IVF33_GetSize)
    SetOutputSpacing = _swig_new_instance_method(_itkFixedPointInverseDisplacementFieldImageFilterPython.itkFixedPointInverseDisplacementFieldImageFilterIVF33IVF33_SetOutputSpacing)
    GetOutputSpacing = _swig_new_instance_method(_itkFixedPointInverseDisplacementFieldImageFilterPython.itkFixedPointInverseDisplacementFieldImageFilterIVF33IVF33_GetOutputSpacing)
    SetOutputOrigin = _swig_new_instance_method(_itkFixedPointInverseDisplacementFieldImageFilterPython.itkFixedPointInverseDisplacementFieldImageFilterIVF33IVF33_SetOutputOrigin)
    OutputHasNumericTraitsCheck = _itkFixedPointInverseDisplacementFieldImageFilterPython.itkFixedPointInverseDisplacementFieldImageFilterIVF33IVF33_OutputHasNumericTraitsCheck
    
    SameDimensionCheck = _itkFixedPointInverseDisplacementFieldImageFilterPython.itkFixedPointInverseDisplacementFieldImageFilterIVF33IVF33_SameDimensionCheck
    
    __swig_destroy__ = _itkFixedPointInverseDisplacementFieldImageFilterPython.delete_itkFixedPointInverseDisplacementFieldImageFilterIVF33IVF33
    cast = _swig_new_static_method(_itkFixedPointInverseDisplacementFieldImageFilterPython.itkFixedPointInverseDisplacementFieldImageFilterIVF33IVF33_cast)

    def New(*args, **kargs):
        """New() -> itkFixedPointInverseDisplacementFieldImageFilterIVF33IVF33

        Create a new object of the class itkFixedPointInverseDisplacementFieldImageFilterIVF33IVF33 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkFixedPointInverseDisplacementFieldImageFilterIVF33IVF33.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkFixedPointInverseDisplacementFieldImageFilterIVF33IVF33.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkFixedPointInverseDisplacementFieldImageFilterIVF33IVF33.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkFixedPointInverseDisplacementFieldImageFilterIVF33IVF33 in _itkFixedPointInverseDisplacementFieldImageFilterPython:
_itkFixedPointInverseDisplacementFieldImageFilterPython.itkFixedPointInverseDisplacementFieldImageFilterIVF33IVF33_swigregister(itkFixedPointInverseDisplacementFieldImageFilterIVF33IVF33)
itkFixedPointInverseDisplacementFieldImageFilterIVF33IVF33___New_orig__ = _itkFixedPointInverseDisplacementFieldImageFilterPython.itkFixedPointInverseDisplacementFieldImageFilterIVF33IVF33___New_orig__
itkFixedPointInverseDisplacementFieldImageFilterIVF33IVF33_cast = _itkFixedPointInverseDisplacementFieldImageFilterPython.itkFixedPointInverseDisplacementFieldImageFilterIVF33IVF33_cast


import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def fixed_point_inverse_displacement_field_image_filter(*args, **kwargs):
    """Procedural interface for FixedPointInverseDisplacementFieldImageFilter"""
    import itk
    instance = itk.FixedPointInverseDisplacementFieldImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def fixed_point_inverse_displacement_field_image_filter_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.FixedPointInverseDisplacementFieldImageFilter, itkTemplate.itkTemplate):
        filter_object = itk.FixedPointInverseDisplacementFieldImageFilter.values()[0]
    else:
        filter_object = itk.FixedPointInverseDisplacementFieldImageFilter

    fixed_point_inverse_displacement_field_image_filter.__doc__ = filter_object.__doc__
    fixed_point_inverse_displacement_field_image_filter.__doc__ += "\n Args are Input(s) to the filter.\n"
    fixed_point_inverse_displacement_field_image_filter.__doc__ += "\n Available Keyword Arguments:\n"
    if isinstance(itk.FixedPointInverseDisplacementFieldImageFilter, itkTemplate.itkTemplate):
        fixed_point_inverse_displacement_field_image_filter.__doc__ += itkHelpers.filter_args(filter_object)[0]
        fixed_point_inverse_displacement_field_image_filter.__doc__ += "\n"
        fixed_point_inverse_displacement_field_image_filter.__doc__ += itkHelpers.filter_args(filter_object)[1]
    else:
        fixed_point_inverse_displacement_field_image_filter.__doc__ += "".join([
            "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
            for item in dir(filter_object)
            if item.startswith("Set")])




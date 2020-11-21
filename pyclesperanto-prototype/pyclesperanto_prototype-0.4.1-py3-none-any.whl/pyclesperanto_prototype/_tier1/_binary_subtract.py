from .._tier0 import execute
from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function
def binary_subtract(minuend : Image, subtrahend : Image, destination : Image = None):
    """Subtracts one binary image from another.
    
    Parameters
    ----------
    minuend : Image
        The first binary input image to be processed.
    suubtrahend : Image
        The second binary input image to be subtracted from the first.
    destination : Image
        The output image where results are written into.
     
    
    Returns
    -------
    destination
    
    Examples
    --------
    >>> import pyclesperanto_prototype as cle
    >>> cle.binary_subtract(minuend, subtrahend, destination)
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_binarySubtract
    """


    parameters = {
        "dst": destination,
        "src1":minuend,
        "src2":subtrahend
    }

    # TODO: Rename cl file and kernel function to fit to naming conventions. This needs to be done in clij2 as well.
    execute(__file__, 'binarySubtract' + str(len(destination.shape)) + 'd_x.cl', 'binary_subtract_image' + str(len(destination.shape)) + 'd', destination.shape, parameters)
    return destination

from .._tier0 import execute
from .._tier0 import plugin_function
from .._tier0 import create_none
from .._tier0 import create
from .._tier0 import Image

@plugin_function(output_creator=create_none)
def transpose_yz(source : Image, destination : Image = None):
    """Transpose Y and Z axes of an image.
    
    Parameters
    ----------
    source : Image
        The input image.
    destination : Image
        The output image where results are written into.
     
    
    Returns
    -------
    destination
    
    Examples
    --------
    >>> import pyclesperanto_prototype as cle
    >>> cle.transpose_yz(source, destination)
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_transposeYZ
    """


    if destination is None:
        dimensions = source.shape
        if len(dimensions) == 3:
            destination = create([dimensions[1], dimensions[0], dimensions[2]])
        elif len(dimensions) == 2:
            destination = create([dimensions[0], 1, dimensions[1]])
        elif len(dimensions) == 1:
            destination = create([1, 1, dimensions[0]])


    parameters = {
        "src":source,
        "dst":destination
    }

    execute(__file__, 'transpose_yz_3d_x.cl', 'transpose_yz_3d', destination.shape, parameters)

    return destination

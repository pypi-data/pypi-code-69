from .._tier0 import create
from .._tier1 import minimum_box
from .._tier1 import maximum_box
from .._tier1 import add_images_weighted
from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function
def bottom_hat_box(input : Image, destination : Image = None, radius_x : float = 1, radius_y : float = 1, radius_z : float = 1):
    """Apply a bottom-hat filter for background subtraction to the input image.
    
    Parameters
    ----------
    input : Image
        The input image where the background is subtracted from.
    destination : Image
        The output image where results are written into.
    radius_x : Image
        Radius of the background determination region in X.
    radius_y : Image
        Radius of the background determination region in Y.
    radius_z : Image
        Radius of the background determination region in Z.
     
    
    Returns
    -------
    destination
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_bottomHatBox
    """


    temp1 = create(input.shape)
    temp2 = create(input.shape)

    maximum_box(input, temp1, radius_x, radius_y, radius_z)
    minimum_box(temp1, temp2, radius_x, radius_y, radius_z)
    add_images_weighted(temp2, input, destination, 1, -1)
    return destination
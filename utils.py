import random
import glob
from PIL import Image
import numpy as np

def list_files(path, extension='*'):
    """
    List files with in a directory with a given extension.

    Input:
        path: string with directory path
        extension: extension to search for (defaults to any extension)
    Output:
        list of file paths
    """
    path = path.rstrip('/')
    return glob.glob(path+'/*.'+extension)

def read_image(path):
    """
    Read image file and return it as a np.array.

    Input:
        path: string with image path
    Output:
        image as np.array, normalized
    """
    f = Image.open(path)
    return np.array(f)/255.

def crop_image(image, pos, size):
    """
    Crop an image.

    Input:
        image: image as a np.array
        pos: upper left corner of the patch (row, col)
        size: size of the patch (rows, cols)
    Output:
        cropped image as np.array
    """
    assert image.shape[0] >= pos[0]+size[0]
    assert image.shape[1] >= pos[1]+size[1]
    return image[pos[0]:pos[0]+size[0], pos[1]:pos[1]+size[1], :]


def n_random_crops(image, n, size):
    """
    Take n random crops from an image.

    Input:
        image: image as a np.array
        n: number of random crops to take
        size: size of the patches (rows, cols)
    Output:
        cropped patches as np.array with shape (n, rows, cols, channels)
    """
    assert size[0] <= image.shape[0]
    assert size[1] <= image.shape[1]
    crops = np.empty((n,*size, image.shape[-1]))
    for i in range(n):
        pos = (random.randint(0, image.shape[0]-size[0]+1), random.randint(0, image.shape[1]-size[1]+1))
        crop = crop_image(image, pos, size)
        crops[i,:,:,:] = crop
    return crops

def np_to_pil(array):
    """
    Convert np.array to PIL.Image

    Input:
        array: image as np.array
    Output:
        image as PIL.Image
    """
    return Image.fromarray((array * 255).astype(np.uint8))
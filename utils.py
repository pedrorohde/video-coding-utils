import random
import glob
from PIL import Image
import numpy as np

def list_files(path, extension='*'):
    path = path.rstrip('/')
    return glob.glob(path+'/*.'+extension)

def read_image(path):
    f = Image.open(path)
    return np.array(f)/255.

def crop_image(image, pos, size):
    assert image.shape[0] >= pos[0]+size[0]
    assert image.shape[1] >= pos[1]+size[1]
    return image[pos[0]:pos[0]+size[0], pos[1]:pos[1]+size[1], :]


def n_random_crops(image, n, size):
    assert size[0] <= image.shape[0]
    assert size[1] <= image.shape[1]
    crops = np.empty((n,*size, image.shape[-1]))
    for i in range(n):
        pos = (random.randint(0, image.shape[0]-size[0]+1), random.randint(0, image.shape[1]-size[1]+1))
        crop = crop_image(image, pos, size)
        crops[i,:,:,:] = crop
    return crops

def np_to_pil(array):
    return Image.fromarray((array * 255).astype(np.uint8))
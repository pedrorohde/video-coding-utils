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
    assert pos[0]+size[0] <= image.shape[0]
    assert pos[1]+size[1] <= image.shape[1]
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
    assert size[0] <= image.shape[0], "patch height should be <= image height"
    assert size[1] <= image.shape[1], "patch width should be <= image width"
    crops = np.empty((n, *size, image.shape[-1]))
    for i in range(n):
        pos = (random.randint(0, image.shape[0]-size[0]), random.randint(0, image.shape[1]-size[1]))
        crop = crop_image(image, pos, size)
        crops[i,:,:,:] = crop
    return crops


def random_crops_from_dir(path, n, size):
    """
    Take n random crops from each image of a directory.

    Input:
        path: string with directory path
        n: number of random crops to take
        size: size of the patches (rows, cols)
    Output:
        cropped patches as np.array with shape (n, rows, cols, channels)
    """
    filelist = list_files(path, 'png')
    data = np.empty((0, *size, 3))
    for f in filelist:
        img = read_image(f)
        data = np.concatenate((data, n_random_crops(img, n, size)),axis=0)
    return data


def read_YUV420(path, size, frame=0, channel='Y'):
    """
    Read binary YUV420 raw video file and return one frame.

    Input:
        path: string with file path
        size: size of each frame (Y)
        frame: which frame to take
        channel: which channel to take
    Output:
        frame as np.array, normalized
    """
    pos = frame*size[0]*size[1]*6//4
    if channel in ['U', 'u', 'Cb', 'cb']:
        pos += size[0]*size[1]
        size = (size[0]//2, size[1]//2)
    elif channel in ['V', 'v', 'Cr', 'cr']:
        pos += size[0]*size[1]*5//4
        size = (size[0]//2, size[1]//2)
    
    with open(filepath, 'rb') as f:
        f.seek(pos, 0)
        img = Image.frombytes('L', [size[1], size[0]], f.read(size[1]*size[0]))
    
    return np.asarray(img)/255.


def read_YUV420_multiframes(filepath, size, frames, channel='Y'):
    """
    Read binary YUV420 raw video file and return multiple frames.

    Input:
        path: string with file path
        size: size of each frame (Y)
        frame: list of frames to take
        channel: which channel to take
    Output:
        frames as np.array with shape (n, rows, cols), normalized
    """
    pos = [frame*size[0]*size[1]*6//4 for frame in frames]
    if channel in ['U', 'u', 'Cb', 'cb']:
        pos = [p + size[0]*size[1] for p in pos]
        size = (size[0]//2, size[1]//2)
    elif channel in ['V', 'v', 'Cr', 'cr']:
        pos = [p + size[0]*size[1]*5//4 for p in pos]
        size = (size[0]//2, size[1]//2)
    
    data = np.empty((len(frames), *size))
    
    with open(filepath, 'rb') as f:
        for i in range(len(pos)):
            p = pos[i]
            f.seek(p, 0)
            img = Image.frombytes('L', [size[1], size[0]], f.read(size[1]*size[0]))
            data[i,:,:] = np.asarray(img)/255.
             
    return data


def np_to_pil(array):
    """
    Convert np.array to PIL.Image

    Input:
        array: image as np.array
    Output:
        image as PIL.Image
    """
    return Image.fromarray((array * 255).astype(np.uint8))
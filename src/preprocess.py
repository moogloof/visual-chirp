import numpy as np
from PIL import Image
import os
import glob
import pickle


IMAGE_DIRPATH = os.path.join("170", "consolidated")
TOTAL_DIRPATH = os.path.join(IMAGE_DIRPATH, "**")


def load_all_paths(dirpath, extension="*", dirsonly=False):
    if not dirsonly:
        paths = glob.glob(os.path.join(dirpath, "*.{}".format(extension)), recursive=True)
    else:
        paths = glob.glob(os.path.join(dirpath, "**"))

    return paths


def unload_image_data(paths):
    data = []

    for path in paths:
        with Image.open(path) as im:
            data.append(list(im.getdata()))

    return np.array(data)


full_data = {}
cat_paths = load_all_paths(IMAGE_DIRPATH, dirsonly=True)

for p in cat_paths:
    name = os.path.basename(p)

    full_data[name] = load_all_paths(p, "jpg") + load_all_paths(p, "png")
    full_data[name] = unload_image_data(full_data[name])

with open("outdata", "wb") as f:
    pickle.dump(full_data, f)

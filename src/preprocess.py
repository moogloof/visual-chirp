import numpy as np
from PIL import Image
import os
import glob
import pickle
import sys


# Declare paths
IMAGE_DIRPATH = os.path.join("170", "consolidated")
TOTAL_DIRPATH = os.path.join(IMAGE_DIRPATH, "**")


# Load all paths with given pattern
def load_all_paths(dirpath, extension="*", dirsonly=False):
    if not dirsonly:
        # Load all paths for files with given extension
        paths = glob.glob(os.path.join(dirpath, "*.{}".format(extension)), recursive=True)
    else:
        # Load all paths for directories
        paths = glob.glob(os.path.join(dirpath, "**"))

    return paths

# Load image data with given paths
def unload_image_data(paths):
    data = []
    dirname = os.path.basename(os.path.dirname(paths[0]))

    for i, path in enumerate(paths):
        # Print status bar
        s = int(i / (len(paths) / 25))
        sys.stdout.write("\r")
        sys.stdout.write("Loading {} data... [{}>{}] ({}/{})".format(dirname, "="*s, " "*(24-s), i+1, len(paths)))
        sys.stdout.flush()

        # Open and append image data
        with Image.open(path) as im:
            data.append(list(im.getdata()))

    sys.stdout.write("\n")

    return np.array(data)


# Declare full_data and all categorical directory paths
full_data = {}
cat_paths = load_all_paths(IMAGE_DIRPATH, dirsonly=True)

# Load and sort image data into respective categories
for p in cat_paths:
    name = os.path.basename(p)

    full_data[name] = load_all_paths(p, "jpg") + load_all_paths(p, "png")
    full_data[name] = unload_image_data(full_data[name])

# Dump loaded image data into outdata file
with open("outdata", "wb") as f:
    pickle.dump(full_data, f)

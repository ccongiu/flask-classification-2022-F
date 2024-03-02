"""
This is a simple collection of utilities employed by the service of the classification from images uploaded from the
user. These allow some functionalities for managing files.
"""
import os
from PIL import Image
from config import Configuration

conf = Configuration()


def fetch_image(image_id):
    """Gets the image from the specified ID. It returns only images
    downloaded in the folder specified in the configuration object."""
    image_path = os.path.join(conf.image_folder_path, image_id)
    img = Image.open(image_path)
    return img

def get_image_path(image_id):
    """Returns the full path of the image from its ID"""
    return os.path.join(conf.image_folder_path, image_id)

def new_file_name(name):
    """Returns a filename. It will be a name concatenated with a
    number representing a counter in order to search for the first
    available name (i.e., a name not belonging to any file in the
    images folder), for avoiding caching issues.
    """
    aux_name = name
    count = 0

    ## If a file with this name already exists, then increases the counter and checks again"
    while os.path.exists(os.path.join(conf.image_folder_path, aux_name+".jpg")):
        aux_name = name+str(count)
        count += 1

    ## Another possible solution for avoiding storing all these files could be the modification of the Cache-Control header
    return aux_name+".jpg"
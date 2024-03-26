"""
This is a simple histogram service. It accepts an url of an
image and returns the histogram.
"""
import os
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE" # Solves error related to libiomp5md dll initialization ('already initialized')
import time
from PIL import Image, ImageOps # For dealing with images (ImageOps for greyscale conversion)
import matplotlib
matplotlib.use('agg') # Use of non-interactive backend for solving the failing when using matplotlib outside the main thread
import matplotlib.pyplot as plt # Used for the histogram plot creation
from config import Configuration

conf = Configuration()


def fetch_image(image_id):
    """Gets the image from the specified ID. It returns only images
    downloaded in the folder specified in the configuration object."""
    image_path = os.path.join(conf.image_folder_path, image_id)
    img = Image.open(image_path)
    return img

def histogram_image_name(image_id):
    """Returns the name of the image file of the histogram related
    to the input image. It uses .jpg as extension for avoinding
    the insertion of the histogram file in the list of images.
    """
    aux_name = image_id.split(".")   # Separates the name of the file from its extension
    return aux_name[0]+"_hist.jpg"   # Concatenates _hist.jpg to the file name


def image_histogram(img_id):
    """Generates a file of the histogram obtained from the image
    corresponding to img_id and returns the name of such a file.
    It generates an image of the histogram from the greyscale
    version of the image.
    """
    img = fetch_image(img_id)         # Gets and opens the name of the file selected by the user
    img_gr = ImageOps.grayscale(img)  # Converts the image from RGB to Grayscale
    hist = img_gr.histogram()         # Generates the list corresponding to the histogram

    x = [n for n in range(256)]       # Generates a list of values from 0 to 255 (x-values of the following plot)
    fig = plt.figure()                # Creates a figure
    ax = plt.subplot(111)             # Adds axes to the figure
    ax.bar(x, hist)                   # Generates the histogram plot using x as x-values and hist as y-values
    ax.set_xlabel('Intensity')        # Sets the name of the x-axis
    ax.set_ylabel('Number of values') # Sets the name of the y-axis

    name = histogram_image_name(img_id)                            # Generates the filename of the histogram
    if os.path.exists(os.path.join(conf.image_folder_path, name)): # If a file with the same name exists...
        os.remove(os.path.join(conf.image_folder_path, name))      # ...then it is deleted

    fig.savefig(os.path.join(conf.image_folder_path, name)) # Saves the image of the histogram
    img.close()                                             # Closes the original image
    img_gr.close()                                          # Closes the greyscale version of the original image
    time.sleep(10)                                          # Delay (gives the time for the saving operation)
    return name                                             # Returns the name of the file containing the histogram

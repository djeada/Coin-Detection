'''
Implements drawing images from numpy arrays.
'''
import numpy as np
from matplotlib import pyplot as plt


def plot_image_matrix(img: np.ndarray, title: str = None) -> None:
    """
    Plots an image matrix.

    param img: the image matrix
    param title: the title of the plot
    """
    # create a figure
    fig = plt.figure(figsize=(10, 10))
    # add a title
    if title is not None:
        fig.suptitle(title, fontsize=16)
    # plot the image
    plt.imshow(img[:, :, ::-1])
    plt.show()

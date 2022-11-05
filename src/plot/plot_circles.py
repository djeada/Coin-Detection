import numpy as np
from matplotlib import pyplot as plt


def plot_circles(img: np.ndarray, circles: np.ndarray, title: str = None) -> None:
    """
    Plots the circles found in the image.

    param img: the image matrix
    param circles: the circles found in the image
    param title: the title of the plot
    """
    # create a figure
    fig = plt.figure(figsize=(10, 10))
    # add a title
    if title is not None:
        fig.suptitle(title, fontsize=16)
    # plot the image
    plt.imshow(img[:, :, ::-1])
    # draw the accepted circles
    for circle in circles:
        x, y, r = circle
        plt.gca().add_patch(plt.Circle((x, y), r, color="g", linewidth=3, fill=False))
    plt.show()

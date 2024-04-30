"""
Module for visualizing circles detected in images using matplotlib.
"""

import numpy as np
from matplotlib import pyplot as plt

def plot_circles(img: np.ndarray, circles: np.ndarray, title: str = "Detected Circles") -> None:
    """
    Displays an image and overlays circles detected in the image.

    Parameters:
    img (np.ndarray): The image array in which circles were detected.
    circles (np.ndarray): Array of circles, where each circle is represented by (x, y, r).
                          'x' and 'y' are the coordinates of the center, and 'r' is the radius.
    title (str, optional): Title of the plot. Defaults to "Detected Circles".

    This function uses matplotlib to plot the image and the circles.
    """
    # Initialize the plot with specified figure size
    fig, ax = plt.subplots(figsize=(10, 10))

    # Set the title of the plot
    ax.set_title(title, fontsize=16)

    # Display the image
    ax.imshow(img[:, :, ::-1])  # Convert BGR to RGB

    # Overlay each circle on the image
    for x, y, r in circles:
        circle = plt.Circle((x, y), r, color='red', fill=False, linewidth=2, linestyle='dashed')
        ax.add_patch(circle)

    # Hide axis labels
    ax.axis('off')

    # Show the plot
    plt.show()

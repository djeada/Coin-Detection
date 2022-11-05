"""
Implements reading and writing images.
"""
from pathlib import Path

import cv2
import numpy as np


def read_image(path: Path) -> np.ndarray:
    """
    Reads an image from a path.

    param path: the path to the image
    return: the image matrix
    """
    return cv2.imread(str(path))


def save_image(img: np.ndarray, path: Path) -> None:
    """
    Saves an image to a path.

    param img: the image matrix
    param path: the path to the image
    """
    cv2.imwrite(str(path), img)

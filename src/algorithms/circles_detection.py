"""
Implements the circle detection algorithm.
"""
import cv2
import numpy as np


def find_circles(img: np.ndarray, r_min: int, r_max: int) -> np.ndarray:
    """
    Finds every circle in the image with radius between r_min and r_max.
    Returns a list of circles, where each circle is represented as a tuple
    (x, y, r) where (x, y) is the center of the circle and r is the radius.

    param img: the image to search
    param r_min: the minimum radius of the circle
    param r_max: the maximum radius of the circle
    return: a list of circles
    """

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # convert to grayscale
    gray = cv2.GaussianBlur(gray, (9, 9), 3)  # blur the image

    circles = cv2.HoughCircles(
        gray, cv2.HOUGH_GRADIENT, 2, r_min, minRadius=r_min, maxRadius=r_max
    )  # find circles
    circles = np.around(circles)[0, :].astype(int)  # round the circles to integers

    return circles

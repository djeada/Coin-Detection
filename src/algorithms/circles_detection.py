"""
Implements the circle detection algorithm using OpenCV.
"""
import cv2
import numpy as np

def find_circles(img: np.ndarray, r_min: int, r_max: int) -> np.ndarray:
    """
    Detects circles in an image using the HoughCircles method from OpenCV. 
    Circles are detected within a specified radius range.

    Parameters:
    img (np.ndarray): The image in which to detect circles.
    r_min (int): The minimum radius of the circles to detect.
    r_max (int): The maximum radius of the circles to detect.

    Returns:
    np.ndarray: An array of detected circles, each represented by (x, y, r),
                where (x, y) is the center and r is the radius.
    """
    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Apply Gaussian blur to reduce noise and improve detection accuracy
    gray = cv2.GaussianBlur(gray, (9, 9), sigmaX=2, sigmaY=2)

    # Detect circles using the Hough Transform
    circles = cv2.HoughCircles(
        gray, 
        cv2.HOUGH_GRADIENT, 
        dp=1.5, 
        minDist=20, 
        param1=50, 
        param2=30, 
        minRadius=r_min, 
        maxRadius=r_max
    )

    # If no circles are detected, return an empty array
    if circles is None:
        return np.array([])

    # Round circle dimensions and convert to integers
    return np.around(circles)[0, :].astype(int)

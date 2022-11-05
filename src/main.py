"""
Main module. 
Run this file to start the program.
"""
import sys
sys.path.append('../src/')

from src.algorithms.circles_detection import find_circles
from src.configs.general_config import GeneralConfigFactory
from src.io.argument_parser import CoinDetectionParser
from src.io.circles import circles_to_csv
from src.io.image import read_image, save_image
from src.plot.plot_circles import plot_circles
from src.plot.plot_image_matrix import plot_image_matrix


def main() -> None:
    """
    Main function.
    """
    parser = CoinDetectionParser()
    config = GeneralConfigFactory.create_from_parser(parser)
    config.validate()

    # read the image
    img = read_image(config.path)
    # plot the image
    plot_image_matrix(img, "Original image")

    # find the circles
    print("Finding circles...")
    circles = find_circles(img, config.r_min, config.r_max)
    print(f"Found {len(circles)} circles.")

    if config.verbose:
        for i, circle in enumerate(circles):
            print(f"Circle {i}: x={circle[0]}, y={circle[1]}, r={circle[2]}")

    if config.csv_output:
        circles_to_csv(circles, config.output_dir / "coin_coordinates.csv")

    # plot the circles
    plot_circles(img, circles, "Coins found in the image")

    for i, circle in enumerate(circles):
        x, y, r = circle
        if config.verbose:
            title = f"Coin {i}"
            plot_image_matrix(img[y - r : y + r, x - r : x + r], title)
        if config.image_output:
            # save the image
            image = img[y - r : y + r, x - r : x + r]
            title = config.output_dir / f"circle_{x}_{y}_{r}.png"
            save_image(image, title)


main()

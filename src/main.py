"""
Main module.
Run this file to start the program.
"""
from pathlib import Path
import logging

from src.algorithms.circles_detection import find_circles
from src.configs.general_config import GeneralConfigFactory
from src.io.argument_parser import CoinDetectionParser
from src.io.circles import circles_to_csv
from src.io.image import read_image, save_image
from src.plot.plot_circles import plot_circles
from src.plot.plot_image_matrix import plot_image_matrix

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main() -> None:
    """
    Main function that orchestrates the detection and plotting of circles in images.
    """
    parser = CoinDetectionParser()
    config = GeneralConfigFactory.create_from_parser(parser)
    config.validate()

    # Read and plot the original image
    img = read_image(config.path)
    plot_image_matrix(img, "Original Image")

    # Detect circles
    logger.info("Finding circles...")
    circles = find_circles(img, config.r_min, config.r_max)
    logger.info(f"Found {len(circles)} circles.")

    if config.verbose:
        for i, (x, y, r) in enumerate(circles):
            logger.info(f"Circle {i}: x={x}, y={y}, r={r}")

    # Export circles to CSV if required
    if config.csv_output:
        csv_path = Path(config.output_dir, "coin_coordinates.csv")
        circles_to_csv(circles, csv_path)

    # Plot circles on the image
    plot_circles(img, circles, "Coins Found in the Image")

    # Process and optionally save sub-images containing each detected circle
    for i, (x, y, r) in enumerate(circles):
        cropped_img = img[y - r:y + r, x - r:x + r]
        if config.verbose:
            plot_image_matrix(cropped_img, f"Coin {i}")
        if config.image_output:
            save_path = Path(config.output_dir, f"circle_{x}_{y}_{r}.png")
            save_image(cropped_img, save_path)

if __name__ == "__main__":
    main()

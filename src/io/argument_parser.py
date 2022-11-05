"""
Defines the parser for the command line arguments.
"""
from argparse import ArgumentParser
from pathlib import Path

from src.configs.general_config import GeneralConfig


class CoinDetectionParser(ArgumentParser):
    """
    Parses command line arguments.
    """

    def __init__(self):
        super().__init__()
        self.add_argument("--path", type=str, default=Path("../resources/coin.png"), help="Path to the image")
        self.add_argument("--output_dir", type=str, default=Path("../output"), help="Path to the output directory")
        self.add_argument("--r_min", type=int, default=30, help="Minimum radius of the coins")
        self.add_argument("--r_max", type=int, default=80, help="Maximum radius of the coins")
        self.add_argument("--interactive", type=bool, default=GeneralConfig.interactive, help="Interactive mode")
        self.add_argument("--verbose", type=bool, default=GeneralConfig.verbose, help="Verbose mode")
        self.add_argument(
            "--image_output", type=bool, default=GeneralConfig.image_output, help="Should the images be displayed")
        self.add_argument("--csv_output", type=bool, default=GeneralConfig.csv_output, help="Should the csv with coin coordinates be saved") 

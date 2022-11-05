'''
Defines the parser for the command line arguments.
'''
from argparse import ArgumentParser
from pathlib import Path

from src.configs.general_config import GeneralConfig


class CoinDetectionParser(ArgumentParser):
    """
    Parses command line arguments.
    """
    def __init__(self):
        super().__init__()
        self.add_argument("--path", type=str, default=Path("../resources/coin.png"))
        self.add_argument("--output_dir", type=str, default=Path("../output"))
        self.add_argument("--r_min", type=int, default=30)
        self.add_argument("--r_max", type=int, default=80)
        self.add_argument("--interactive", type=bool, default=GeneralConfig.interactive)
        self.add_argument("--verbose", type=bool, default=GeneralConfig.verbose)
        self.add_argument(
            "--image_output", type=bool, default=GeneralConfig.image_output
        )
        self.add_argument("--csv_output", type=bool, default=GeneralConfig.csv_output)

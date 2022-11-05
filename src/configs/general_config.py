"""
Defines the general configuration class that 
stores the configuration parameters for the program.
"""
import argparse
from dataclasses import dataclass
from pathlib import Path


@dataclass
class GeneralConfig:
    """
    Stores the configuration parameters for the program.
    """
    path: Path
    output_dir: Path
    r_min: int
    r_max: int
    interactive: bool = True
    verbose: bool = True
    image_output: bool = True
    csv_output: bool = True

    def validate(self) -> None:
        """
        Validates the configuration parameters.

        Raises:
            ValueError: if the configuration parameters are invalid.
        """
        if not self.path.exists():
            raise ValueError(f"Path {self.path} does not exist")
        if not self.output_dir.exists():
            try:
                self.output_dir.mkdir(parents=True, exist_ok=True)
            except OSError:
                raise ValueError(f"Could not create output directory {self.output_dir}")
        if self.r_min < 0:
            raise ValueError(f"r_min must be greater than 0, but is {self.r_min}")
        if self.r_max < 0:
            raise ValueError(f"r_max must be greater than 0, but is {self.r_max}")
        if self.r_min > self.r_max:
            raise ValueError(f"r_min must be smaller than r_max, but is {self.r_min} and {self.r_max} respectively")


class GeneralConfigFactory:
    """
    Factory class for creating a GeneralConfig object from a parser.
    """

    @staticmethod
    def create_from_parser(parser: argparse.ArgumentParser) -> GeneralConfig:
        """
        Creates a GeneralConfig object from a parser.

        param parser: the parser to use.
        return: a GeneralConfig object.
        """
        args = parser.parse_args()
        return GeneralConfig(
            path=args.path,
            output_dir=args.output_dir,
            r_min=args.r_min,
            r_max=args.r_max,
            interactive=args.interactive,
            verbose=args.verbose,
            image_output=args.image_output,
            csv_output=args.csv_output,
        )

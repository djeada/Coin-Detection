"""
Defines the GeneralConfig class that stores configuration parameters for the program.
"""
import argparse
from dataclasses import dataclass
from pathlib import Path

@dataclass
class GeneralConfig:
    """
    Data class that stores the configuration parameters for the program.
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
        Validates the configuration parameters to ensure they meet expected conditions.

        Raises:
            ValueError: If any configuration parameter is invalid.
        """
        if not self.path.is_file():
            raise ValueError(f"The specified image path does not exist: {self.path}")
        if not self.output_dir.exists():
            self.output_dir.mkdir(parents=True, exist_ok=True)
        if not (0 < self.r_min <= self.r_max):
            raise ValueError(f"Invalid radius range: r_min ({self.r_min}) must be positive and less than or equal to r_max ({self.r_max}).")

class GeneralConfigFactory:
    """
    Factory class for creating a GeneralConfig object from command line arguments.
    """
    @staticmethod
    def create_from_parser(parser: argparse.ArgumentParser) -> GeneralConfig:
        """
        Parses command line arguments to create a GeneralConfig object.

        Parameters:
            parser (argparse.ArgumentParser): The argument parser instance.

        Returns:
            GeneralConfig: The configuration object initialized with parsed arguments.
        """
        args = parser.parse_args()
        return GeneralConfig(
            path=Path(args.path),
            output_dir=Path(args.output_dir),
            r_min=args.r_min,
            r_max=args.r_max,
            interactive=args.interactive,
            verbose=args.verbose,
            image_output=args.image_output,
            csv_output=args.csv_output,
        )

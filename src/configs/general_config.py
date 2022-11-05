import argparse
from dataclasses import dataclass
from pathlib import Path


@dataclass
class GeneralConfig:
    path: Path
    output_dir: Path
    r_min: int
    r_max: int
    interactive: bool = True
    verbose: bool = True
    image_output: bool = True
    csv_output: bool = True


class GeneralConfigFactory:
    @staticmethod
    def create_from_parser(parser: argparse.ArgumentParser) -> GeneralConfig:
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

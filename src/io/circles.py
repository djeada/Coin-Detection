from pathlib import Path

import numpy as np
import pandas as pd


def circles_to_csv(circles: np.ndarray, path: Path) -> None:
    """
    Saves the circles to a csv file.

    param circles: the circles found in the image
    param path: the name of the csv file
    """
    df = pd.DataFrame(circles, columns=["x", "y", "r"])
    df.to_csv(path, index=False)

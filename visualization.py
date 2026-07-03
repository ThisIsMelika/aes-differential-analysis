"""
visualization.py

Generate a heatmap of the AES Difference Distribution Table.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


OUTPUT_DIR = Path("output")
OUTPUT_DIR.mkdir(exist_ok=True)


def generate_heatmap(table):

    matrix = np.array(table)

    plt.figure(figsize=(10, 8))

    plt.imshow(matrix, interpolation="nearest")

    plt.title("AES Difference Distribution Table")

    plt.xlabel("Output Difference")

    plt.ylabel("Input Difference")

    plt.colorbar()

    plt.tight_layout()

    plt.savefig(OUTPUT_DIR / "heatmap.png", dpi=300)

    plt.show()

    print("[✓] Heatmap saved.")
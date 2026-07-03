"""
exporter.py

Export DDT tables to CSV files.

Author: Melika Bagherii
"""

import csv
from pathlib import Path


OUTPUT_DIR = Path("output")
OUTPUT_DIR.mkdir(exist_ok=True)


def export_ddt(table, filename="ddt.csv"):

    filepath = OUTPUT_DIR / filename

    with open(filepath, "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow(["Δx\\Δy"] + list(range(256)))

        for dx in range(256):
            writer.writerow([dx] + table[dx])

    print(f"[✓] DDT exported to {filepath}")


def export_probability(table, filename="probability.csv"):

    filepath = OUTPUT_DIR / filename

    with open(filepath, "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow(["Δx\\Δy"] + list(range(256)))

        for dx in range(256):

            row = [value / 256 for value in table[dx]]

            writer.writerow([dx] + row)

    print(f"[✓] Probability table exported to {filepath}")
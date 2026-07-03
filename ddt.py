"""
ddt.py

Generate the Difference Distribution Table (DDT)
for the AES S-box.

Author: Melika Bagherii
"""

from typing import List, Tuple
from aes_sbox import sbox


class DifferenceDistributionTable:
    """
    Generates the AES Difference Distribution Table.

    DDT[a][b] represents the number of x values satisfying:

        S(x) XOR S(x XOR a) = b
    """

    def __init__(self) -> None:
        self.size = 256
        self.table: List[List[int]] = [
            [0] * self.size for _ in range(self.size)
        ]

    def generate(self) -> None:
        """
        Generate the 256x256 Difference Distribution Table.
        """

        for input_difference in range(self.size):

            if input_difference % 16 == 0:
                print(f"Processing input difference {input_difference}/255")

            for x in range(self.size):

                y = x ^ input_difference

                output_difference = sbox(x) ^ sbox(y)

                self.table[input_difference][output_difference] += 1

    def probability(self, dx: int, dy: int) -> float:
        """
        Returns the differential probability.

        P = Count / 256
        """

        return self.table[dx][dy] / 256

    def get_max_value(self) -> Tuple[int, int, int]:
        """
        Find maximum DDT value (excluding Δx = 0).

        Returns
        -------
        (dx, dy, value)
        """

        maximum = -1
        best_dx = 0
        best_dy = 0

        for dx in range(1, self.size):

            for dy in range(self.size):

                value = self.table[dx][dy]

                if value > maximum:

                    maximum = value
                    best_dx = dx
                    best_dy = dy

        return best_dx, best_dy, maximum

    def print_summary(self) -> None:
        """
        Print summary statistics.
        """

        dx, dy, maximum = self.get_max_value()

        print("\n==============================")
        print("AES Differential Analysis")
        print("==============================\n")

        print(f"Best Input Difference  : {dx}")
        print(f"Best Output Difference : {dy}")
        print(f"Maximum Count          : {maximum}")
        print(f"Maximum Probability    : {maximum}/256")

        print(f"Decimal Probability    : {maximum/256:.6f}")

    def print_row(self, dx: int) -> None:
        """
        Print one DDT row.
        """

        print(f"\nInput Difference = {dx}\n")

        for dy in range(self.size):

            print(
                f"{dy:3d} : {self.table[dx][dy]}"
            )

    def export_probability_table(self) -> List[List[float]]:
        """
        Return probability table.
        """

        probabilities = []

        for dx in range(self.size):

            row = []

            for dy in range(self.size):

                row.append(self.table[dx][dy] / 256)

            probabilities.append(row)

        return probabilities
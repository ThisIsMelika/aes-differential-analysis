import argparse

from ddt import DifferenceDistributionTable
from exporter import export_ddt
from exporter import export_probability
from visualization import generate_heatmap
from utils import Timer


def main():

    parser = argparse.ArgumentParser(
        description="AES Differential Cryptanalysis Toolkit"
    )

    parser.add_argument(
        "--export",
        action="store_true",
        help="Export CSV files",
    )

    parser.add_argument(
        "--heatmap",
        action="store_true",
        help="Generate heatmap",
    )

    parser.add_argument(
        "--dx",
        type=int,
        help="Display one DDT row",
    )

    args = parser.parse_args()

    with Timer():

        ddt = DifferenceDistributionTable()

        ddt.generate()

        ddt.print_summary()

        if args.dx is not None:
            ddt.print_row(args.dx)

        if args.export:
            export_ddt(ddt.table)
            export_probability(ddt.table)

        if args.heatmap:
            generate_heatmap(ddt.table)


if __name__ == "__main__":
    main()
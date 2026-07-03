# AES Differential Distribution Table (DDT)

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Cryptography](https://img.shields.io/badge/Cryptography-AES-red.svg)

## Overview

This project implements the **Differential Distribution Table (DDT)** of the AES S-box.

The toolkit computes the differential probabilities used in differential cryptanalysis and exports the results as CSV files. It also generates a heatmap for visualization.

The implementation follows the AES standard described in:

> Paar, Pelzl — *Understanding Cryptography* (2nd Edition)

---

## Features

- AES S-box implementation
- Difference Distribution Table (256 × 256)
- Differential probability computation
- CSV export
- Heatmap visualization
- Unit tests
- Command-line interface
- Clean project structure

---

## Project Structure

```
aes-differential-analysis/
├── aes_sbox.py
├── ddt.py
├── exporter.py
├── visualization.py
├── utils.py
├── main.py
│
├── tests/
├── output/
│
├── README.md
├── LICENSE
└── requirements.txt
```

---

## Installation

```bash
git clone https://github.com/meliiwx/aes-differential-analysis.git
cd aes-differential-analysis
pip install -r requirements.txt
```

---

## Usage

Run the full analysis:

```bash
python main.py
```

Generate CSV output:

```bash
python main.py --export
```

Generate heatmap:

```bash
python main.py --heatmap
```

Display a single DDT row:

```bash
python main.py --dx 37
```

---

## Example Output

```
AES Differential Analysis
Maximum Count        : 4
Maximum Probability  : 4 / 256
Decimal Probability  : 0.015625
```

---

## Mathematics

For every input difference `Δx`, the toolkit computes:

```
S(x) ⊕ S(x ⊕ Δx)   for all x ∈ {0, ..., 255}
```

and stores the frequency of every resulting output difference `Δy`.

The differential probability is then given by:

```
P(Δx → Δy) = DDT[Δx][Δy] / 256
```

---

## References

- Paar, Pelzl — *Understanding Cryptography* (2nd Edition)
- FIPS-197 — Advanced Encryption Standard (AES)

---

## Author

**Melika Bagheri**


GitHub: [github.com/meliiwx](https://github.com/meliiwx)

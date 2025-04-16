# PDF Cutter/Merger Tool Overview

## Purpose
The PDF Cutter/Merger Tool is an interactive Python-based application designed to:
1. **Select specific pages** from multiple PDF files based on user input.
2. **Merge** the selected pages into a single output PDF file.

## Features
- **Interactive User Interface:** The tool prompts users to input file paths, page ranges, and output file paths.
- **Error Handling:** Handles invalid inputs, such as non-existent files or incorrect page ranges.
- **Flexible Page Selection:** Allows page selection in various formats (e.g., `1,3-5,10-12`).

## Tools and Libraries
- [PyPDF2](https://pypi.org/project/PyPDF2/): A Python library for PDF processing.

## How It Works
1. The tool asks the user for the number of PDF files to process.
2. Prompts the user to input each file's path and validates its existence.
3. Displays the number of pages in each PDF and requests page ranges for selection.
4. Merges the specified pages into a single output PDF file.

## Requirements
- Python 3.6+
- PyPDF2 library
```bash
pip install PyPDF2
```
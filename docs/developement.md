# Development Guide

## Code Structure
### `main.py`
- **Functions:**
  - `parse_page_ranges(range_str)`: Parses a page range string into a list of tuples.
  - `main()`: The main entry point for the tool. Handles user input, validation, and PDF processing.

## Coding Standards
- Use Python 3.6+.
- Follow PEP 8 guidelines for code style.

## Adding Features
### Example: Adding Support for Reverse Page Order
1. Modify the `parse_page_ranges` function to handle reverse ranges (e.g., `10-1`).
2. Update the page processing logic in the `main` function to iterate in reverse order.

## Debugging
- Use `print` statements to log intermediate values.
- Test with various input edge cases:
  - Non-existent file paths.
  - Invalid page ranges (e.g., `5-1` without reverse support).
  - Large PDF files.

## Testing
### Manual Testing
Run the tool with different scenarios:
- Single PDF file with valid and invalid page ranges.
- Multiple PDF files with overlapping or disjoint ranges.
- Output file path validation.

### Automated Testing
Consider writing unit tests for:
- `parse_page_ranges` function with various inputs.
- Mocking file inputs for the `main` function.
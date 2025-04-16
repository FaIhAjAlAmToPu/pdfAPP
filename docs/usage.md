# Usage Instructions

## Running the Tool
To start the PDF Cutter/Merger Tool, run the following command:
```bash
python main.py
```

## Example Walkthrough
### Step 1: Start the Tool
Run the script:
```bash
python main.py
```

### Step 2: Input the Number of PDF Files
```
How many PDF files do you want to process? 2
```

### Step 3: Enter File Paths
Enter the path to each PDF file you want to process:
```
Enter path for PDF #1: example1.pdf
PDF has 10 pages
```

### Step 4: Specify Page Ranges
Input the page ranges you want to select:
```
Enter pages to select (e.g., '1-10,4-30' or '1,3-5'): 1-3,5
```

Repeat this for all files.

### Step 5: Specify Output File Path
Provide the path for the output merged PDF:
```
Enter output file path (e.g., merged.pdf): merged_output.pdf
```

### Step 6: Completion
The tool confirms successful creation of the merged PDF:
```
Successfully created merged PDF at: merged_output.pdf
```

## Error Handling
- **File Not Found:** If a file path is invalid, you'll be prompted to re-enter it.
- **Invalid Page Range:** If a page range exceeds the total number of pages, an error message will be displayed, and you'll need to re-enter the range.
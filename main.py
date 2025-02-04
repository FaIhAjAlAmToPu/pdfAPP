import PyPDF2

def parse_page_ranges(range_str):
    """Parse page range string into list of (start, end) tuples"""
    ranges = []
    parts = range_str.replace(' ', '').split(',')
    for part in parts:
        if '-' in part:
            start, end = part.split('-')
        else:
            start = end = part
        ranges.append((int(start), int(end)))
    return ranges

def main():
    print("PDF Cutter/Merger Tool")
    print("======================\n")
    
    merger = PyPDF2.PdfWriter()
    
    num_files = int(input("How many PDF files do you want to process? "))
    
    for i in range(num_files):
        while True:
            file_path = input(f"\nEnter path for PDF #{i+1}: ").strip()
            try:
                reader = PyPDF2.PdfReader(file_path)
                break
            except FileNotFoundError:
                print("File not found. Please try again.")
            except Exception as e:
                print(f"Error opening PDF: {e}")
                return

        num_pages = len(reader.pages)
        print(f"PDF has {num_pages} pages")
        
        while True:
            range_str = input("Enter pages to select (e.g., '1-10,4-30' or '1,3-5'): ")
            try:
                page_ranges = parse_page_ranges(range_str)
                valid = True
                for start, end in page_ranges:
                    if start < 1 or end > num_pages or start > end:
                        print(f"Invalid range {start}-{end} for PDF with {num_pages} pages")
                        valid = False
                        break
                if valid:
                    break
            except ValueError:
                print("Invalid format. Please try again.")

        # Add selected pages to merger
        for start, end in page_ranges:
            for page_num in range(start-1, end):  # Convert to 0-based index
                merger.add_page(reader.pages[page_num])
    
    output_path = input("\nEnter output file path (e.g., merged.pdf): ").strip()
    
    try:
        with open(output_path, 'wb') as out_file:
            merger.write(out_file)
        print(f"\nSuccessfully created merged PDF at: {output_path}")
    except Exception as e:
        print(f"\nError writing output file: {e}")

if __name__ == "__main__":
    main()
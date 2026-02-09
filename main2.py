import os
import PyPDF2

def list_pdfs(file_name):
    """Scan current directory for PDF files"""
    pdf_files = [f for f in os.listdir(file_name) if f.lower().endswith('.pdf')]
    return pdf_files

def choose_pdf(pdf_files, multiple=False):
    """Ask user to choose one or multiple PDF files"""
    print("\nAvailable PDF files:")
    for i, file in enumerate(pdf_files, 1):
        print(f"{i}. {file}")

    if multiple:
        print("\nEnter numbers separated by commas (e.g. 1,2,4)")
    while True:
        try:
            choice = input("\nEnter your choice: ")
            if multiple:
                indices = [int(x.strip()) for x in choice.split(",")]
                selected = [pdf_files[i - 1] for i in indices if 1 <= i <= len(pdf_files)]
                if selected:
                    return selected
            else:
                idx = int(choice)
                if 1 <= idx <= len(pdf_files):
                    return pdf_files[idx - 1]
            print("Invalid choice, try again.")
        except ValueError:
            print("Please enter valid number(s).")

def parse_page_input(pages_str, total_pages):
    """Convert user input (like 1,3,5-7) into list of page indices"""
    pages = []
    for part in pages_str.split(","):
        if "-" in part:
            start, end = part.split("-")
            start, end = int(start), int(end)
            pages.extend(range(start, end + 1))
        else:
            pages.append(int(part))
    pages = [p for p in pages if 1 <= p <= total_pages]
    return sorted(set(pages))

def choose_rotation():
    """Ask user to choose rotation angle"""
    print("\nRotation options:")
    print("1. 90° clockwise")
    print("2. 180°")
    print("3. 270° clockwise (90° counter-clockwise)")
    
    rotation_map = {
        "1": 90,
        "2": 180,
        "3": 270
    }
    
    while True:
        choice = input("\nEnter your choice (1-3): ")
        if choice in rotation_map:
            return rotation_map[choice]
        print("Invalid choice, try again.")

def extract_pages(input_pdf, pages, output_pdf):
    """Create a new PDF with the selected pages"""
    reader = PyPDF2.PdfReader(input_pdf)
    writer = PyPDF2.PdfWriter()
    for p in pages:
        writer.add_page(reader.pages[p - 1])
    with open(output_pdf, "wb") as f:
        writer.write(f)
    print(f"\nNew PDF created: {output_pdf}")

def delete_pages(input_pdf, pages, output_pdf):
    """Delete given pages from PDF"""
    reader = PyPDF2.PdfReader(input_pdf)
    writer = PyPDF2.PdfWriter()
    for i in range(len(reader.pages)):
        if (i + 1) not in pages:
            writer.add_page(reader.pages[i])
    with open(output_pdf, "wb") as f:
        writer.write(f)
    print(f"\nPages deleted. New PDF: {output_pdf}")

def rotate_pages(input_pdf, pages, rotation_angle, output_pdf):
    """Rotate specified pages in a PDF"""
    reader = PyPDF2.PdfReader(input_pdf)
    writer = PyPDF2.PdfWriter()
    
    for i in range(len(reader.pages)):
        page = reader.pages[i]
        if (i + 1) in pages:
            # Rotate the specified pages
            page = page.rotate(rotation_angle)
        writer.add_page(page)
    
    with open(output_pdf, "wb") as f:
        writer.write(f)
    print(f"\nPages rotated {rotation_angle}°. New PDF: {output_pdf}")

def merge_pdfs(pdf_list, output_pdf):
    """Merge multiple PDFs"""
    merger = PyPDF2.PdfMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write(output_pdf)
    merger.close()
    print(f"\nPDFs merged into: {output_pdf}")

def password_protect(input_pdf, output_pdf, password):
    """Add password to a PDF"""
    reader = PyPDF2.PdfReader(input_pdf)

    writer = PyPDF2.PdfWriter()
    for page in reader.pages:
        writer.add_page(page)
    writer.encrypt(password)
    with open(output_pdf, "wb") as f:
        writer.write(f)
    print(f"\nPDF protected with password. Saved as: {output_pdf}")

def main():
    file_name=input("Enter directory: ")
    pdf_files = list_pdfs(file_name)
    if not pdf_files:
        print("No PDF files found in the current directory.")
        return

    print("\nChoose an operation:")
    print("1. Extract pages into new PDF")
    print("2. Delete pages from a PDF")
    print("3. Merge multiple PDFs")
    print("4. Add password to a PDF")
    print("5. Rotate pages in a PDF")
    choice = input("\nEnter your choice (1-5): ")

    if choice == "1":
        chosen_pdf = choose_pdf(pdf_files)
        reader = PyPDF2.PdfReader(chosen_pdf)
        total_pages = len(reader.pages)
        print(f"\n{chosen_pdf} has {total_pages} pages.")
        pages_str = input("Enter page numbers to extract (e.g. 1,3,5-7): ")
        pages = parse_page_input(pages_str, total_pages)
        output_name = input("Enter name for new PDF (without .pdf): ") + ".pdf"
        extract_pages(chosen_pdf, pages, output_name)

    elif choice == "2":
        chosen_pdf = choose_pdf(pdf_files)
        reader = PyPDF2.PdfReader(chosen_pdf)
        total_pages = len(reader.pages)
        print(f"\n{chosen_pdf} has {total_pages} pages.")
        pages_str = input("Enter page numbers to delete (e.g. 2,5-6): ")
        pages = parse_page_input(pages_str, total_pages)
        output_name = input("Enter name for new PDF (without .pdf): ") + ".pdf"
        delete_pages(chosen_pdf, pages, output_name)

    elif choice == "3":
        chosen_pdfs = choose_pdf(pdf_files, multiple=True)
        output_name = input("Enter name for merged PDF (without .pdf): ") + ".pdf"
        merge_pdfs(chosen_pdfs, output_name)

    elif choice == "4":
        chosen_pdf = choose_pdf(pdf_files)
        reader = PyPDF2.PdfReader(chosen_pdf)
        if reader.is_encrypted:
            print(f"\nThe file '{chosen_pdf}' is already password-protected. Exiting program.")
            return
        password = input("Enter password to protect PDF: ")
        output_name = input("Enter name for protected PDF (without .pdf): ") + ".pdf"
        password_protect(chosen_pdf, output_name, password)

    elif choice == "5":
        chosen_pdf = choose_pdf(pdf_files)
        reader = PyPDF2.PdfReader(chosen_pdf)
        total_pages = len(reader.pages)
        print(f"\n{chosen_pdf} has {total_pages} pages.")
        pages_str = input("Enter page numbers to rotate (e.g. 1,3,5-7): ")
        pages = parse_page_input(pages_str, total_pages)
        rotation_angle = choose_rotation()
        output_name = input("Enter name for rotated PDF (without .pdf): ") + ".pdf"
        rotate_pages(chosen_pdf, pages, rotation_angle, output_name)

    else:
        print("Invalid choice. Exiting.")

if __name__ == "__main__":
    main()

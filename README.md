PDF Utility Tool

A command-line Python tool for performing common PDF operations such as extracting pages, deleting pages, merging multiple PDFs, rotating pages, and adding password protection.

📌 Features

This script allows you to:

Extract specific pages from a PDF and save them as a new file

Delete pages from a PDF

Merge multiple PDF files into one

Add password protection to a PDF

Rotate selected pages within a PDF

All operations are done interactively through the terminal.

🛠 Requirements

   1. Python 3.x

   2. PyPDF2 library

Install PyPDF2:

pip install PyPDF2

📂 How It Works

When run the script:

It asks for a directory path where PDF files are located

It scans that directory and displays all .pdf files

You choose an operation

Depending on the operation, you select one or more PDFs

You provide pages, rotation angle, output filename, etc.

The script processes the file(s) and generates the new PDF

📘 Available Operations
1. Extract Pages

Select a PDF → Enter pages (e.g., 1,3,5-7) → Creates a new PDF containing only those pages.

2. Delete Pages

Select a PDF → Enter pages to remove → New PDF is created without those pages.

3. Merge PDFs

Select multiple PDFs (e.g., 1,2,4) → Merges them in the chosen order.

4. Password Protect

Select a PDF → Enter a password → Creates an encrypted PDF file.

5. Rotate Pages

Select a PDF → Choose pages → Choose rotation (90°, 180°, 270° clockwise).

📄 Page Selection Format

Page ranges support:

Single pages: 3

Multiple pages: 1,4,10

Ranges: 2-7

Mixed: 1,3,5-6,9

The script automatically filters invalid page numbers.

▶️ Running the Script

From the terminal:

python main2.py

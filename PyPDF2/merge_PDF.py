from PyPDF2 import PdfMerger

# Step 1: Create a PdfMerger object
merger = PdfMerger()

# Step 2: Append the first PDF
merger.append("D:\VU\SEM-1\WTL\WTL Assignment 20.pdf")

# Step 3: Append the second PDF
merger.append("D:\VU\SEM-1\WTL\WTL Assingment 2.pdf")

# Step 4: Save the merged PDF
merger.write("merged.pdf")
merger.close()

print("The PDFs have been merged into merged.pdf.")
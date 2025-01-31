#this script include all the reading function used by PyPDF2

from PyPDF2 import PdfReader

reader = PdfReader("D:\VU\Extras\INDUCTION_REPORT[1].pdf") #reades the PDF 

len_page = len(reader.pages) # Extract the number of pages form pages

print(len_page) 

page = reader.pages[9] # we define the page numebr for extracting the specific page 
text = page.extract_text() # we store the page extraxted text to the text veriable with the function extract_text()

print(text) #print the extracted text 





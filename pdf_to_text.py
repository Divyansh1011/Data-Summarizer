import PyPDF2

pdfFileobj = open('original_sale_deed.pdf', 'rb') 
pdfReader = PyPDF2.PdfFileReader(pdfFileobj)
print(pdfReader.numPages)

pageObj = pdfReader.getPage(0)

print(pageObj.extract_text())

pdfFileobj.close()
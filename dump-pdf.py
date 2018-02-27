import PyPDF2

if __name__ == "__main__":
    pdfFileObj = open('my_file.pdf','rb')  
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    pdfReader.numPages
    pageObj = pdfReader.getPage(9)         
    pageObj.extractText()
import PyPDF2

pdfFiles = ("A.pdf","B.pdf")
combine = PyPDF2.PdfMerger()

for filename in pdfFiles:
        pdfFile = open(filename,'rb')
        pdfReader = PyPDF2.PdfReader(pdfFile)
        combine.append(pdfReader)
        pdfFile.close()
combine.write(('merged.pdf'))


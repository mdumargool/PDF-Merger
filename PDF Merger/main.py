import PyPDF2

pdfiles=["niwas24.pdf", "udemyPhp.pdf", "UMAR_RESUME_Ac.pdf"]
Merger = PyPDF2.PdfMerger()
for filename in pdfiles:
    pdfFile=open(filename, 'rb')
    pdfReader=PyPDF2.PdfReader(pdfFile)
    Merger.append(pdfReader)
pdfFile.close()
Merger.write('merged.pdf')

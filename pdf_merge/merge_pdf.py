from PyPDF2 import PdfFileMerger


merger = PdfFileMerger()

file_list = []


for i in range(1,26):
    text = "/Users/tony/PycharmProjects/streamlit/pdf_merge/page"+str(i)+".pdf"
    file_list.append(text)

for pdf in file_list:
    merger.append(pdf)

merger.write("/Users/tony/PycharmProjects/streamlit/pdf_merge/merged.pdf")
merger.close()

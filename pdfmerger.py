from pypdf import PdfReader

r = PdfReader("exersice 8/baka.pdf")
# n = len(r.pages)
# print(n)
# page = r.pages[0]
# text = page.extract_text()
# print(text)
from pypdf import PdfWriter

merger = PdfWriter()

for pdf in ["exersice 8/baka.pdf", "exersice 8/m.pdf"]:
    merger.append(pdf)

merger.write("merged-pdf.pdf")
merger.close()
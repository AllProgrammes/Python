import PyPDF2 as p

a = p.PdfFileReader("ANY_PDF_FILE.pdf")
with open(
    "pdf_to_txt.txt", "w", encoding="utf-8"
) as pdf_file:  # makes a text file to write the content of that pdf
    for i in range(11):  # 11 is the number of pages (you can change to your choice)
        pdf_file.write(a.getPage(i).extract_text())

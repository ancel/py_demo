# https://pypi.org/project/PyPDF2/
# pip install PyPDF2
from PyPDF2 import PdfMerger
def merge_pdf(pdf_filenames, result_filename):
    fileMerger = PdfMerger()
    for pdf_filename in pdf_filenames:
        fileMerger.append(pdf_filename)
    fileMerger.write(result_filename)
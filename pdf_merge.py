from util import pdf_util

pdf_filenames=["石楼县2024年脱贫劳动力外出务工.pdf", '全页照片.pdf', '全页照片4.pdf']
result_filename="石楼县2024年脱贫劳动力外出务工_final.pdf"
pdf_util.merge_pdf(pdf_filenames, result_filename)
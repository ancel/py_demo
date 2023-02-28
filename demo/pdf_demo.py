import sys
sys.path.append('..')
from util import pdf_util
pdfs = ['C:\\Users\\Li Yujie\\Desktop\\工作居住证\\学位证和学位在线验证报告.pdf',
'C:\\Users\\Li Yujie\\Desktop\\工作居住证\\毕业证.pdf']
pdf_util.merge_pdf(pdfs, 'result.pdf')
import fitz  # PyMuPDF

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from PIL import Image
 
def png_to_pdf(png_file, pdf_file):
    # 创建一个PDF文档
    c = canvas.Canvas(pdf_file, pagesize=letter)
    
    # 加载PNG图片
    image = Image.open(png_file)
    
    # 将图片绘制到PDF文档上
    c.drawImage(image, x=0, y=0, width=image.width, height=image.height)
    
    # 关闭PDF文档
    c.save()

 
def print_pdf_pages(pdf_path):
    # 打开PDF文件
    document = fitz.open(pdf_path)
    
    for page_number in range(len(document)):
        # 获取页面
        page = document[page_number]
        
        # 渲染页面
        pix = page.get_pixmap()
        
        # 这里可以实现你自己的打印逻辑，例如显示图像或保存为新的图片文件
        # 例如，将页面保存为图片
        filename=f'page_{page_number + 1}'
        pix.save(f'{filename}.png')
        png_to_pdf(f'{filename}.png', f'{filename}.pdf')
 
# 使用函数打印PDF文档的每一页
pdf_path = '务工就业承诺书(2).pdf'  # 替换为你的PDF文件路径
print_pdf_pages(pdf_path)
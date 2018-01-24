import xlsxwriter
import codecs
import pandas as pd

file_path = 'demo.xlsx'

# 使用pandas包装excel处理类
# Create a Pandas dataframe from the data.
df = pd.DataFrame()
# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter(file_path, engine='xlsxwriter', options={'strings_to_urls': False})

# Convert the dataframe to an XlsxWriter Excel object.
df.to_excel(writer, sheet_name='Sheet1')

# Get the xlsxwriter objects from the dataframe writer object.
workbook  = writer.book
worksheet = writer.sheets['Sheet1']


# 使用xlsxwriter
# workbook = xlsxwriter.Workbook(file_path)
# worksheet = workbook.add_worksheet()

# Widen the first column to make the text clearer.
worksheet.set_column('A:A', 20)

# Add a bold format to use to highlight cells.
bold = workbook.add_format({'bold': True})

# Write some simple text.
worksheet.write('A1', 'Hello')

# Text with formatting.
worksheet.write('A2', 'World', bold)

# Write some numbers, with row/column notation.
worksheet.write(2, 0, 123)
worksheet.write(3, 0, 123.456)

# Insert an image.
worksheet.insert_image('B5', 'logo.png')

workbook.close()
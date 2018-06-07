import json
import xlsxwriter
import codecs
import sys

import pandas as pd

# json转excel
# 要求json所有字段都一致
if __name__ == '__main__':
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Create a Pandas dataframe from the data.
    df = pd.DataFrame()
    # Create a Pandas Excel writer using XlsxWriter as the engine.
    writer = pd.ExcelWriter(output_file, engine='xlsxwriter', options={'strings_to_urls': False})

    # Convert the dataframe to an XlsxWriter Excel object.
    df.to_excel(writer, sheet_name='Sheet1')

    # Get the xlsxwriter objects from the dataframe writer object.
    workbook  = writer.book
    worksheet = writer.sheets['Sheet1']
    # workbook = xlsxwriter.Workbook(output_file)
    # worksheet = workbook.add_worksheet()

    row = 0
    column = 0
    keys = None
    with open(input_file, mode='r', encoding='utf-8') as f:
        for line in f.readlines():
            try:
                line_json = json.loads(line)
            except Exception as e:
                raise e
            if None==keys:
                keys = sorted(line_json.keys())
                for key in keys:
                    worksheet.write(row, column, key)
                    column += 1
                row += 1
                column = 0
            for key in keys:
                value = line_json[key]
                if type(value)==type([]):
                    value = ','.json(value)
                worksheet.write(row, column, value)
                column += 1
            row += 1
            column = 0
    workbook.close()


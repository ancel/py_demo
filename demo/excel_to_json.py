import sys
import xlrd
from collections import OrderedDict
import json

def excel_to_json(excel_filename, sheet_id, json_filename):
    wb = xlrd.open_workbook(excel_filename)
    sh = wb.sheet_by_index(sheet_id)
    title = sh.row_values(0)
    convert_list = []
    for rownum in range(1, sh.nrows):
        rowvalue = sh.row_values(rownum)
        single = OrderedDict()
        for colnum in range(0, len(rowvalue)):
            current_cell = sh.cell(rownum, colnum)
            ctype = current_cell.ctype
            current_value =  current_cell.value
            if ctype == 2 and current_value % 1 == 0.0:
                current_value = str(int(current_value))
            single[title[colnum]] = current_value
        convert_list.append(single)
         
    with open(json_filename, mode="w", encoding='utf-8') as f:
        for json_data in convert_list:
            f.write(json.dumps(json_data, separators=(',', ':'), ensure_ascii=False)+'\n')

if __name__ == '__main__':
    excel_filename = sys.argv[1]
    json_filename = sys.argv[2]
    sheet_id = int(sys.argv[3])
    excel_to_json(excel_filename, sheet_id, json_filename)
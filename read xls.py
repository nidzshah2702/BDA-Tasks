import xlrd
wb = xlrd.open_workbook('./Desktop/myfile.xls')
wb.sheet_names()
sheet1 = wb.sheet_by_index(0)
if not sheet1.ragged_rows: 
    for row in range(sheet1.nrows):
        for col in range(sheet1.ncols):
            data = sheet1.cell(row, col)
            if data.value:
                print(data, end='')
        print()
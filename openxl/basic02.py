import openpyxl as xl

wb = xl.Workbook()
sheet = wb.active
sheet['B2'] = 'b2'
sheet.cell(row=3, column=3).value = '3, 3'
sheet.append([1, 2, 3, 4, 5])
sheet.append([1, 2, 3, 4])
sheet.append([1, 2, 3])
sheet.append([1, 2, None])
wb.save('test2.xlsx')

import openpyxl
# create a sheet in computer's memory
wb = openpyxl.Workbook()
# retrieve sheet name command
sheet = wb.get_sheet_by_name('Sheet')
print(sheet)
#assign value with a basic command
sheet['A1'] = 42
sheet['A2'] = 'Hello'
print (sheet['A2'].value)
import os
os.chdir('C:\\Users\\16616\\Documents')
# save the documnent as an xl sheet
wb.save('example2.xlsx')

# add sheets to workbook
sheet2 = wb.create_sheet()
# change title of new sheet
sheet2.title = 'Another Sheet, WoW'

import openpyxl
import os
os.chdir('C:\\Users\\16616\\Documents')

# loading the workbook and printing the class
workbook = openpyxl.load_workbook('example.xlsx')
print(type(workbook))

# obtaining the names of each sheet
print(workbook.get_sheet_names())

# assigns variable to the first sheet
sheet = workbook.get_sheet_by_name('Sheet1')
# prints class of the sheet
print(type(sheet))
#prints the object, stating that it's a 'cell'
print(sheet['A1'])
# assigns the sheet to a variable 'cell'
cell = sheet['A1']
# prints value of the variable in string value
print(str(cell.value))

for i in range(1,8):
  print(i, sheet.cell(row=i, column=2).value)
import PyPDF2
import os
os.chdir('C://Users//16616//Documents')

################
# Reading PDFs #
################

# open the pdf in the computer's memory
pdfFile = open('meetingminutes1.pdf', 'rb')

# assign a variable to our PDF
reader = PyPDF2.PdfFileReader(pdfFile)

#prints number of pages in pdf
print(reader.numPages)

#return a page object
print(reader.getPage(0))

# assign our variable to the page object
page = reader.getPage(0)

# extract text from the object and print 
print(page.extractText())

# loop through pages and print text of each
for pageNum in range(reader.numPages):
  print(reader.getPage(pageNum).extractText())


################
# Writing PDFs #
################

import PyPDF2
import os
os.chdir('C://Users//16616//Documents')

################
# Reading PDFs #
################

# open the pdf in the computer's memory and assign variables
pdf1File = open('meetingminutes1.pdf', 'rb')
pdf2File = open('meetingminutes2.pdf', 'rb')
# defining variables that create python objects from the PDF
reader1 = PyPDF2.PdfFileReader(pdf1File)
reader2 = PyPDF2.PdfFileReader(pdf2File)

# creates a python object that can accept pages
writer = PyPDF2.PdfFileWriter()

# loop through the first pdf and adding the data as a page to the python object
for pageNum in range(reader1.numPages):
  page = reader1.getPage(pageNum)
  writer.addPage(page)

# loop through the second pdf and adding the data as a page to the python object
for pageNum in range(reader2.numPages):
  page = reader2.getPage(pageNum)
  writer.addPage(page)

# opening a new pdf in write binary mode
outputFile = open('combinedminutes.pdf', 'wb')

# takes the pages added to the 'writer' variable and writes it as a PDF
writer.write(outputFile)
outputFile.close()
pdf1File.close()
pdf2File.close()
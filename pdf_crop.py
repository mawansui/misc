# -*- coding: utf-8 -*-

from PyPDF2 import PdfFileWriter, PdfFileReader

output = PdfFileWriter()
input1 = PdfFileReader(open('halo.pdf', 'rb'))

how_many_pages = input1.getNumPages()

print("Number of pages: " + str(how_many_pages))

# https://github.com/mstamy2/PyPDF2/blob/master/Sample_Code/basic_features.py

all_pages = list(range(0, how_many_pages))
reversed_pages_list = list(reversed(all_pages))

"""
Это печатает корректную версию для страниц 25-48... 
Надо бы их как-нибудь объединить!

for page in list(reversed(range(0, how_many_pages))):
current_page = input1.getPage(page)

	if (page % 2 == 0):
		current_page.mediaBox.upperLeft = (5.17, 432.19)
	else:
		current_page.mediaBox.lowerLeft = (5.17, 432.19)
	
	output.addPage(current_page)
"""

# Это печатает правильную версию для страниц 1-24

for page in range(0, how_many_pages):
	# для всех четных страниц создаем прямоугольник справа (?)
	current_page = input1.getPage(page)

	if (page % 2 == 0):
		current_page.mediaBox.lowerLeft = (5.17, 432.19)
	else:
		current_page.mediaBox.upperLeft = (5.17, 432.19)
	
	output.addPage(current_page)

outputStream = open("Halogenation2.pdf", "wb")
output.write(outputStream)
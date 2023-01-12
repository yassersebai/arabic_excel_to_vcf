import os
import sys
#get current file directory
dir_path = os.path.dirname(os.path.realpath(__file__))

import xlrd
# read first row and first column
data = xlrd.open_workbook(dir_path+r'\contacts.xls')
sheet = data.sheet_by_index(0)
i=0
j=0
k=1
# open text file with utf-8 encoding in write mode
f = open(dir_path+'\contacts.txt', 'w', encoding='utf-8')
while sheet.cell_value(i,j) != '':
    print(sheet.cell_value(i,j))
    f.write('BEGIN:VCARD')
    f.write('\n')
    f.write('VERSION:3.0')
    f.write('\n')
    f.write('FN:'+sheet.cell_value(i,j))
    f.write('\n')
    f.write('TEL;TYPE=VOICE,CELL;VALUE=text:+'+str(int(sheet.cell_value(i,k))))
    f.write('\n')
    f.write('END:VCARD')
    f.write('\n')
    i+=1
    print(i)
    try:
        sheet.cell_value(i,j)
    except IndexError:
        print('done')
        break
f.close()
my_file = dir_path+'\contacts.txt'
base = os.path.splitext(my_file)[0]
#  if file already exists as vcf erase it first
if os.path.exists(base + '.vcf'):
    os.remove(base + '.vcf')
os.rename(my_file, base + '.vcf')
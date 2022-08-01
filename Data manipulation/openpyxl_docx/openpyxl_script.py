<<<<<<< HEAD
# Te program requires some modules installed before firrst use
# googletrans module requires specific version, so we install it first
# then install transliterate & openpyxl modules.
# if this is the first time you are running this script, uncommment next four lines of code
# If you are using Dockerimage file, do not do anything!

# import os
# os.system('pip install googletrans==3.1.0a0')
# os.system('pip install transliterate')
# os.system('pip install openpyxl')

# import libraries
from transliterate import translit
import openpyxl
from googletrans import Translator
import time

start = time.time()
# instantiate
translator = Translator()

# open and read excel file
wb = openpyxl.load_workbook('/home/ivo/Python3/Data manipulation/openpyxl_docx/list.xlsx')
ws = wb.active

# iterate through the specified columns
for sheet in ws.iter_rows(min_col=5, max_col=8):
  for cell in sheet:
    # if cell.value in [None,'RANK','FIRST NAME','FAMILY NAME','POSITION']: --> shorter and faster
    if cell.value == None or cell.value == 'RANK' or cell.value == 'FIRST NAME' or cell.value == 'FAMILY NAME' or cell.value == 'POSITION':
      continue
    else:
      # if cell.value in ['FIRST NAME','FAMILY NAME']:
      if cell.value == 'FIRST NAME' or cell.value == 'FAMILY NAME':
        # transliterate the names
        cell.value = translit(cell.value, 'bg', reversed=True).title()
      else:
        # translate the rest through google translate
        t = translator.translate(cell.value)
        cell.value = t.text

# save the workbook
wb.save('/home/ivo/Python3/Data manipulation/openpyxl_docx/result.xlsx')

# Calculate the time of the code implementation
print(time.time() - start)

# import libraries
from transliterate import translit
import openpyxl
from googletrans import Translator
import time

start = time.time()
# instantiate
translator = Translator()

# open and read excel file
wb = openpyxl.load_workbook('/home/ivo/Python3/Data manipulation/openpyxl/list.xlsx')
ws = wb.active

# iterate through the specified columns
for sheet in ws.iter_rows(min_col=5, max_col=8):
  for cell in sheet:
    if cell.value == None or cell.value == 'RANK' or cell.value == 'FIRST NAME' or cell.value == 'FAMILY NAME' or cell.value == 'POSITION':
      continue
    else:
      if cell.value == 'FIRST NAME' or cell.value == 'FAMILY NAME':
        # transliterate the names
        cell.value = translit(cell.value, 'bg', reversed=True).title()
      else:
        # translate the rest through google translate
        t = translator.translate(cell.value)
        cell.value = t.text

# save the workbook
wb.save('/home/ivo/Python3/Data manipulation/openpyxl/test.xlsx')

print(time.time() - start)
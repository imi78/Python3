"""This program calculates the refugee's numbers from two Excel workbooks.
The first file must be named --> 13.xlxs with the figures form 24.02 to 31.12.2022.
The second file must be named --> 16.xlxs with the figures from 01.01.2023 onward.
The files have to be identical in terms of number of rows (from 1 to 7).
the 4th row must be the BXPs, 
5th row - "citizenship",
6th row - represents the exiting and entering PAX through the BXP column,
7th row - "Total"
in the 7th row ("Total") the new values will be written.
Any charts that you want to make should take the figures from the 7th row.
The columns may vary as it reads only the identical text written in the 4th row starting from "B" column"""


# import libraries
from openpyxl import load_workbook

#set the acive excel worksheets
wb13 = load_workbook("13.xlsx", data_only=True)
wb16 = load_workbook("16.xlsx", data_only=True)

# set the active worksheet
ws13 = wb13.active
ws16 = wb16.active

# function for sum up the values from both files
def sum_values():
    # get the column letter and change it to int ("A" > 1)
    colnum13 = col13[0].column
    colnum16 = col16[0].column
    val13_exit, val16_exit = ws13.cell(row=6, column=colnum13), ws16.cell(row=6, column=colnum16)
    val13_enter, val16_enter = ws13.cell(row=6, column=colnum13+1), ws16.cell(row=6, column=colnum16+1)
    
    # sum the values
    sum_exit = val13_exit.value + val16_exit.value
    sum_enter = val13_enter.value + val16_enter.value
              
    # get the cells coordinates (e.g. "B7", "C7")
    cell_to_write_exit = ws13.cell(row=7, column=colnum13).coordinate
    cell_to_write_enter = ws13.cell(row=7, column=colnum13+1).coordinate
    # write the values to row No. 7
    ws13[cell_to_write_exit] = sum_exit
    ws13[cell_to_write_enter] = sum_enter

for col13 in ws13.iter_cols(min_row=4, min_col=2, max_row=4):
    for col16 in ws16.iter_cols(min_row=4, min_col=2, max_row=4):
        
        # skip the merged cells
        if type(col13[0]).__name__ == 'MergedCell':
            continue
             
        # checks for empty cells
        if col13[0].value == None or col16[0].value == None:
            continue

        # check if the values are the same
        if col13[0].value == col16[0].value:
            if col13[0].value.startswith("ОБЩО"):
                sum_values()
                break
            else:
                sum_values()
                
    else:  # only execute when it's no break in the inner loop
        continue
    break # breaks the outer loop
    
wb13.save('test.xlsx')

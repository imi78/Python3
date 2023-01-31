# import libraries
import pandas as pd
from openpyxl import load_workbook
import matplotlib.pyplot as plt

# three files has to be added
# 13.xlsx - data from 24.02-31.12.2022
# 16.xlsx - any file file from year 2023
# last.xlsx - 24.02-31.12.2022 (the same file like 13.xlsx, but rename it!)
# 13.xlsx is used for a placeholder for added values form both 13.xlsx and 16.xlsx

#set the acive excel worksheets
wb13 = load_workbook("13.xlsx").active
wb16 = load_workbook("16.xlsx").active
wb_last = load_workbook("last.xlsx").active
# prepare the datasets
lst13 = []
lst16 = []
last = []
d = {}
# iterate through two files and extract the cell values
for col13, last_col in zip(wb13.iter_cols(min_row=4, min_col=2, max_row=7), wb_last.iter_cols(min_row=4, min_col=2, max_row=7)):

    for cell13, cell_last in zip(col13, last_col):
        if cell13.value == None or cell_last == None:
            continue
        # append the values to list
        lst13.append(cell13.value)
        last.append(cell_last.value)

# extract the new values from 2023
for col16 in wb16.iter_cols(min_row=4, min_col=2, max_row=7):
    for cell16 in col16:
        if cell16.value == None:
            continue
        # append the values to list
        lst16.append(cell16.value)

# iterate through lists and sum the numbers
for i in range(0, len(lst13), 5):
    for j in range(0, len(lst16), 5):
        bxp13 = lst13[i]
        bxp16 = lst16[j]
        if bxp13.startswith("ОБЩО") == False or bxp16.startswith("ОБЩО") == False:
            if bxp13 == bxp16:
                lst13[i+2] += lst16[j+2]
                lst13[i+4] += lst16[j+4]
        else:
        # this calculates the "Total" cell values
            lst13[i+1] += lst16[j+1]
            lst13[i+3] += lst16[j+3]
      
# iterate through the new lists and calculate the difference in the numbers
for i, j in zip(range(0, len(lst13), 5), range(0, len(last), 5)):
    bxp = lst13[i]
    if bxp.startswith("ОБЩО") == False:
        # variables are made for readability
        exit13, enter13 = lst13[i + 2], lst13[i + 4]
        exit_last, enter_last = last[i + 2], last[i + 4]
        exit_diff, enter_diff = (exit13 - exit_last), (enter13 - enter_last)

        # put all the info in dict if greater than 3 digit number
        if exit_diff > 100 and enter_diff > 100:
            d[bxp[4:]] = [exit_diff,enter_diff]

    else:
        # this calculates the "Total" cell values
        total_exit13, total_enter13 = lst13[i + 1], lst13[i + 3]
        total_exit_last, total_enter_last = last[i + 1], last[i + 3]
        
        exit_diff, enter_diff = (total_exit13 - total_exit_last), (total_enter13 - total_enter_last)
        d[bxp[:4]] = [exit_diff, enter_diff]

# make the dataframe
df = pd.DataFrame.from_dict(d, orient='index', columns=['Exiting', 'Entering'])
#reset the index by default
df.reset_index(inplace=True)
# change the name of the columns, so 'BXP' is added
df.columns = ['BXP', 'Exiting', 'Entering']

# plot the data from DF with grid
ax = df.plot(x='BXP', y=['Exiting', 'Entering'], kind='bar', grid=True)
# sets the bar labels to be rotated for visibility
ax.bar_label(ax.containers[0], label_type='edge', rotation=90, padding=5)
ax.bar_label(ax.containers[1], label_type='edge', rotation=90, padding=5)
# sets the margins of subplots (figure is visible at all corners)
plt.subplots_adjust(left=0.05,
                    bottom=0.374,
                    right=0.98,
                    top=0.95,
                    wspace=0.4,
                    hspace=0.4)

# get current figure
figure = plt.gcf() 
# set the figure to be expanded, so it can be visible
figure.set_size_inches(13, 8)
# saves the figure as picture
plt.savefig('foo.jpg')
# or show it
plt.show()


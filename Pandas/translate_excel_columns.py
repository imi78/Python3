from transliterate import translit
import pandas as pd

def translate_excel_columns():

  # select the correct columns to translate
  cols = ['RANK', 'FIRST NAME', 'FAMILY NAME', 'POSITION']
  
  # make dataframe
  df = pd.read_excel('list.xlsx', index_col=None, usecols=cols)
  
  # loop over each row and transliterate directly into the DataFrame
  # make it string to avoid float error
  for i in df.index:
    rank = translit(str(df['RANK'][i]), 'bg', reversed=True)
    first_name = translit(str(df['FIRST NAME'][i]), 'bg', reversed=True)
    family_name = translit(str(df['FAMILY NAME'][i]), 'bg', reversed=True)
    position = translit(str(df['POSITION'][i]), 'bg', reversed=True)

    rank = translit(str(rank), 'bg', reversed=True)
    
    # if the value is NaN, replace cut the line
    if rank == 'nan':
      rank = rank.replace('nan', "")
      continue
    if rank == 'g-zha' or rank == 'g-tsa':
      rank = "Mrs."
    
    if rank == 'g-n' or rank == 'gospodin':
      rank = "Mr."
      
    print(rank, first_name, family_name, position)

    
if __name__ =='__main__':
  translate_excel_columns()




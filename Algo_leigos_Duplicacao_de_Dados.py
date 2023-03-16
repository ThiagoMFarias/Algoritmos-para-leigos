import pandas as pd

df = pd.DataFrame({'A': [0,0,0,0,0,1,0],
                   'B': [0,2,3,5,0,2,0],
                   'C': [0,3,4,1,0,2,0]})
print(df, '\n')

df = df.drop_duplicates()
print(df)

# A função "drop_duplicates" remove os registros duplicaods encontrados nas linhas 4 e 6. 
# A Pandas DataFrame is a 2 dimensional data structure, like a 2 dimensional array, or a table with rows and columns. 
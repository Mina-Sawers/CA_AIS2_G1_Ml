import pandas as pd
from config import DROP_COLS
from preprocessing import drop_cols

df = pd.read_csv('Titanic.csv')
df = drop_cols(df,DROP_COLS)
print(df.head())
from preprocessing import *
from config import *
from pathlib import Path

base_dir = Path(__file__).resolve().parent
file_path = base_dir/"data"/"raw"/"Titanic.csv"

df = read_data_file(file_path)
df = drop_unnecessary_features(df,cols_to_drop)

df_info = check_data_type(df)
print(df_info)

df = change_data_type(df,cols_to_change,"category")
print("="*30)
print(check_data_type(df))

print(count_null(df))

df = drop_null_values(df,'Embarked')

print(count_null(df))

df = fill_null_numerical(df,"Age")

print(count_null(df))

df = fill_null_categorial(df,'Cabin')

print(count_null(df))

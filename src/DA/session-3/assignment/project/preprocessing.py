import pandas as pd
import os

def read_data_file(file_path:str)->pd.DataFrame | None:
    ''' 
    This function read a CSV file and return a DataFrame
    '''
    try:
        if not isinstance(file_path,(str,os.PathLike)):
            raise TypeError("The provided file path must be a string or path object")
        df = pd.read_csv(file_path)
        return df
    except TypeError as e:
        print(f"Invalid path type: {e}")
    except FileNotFoundError:
        print(f"file at path {file_path} not found")
    except PermissionError:
        print(f"Error: Permission Denied. file at path {file_path} cannot be read")
    except Exception as e:
        print(f"Exception: {e}")

    return None

def drop_unnecessary_features(df:pd.DataFrame,cols_to_drop:list[str])->pd.DataFrame:
    ''' 
    This function drop unnecessary features from pd.DataFrame
    '''
    return df.drop(cols_to_drop,axis=1)

def check_data_type(df:pd.DataFrame)->pd.DataFrame:
    ''' 
    This function helps you understand the structure of the database
    '''
    dtype = df.dtypes
    n_uniq = df.nunique()
    return pd.DataFrame({"Dtypes: ":dtype,"N_Uniq: ":n_uniq})

def change_data_type(df:pd.DataFrame,cols_to_change:list[str],type:str)->pd.DataFrame:
    ''' 
    This function changes the data type of certain columns to specific data type
    '''
    df[cols_to_change] =  df[cols_to_change].astype(type)
    return df

def count_null(df:pd.DataFrame)->pd.DataFrame:
    null = df.isnull().sum()
    ratio = null / df.shape[0] * 100
    return pd.DataFrame({"null: ":null,"ratio":ratio})


def drop_null_values(df:pd.DataFrame,target:str)->pd.DataFrame:
    ''' 
    This functions drop null values in specific column
    '''
    return df.dropna(subset=[target])

def fill_null_numerical(df:pd.DataFrame,target:str)->pd.DataFrame:
    ''' 
    This function fills null numerical values in specific column with median
    '''
    median = df[target].median()
    df[target] = df[target].fillna(median)
    return df

def fill_null_categorial(df:pd.DataFrame,target:str)->pd.DataFrame:
    ''' 
    This function fills null categorial values in specific column with mode
    '''
    mode = df[target].mode()
    df[target] = df[target].fillna(mode)[0]
    return df
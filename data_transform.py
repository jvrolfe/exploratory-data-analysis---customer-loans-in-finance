import pandas as pd

class DataTransform:
    '''
    This class is used transform the data after it is loaded in. 

    Parameters:
    df (dataframe): A dataframe of data.
          
    Methods:
    extract_int(int_to_convert_columns): Extracts integer values from 
        specified colums.
    to_date_column(date_cols_to_convert): Converts column data to date data 
        type. 
    to_cat_column(cat_cols_to_convert): Converts column data to catergory
        data type.
    '''
    def __init__(self, df):
        self.df = df             

    def extract_int(self, int_to_convert_columns):
        '''
        This function extracts the integer values from an object column and
        drops the string values. This function overwrites the data in the
        column.

        Args:
        int_to_convert_columns (list): A list of columns to apply the function
            to.

        '''
        for col in int_to_convert_columns:
            self.df[col] = self.df[col].str.extract("(\d+)").\
                                            astype(float, errors="ignore")
    
    def to_date_column(self, date_cols_to_convert):
        '''
        This function converts data columns to datetime format. This function 
        overwrites the data in the column.

        Args:
        date_cols_to_convert (list): A list of columns to apply the function
            to.
        '''
        self.df[date_cols_to_convert] = self.df[date_cols_to_convert].\
                                    apply(lambda x: pd.to_datetime\
                                        (x, errors="coerce", format="%b-%Y"))

    def to_cat_column(self, cat_cols_to_convert):
        '''
        This function converts string values from an object column to a
        category data type. This function overwrites the data in the column.

        Args:
        cat_cols_to_convert (list): A list of columns to apply the function
            to.
        '''
        self.df[cat_cols_to_convert] = self.df[cat_cols_to_convert].\
                                        astype("category")
      
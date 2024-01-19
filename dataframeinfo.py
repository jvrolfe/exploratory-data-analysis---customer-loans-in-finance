
class DataFrameInfo:
    '''
    This class is used to view basic information about the dataframe. 

    Parameters:
    df (dataframe): A dataframe of data.
            
    Methods:
    stats_overview(): Prints the shape of the dataframe and applies the
        .describe() function.
    datatypes(): Prints the data type for each column.
    category_count(): Returns the counts for each category column.  
    null_count_percent(): Returns the null count and percentage for each 
        column.
    '''
    def __init__(self, df):
        self.df = df
    
    def stats_overview(self):
        '''
        This function prints the shape of the dataframe as well as a statistical 
        overview through the use of the .describe() method. 
        '''
        print(f"The shape of the dataframe is {self.df.shape}.")
        print("\n")
        print("Statistical Overview:")
        print(self.df.describe())
    
    def datatypes(self):
        '''
        This function prints the data type for each column in the dataframe.
        '''
        print("Column Datatypes:")
        print(self.df.info())
    
    def category_count(self):
        '''
        This function calculates how many categories there are.

        Returns:
        unique_counts (int): A count of the number of unique categories.
        '''
        category_cols = self.df.select_dtypes(include="category").columns
        unique_counts = self.df[category_columns].nunique()
        return unique_counts
    
    def null_count_percent(self):
        '''
        This function prints the null count and percentage of nulls for each 
        column. 

        '''
        null_count = self.df.isnull().sum()
        null_percent = self.df.isnull().sum()/len(self.df)
        print("The null count is:")
        print(null_count)
        print("The null percentage is:")
        print(null_percent)
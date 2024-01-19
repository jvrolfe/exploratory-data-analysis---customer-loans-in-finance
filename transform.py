import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from statsmodels.graphics.gofplots import qqplot

from xgboost import XGBClassifier

class DataFrameTransform:
    '''
    This class is used to transform the data within the dataframe after basic
    data transform has been applied. 

    Parameters:
    df (dataframe): A dataframe of data. 
            
    Methods:
    impute_with_mean(column_list): Imputes null values with the mean 
        of the column for a list of given columns.
    impute_with_median(column_list): Imputes null values with the mean 
        of the column for a list of given columns.
    drop_null_rows(column_list): Drops null values in given columns.
    replace_nulls(column_list, val): Replaces null values with a given value
        for all nulls in a iven list of columns. 
    identify_skewed_columns(threshold): Returns the skew values for all columns
        the are above the threshold in the dataframe.
    transform_log(threshold): Transforms the skewed columns idetified with 
        identify_skewed_columns().
    identify_outliers_IQR(column, threshold): Identifies outliers in a given
        column through a threshold in columns using the IQR method. 
    identify_outliers_IQR_all_columns(threshold): Identifies outliers in all
        columns through a threshold in columns using the IQR method. 
    outlier_count_per_column(threshold): Gives the outlier count per column.
    remove_outliers(threshold): Removes outliers from columns in a given list. 
    identify_correlated_columns(); Applies the perason correlation method to 
        all columns in the dataframe. Generates a heatmap to show the 
        correlation.
    encode_categorical_columns(column_list); Encodes categorical data to be 
        used in a correlation matrix. 
    
    '''
    def __init__(self, df):
        self.df = df
    
    def impute_with_mean(self, column_list):
        '''
        This function imputes nulls in a column with the mean of the column. 
        Occurs inplace. 

        Args:
        column_list (list): A list of columns to apply this function to. 
        '''
        for col in column_list: 
            self.df[f"{col}"].fillna(self.df[f"{col}"].mean(), inplace=True)
    
    def impute_with_median(self, column_list):
        '''
        This function imputes nulls in a column with the median of the column. 
        Occurs inplace. 

        Args:
        column_list (list): A list of columns to apply this function to. 
        '''
        for col in column_list: 
            self.df[f"{col}"].fillna(self.df[f"{col}"].median(), inplace=True)
    
    def drop_null_rows(self, column_list):
        '''
        This function drops nulls in a column. Occurs inplace. 

        Args:
        column_list (list): A list of columns to apply this function to. 
        '''
        for col in column_list:     
            self.df.dropna(subset=[f"{col}"], inplace=True)
    
    def replace_nulls(self, column_list, val):
        '''
        This function replaces nulls in a column with a specified value. 
        Occurs inplace. 

        Args:
        column_list (list): A list of columns to apply this function to. 
        val (int/str): A integer or string value. 
        '''
        for col in column_list: 
            self.df[f"{col}"].fillna(val, inplace=True)
        
    def identify_skewed_columns(self, threshold=2):
        '''
        This function applies the .skew() method to each column in a dataframe
        and returns a list of columns with a skew above a given threshold. 

        Args:
        Threshold (list): The threshold value to filter the returned column 
            list. 
        
        Returns:
        skewed_columns (list): A list of columns with a skew above the 
            threshold. 
        '''
        numeric_columns = self.df.select_dtypes(include=[np.number]).columns
        skewness = self.df[numeric_columns].apply(lambda x: x.skew())
        skewed_columns = skewness[abs(skewness) > threshold].index.tolist()
        return skewed_columns
    
    def transform_log(self, threshold=2):
        '''
        This function applies a log transformation to a given list of skewed
        columns. Occurs inplace.

        Args:
        threshold (list): The threshold passed to the identify_skewed_columns()
        function.
        '''
        skewed_columns = self.identify_skewed_columns(threshold)
        for col in skewed_columns: 
            self.df[f"{col}"] = self.df[f"{col}"].map(lambda\
                i: np.log1p(i) if i > 0 else 0)
    
    def identify_outliers_IQR(self, column, threshold=1.5):
        '''
        This function identifies outliers through the IQR method for a 
        specified column. 

        Args:
        column (str): The column to identify outliers in. 
        threshold (int): The multiplier which outliers must be beyond to be 
            classified as an outlier.
        
        Returns:
        outliers (dict): A dictionary of outliers. 
        '''
        q1 = self.df[column].quantile(0.25)
        q3 = self.df[column].quantile(0.75)
        iqr = q3 - q1
        
        lower_bound = q1 - threshold * iqr
        upper_bound = q3 + threshold * iqr
        
        outliers = self.df[(self.df[column] < lower_bound) | (self.df[column]\
            > upper_bound)].index.tolist()
        return outliers
    
    def identify_outliers_IQR_all_columns(self, threshold=1.5):
        '''
        This function identifies outliers through the IQR method for the whole 
        dataframe. 

        Args:
        threshold (int): The multiplier which outliers must be beyond to be 
            classified as an outlier.
        
        Returns:
        non_empty (dict): A dictionary of outliers with no empty key-value 
        pairs. 
        '''
        outliers_dict = {}
        
        for column in self.df.select_dtypes(include=[np.number]).columns:
            outliers = self.identify_outliers_IQR(column, threshold)
            outliers_dict[column] = outliers
        
        non_empty = {key: value for key, value in outliers_dict.items() if value}

        return non_empty
    
    def outlier_count_per_column(self, threshold):
        '''
        This function counts the outliers per column. 

        Args: 
        threshold (int): Threshold value to be passed to the 
        identify_outliers_IQR_all_columns() function. 
        
        Returns:
        A dictionary with the columns and the number of outliers.  
        '''
        outliers = self.identify_outliers_IQR_all_columns(threshold)
        return {key: len(value) for key, value in outliers.items() if value}
    
    def remove_outliers(self, threshold=1.5):
        '''
        This function removes outleirs depending on the number of outliers in 
        a given column. 
        If the count is below 10, then outlier rows are removed.
        If the count is above 10, then the top 1% of data is removed for 
        positive skews, and the bottom 1% of data is removed for negativ skews.
        Occurs inplace. 

        Args: 
        threshold (int): Threshold value to be passed to the 
        outlier_count_per_column() function.                 
        '''
        outliers = self.outlier_count_per_column(threshold)
        
        for column, count in outliers.items():
            skewness = self.df[column].skew()
            if count < 10:
                # Remove outliers if count is less than 10
                self.df = self.df[~self.df.index.isin(self.\
                    identify_outliers_IQR_all_columns()[column])]
            elif skewness > 0:
                # Remove the top 1% of data for positively skewed columns
                upper_percentile = 99
            else:
                # Remove the bottom 1% of data for negatively skewed columns
                upper_percentile = 100

                upper_bound = np.percentile(self.df[column].dropna(),\
                    upper_percentile)

                 # Identify and remove outliers above the calculated upper bound
                self.df = self.df[~(self.df[column] > upper_bound)]
          
    def identify_correlated_columns(self): 
        '''
        This function calculates the correlation between columns using the 
        pearson method. It generates a heatmap to visually show this.                 
        '''
        numeric_df = self.df.select_dtypes(include=["number"])
        correlation_matrix = numeric_df.corr(method="pearson")
        plt.figure(figsize=(20, 20))
        sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f",\
            linewidths=0.5)
        plt.title("Correlation Matrix")
        plt.show()
    
    def encode_categorical_columns(self, column_list):
        '''
        This function encodes categorical data to be used in the   
        identify_correlated_columns() function. A new column is create called 
        x_encoded, where x is the column name. 

        Returns:
        df (dataframe): The dataframe with the additional columns.              
        '''
        for column in column_list:
            if self.df[column].dtype.name == "category":
                self.df[f'{column}_encoded'] = self.df[column].cat.codes
        return self.df

      
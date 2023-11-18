import pandas as pd
import datetime as dt  
from scipy.stats import normaltest
from statsmodels.graphics.gofplots import qqplot
from matplotlib import pyplot
      
def load_data(file_path):
    '''
    This function reads in the loan_payments csv file.
    
    Parameters:
    file_path (str): Path to the desired csv file. 
    
    Returns:
    data (df): A dataframe of the read csv file. 
    '''
    data = pd.read_csv(file_path)
    return data

# Load in the data
loan_data = load_data("loan_payments_data.csv")
loan_data_cleaned = loan_data.copy()

class DataTransform:
    def __init__(self, df):
        self.df = df             

    def extract_int(self, int_to_convert_columns):
        for col in int_to_convert_columns:
            self.df[col] = self.df[col].str.extract("(\d+)")\
                .astype(float, errors="ignore")
                                            
    def to_date_column(self, date_cols_to_convert):
        self.df[date_cols_to_convert] = self.df[date_cols_to_convert].\
                                    apply(pd.to_datetime, format="%b-%Y")

    def to_cat_column(self, cat_cols_to_convert):
        self.df[cat_cols_to_convert] = self.df[cat_cols_to_convert].\
                                        astype("category")
    
class DataFrameInfo:
    def __init__(self, df):
        self.df = df
    
    def stats_overview(self):
        print(f"The shape of the dataframe is {self.df.shape}.")
        print("\n")
        print("Statistical Overview:")
        print(self.df.describe())
    
    def datatypes(self):
        print("Column Datatypes:")
        print(self.df.info())
    
    def category_unique_count(self):
        category_cols = self.df.select_dtypes(include="category").columns
        unique_counts = self.df[category_columns].nunique()
        print(unique_counts)
    
    def category_value_count(self):
        for col in category_columns:
            unique_value_counts = self.df[col].value_counts()
            print(unique_value_counts)
        
    def null_count_percent(self):
        null_count = self.df.isnull().sum()
        null_percent = self.df.isnull().sum()/len(self.df)
        print("The null count is:")
        print(null_count)
        print("The null percentage is:")
        print(null_percent)

class DataFrameTransform:
    def __init__(self, df):
        self.df = df
    
    def impute_with_mean(self, column_list):
        for col in column_list: 
            self.df[f"{col}"].fillna(self.df[f"{col}"].mean(), inplace=True)
    
    def impute_with_median(self, collumn_list):
        for col in column_list: 
            self.df[f"{col}"].fillna(self.df[f"{col}"].median(), inplace=True)
    
    def drop_null_rows(self, column_list):
        for col in column_list:     
            self.df.dropna(subset=[f"{col}"], inplace=True)
    
    def replace_nulls(self, column_list, val):
        for col in column_list: 
            self.df[f"{col}"].fillna(val, inplace=True)
        
    def identify_skewed_columns(self, threshold=2):
        numeric_columns = self.df.select_dtypes(include=[np.number]).columns
        skewness = self.df[numeric_columns].apply(lambda x: x.skew())
        skewed_columns = skewness[abs(skewness) > threshold].index.tolist()
        return skewed_columns
    
    def transform_log(self, threshold=2):
        skewed_columns = self.identify_skewed_columns(threshold)
        for col in skewed_columns: 
            self.df[f"{col}"] = self.df[f"{col}"].map(lambda\
                i: np.log1p(i) if i > 0 else 0)

class DistributionChecker:
    def __init__(self, df):
        self.df = df 
    
    def dagostino(self):
        stat, p = normaltest(self.df, nan_policy='omit')
        print('Statistics=%.3f, p=%.3f' % (stat, p))       
        
    def mean_vs_median(self):
        print(f'The median is {self.df.median()}')
        print(f'The mean is {self.df.mean()}')      

class Plotter:
    def __init__(self, df):
        self.df = df
    
    def histogram(self):
        self.df.hist(bins=40)
    
    def q_q_plot(self):
        qq_plot = qqplot(self.df , scale=1 ,line='q')
        pyplot.show()
    
    def bar_plot(self):
        null_counts = self.df.isnull().sum()
        null_counts = null_counts[null_counts > 0]
        if not null_counts.empty:
            plt.figure(figsize=(10, 5))
            sns.barplot(x=null_counts.index, y=null_counts, color='red', alpha=0.7)

            plt.title('Number of Null Values in Each Column')
            plt.ylabel('Count')
            plt.xticks(rotation=73)
            plt.show()
        else:
            print('No null values in the DataFrame.')

# Transform the database

transform_loan_data = DataTransform(loan_data_cleaned)

# Create a list of columns to extract the integer from
integer_columns = ["term", "employment_length"]
transform_loan_data.extract_int(integer_columns)

# Create a list of the date columns to convert
date_columns = ["issue_date", "earliest_credit_line", "last_payment_date", \
                "next_payment_date", "last_credit_pull_date"]
transform_loan_data.to_date_column(date_columns)

#Create a list of the category columns to convert
category_columns = ["grade", "sub_grade", "home_ownership", \
                    "verification_status", "loan_status", "purpose", \
                    "application_type", "payment_plan"]
transform_loan_data.to_cat_column(category_columns)

# Get a basic overview of the database
overview_loan_data = DataFrameInfo(loan_data_cleaned)
# overview_loan_data.stats_overview()
# overview_loan_data.datatypes()
# overview_loan_data.category_unique_count()
# overview_loan_data.category_value_count()
# overview_loan_data.null_count_percent()

# Clean the null values (all variables with >60% nulls are dropped)
loan_data_cleaned.drop(["mths_since_last_delinq", "mths_since_last_record", \
        "next_payment_date", "mths_since_last_major_derog", \
        "last_credit_pull_date", "collections_12_mths_ex_med"], \
        axis=1, inplace=True)

# Transform the dataframe
transform = DataFrameTransform(loan_data_cleaned)

impute_with_median_list = ["int_rate", "funded_amount", "employment_length"]
transform.impute_with_median(impute_with_median_list)

replace_nulls_list = ["term"]
transform.replace_nulls(replace_nulls_list, 36)

remove_rows_list = ["last_payment_date"]
transform.drop_null_rows(remove_rows_list)

overview_loan_data_cleaned = DataFrameInfo(loan_data_cleaned)
overview_loan_data_cleaned.null_count_percent()
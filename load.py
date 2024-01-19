
from matplotlib import pyplot as plt
import numpy as np  
from scipy.stats import normaltest
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from statsmodels.graphics.gofplots import qqplot
import statsmodels.formula.api as smf
from xgboost import XGBClassifier

if __name__ == "__main__":
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

loan_data = load_data("loan_payments_data.csv")
loan_data_cleaned = loan_data.copy()
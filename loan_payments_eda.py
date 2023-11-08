import pandas as pd
      
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


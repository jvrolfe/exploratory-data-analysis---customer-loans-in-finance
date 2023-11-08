import pandas as pd
      
def load_data(file_path):
    data = pd.read_csv(file_path)
    return data

loan_data = load_data("loan_payments_data.csv")

print(loan_data.head())
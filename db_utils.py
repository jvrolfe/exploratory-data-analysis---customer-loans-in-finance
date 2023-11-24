from sqlalchemy import create_engine
from yaml import safe_load
import pandas as pd

def load_creds(file_path):
    '''
    This function is used to load in a yaml file containing the 
    credentials required to access a database.
    
    Parameters:
    file_path (str): The file path of the yaml file containing 
    the credentials. 
    
    Attributes:
    creds (dict): A dictionary of the credentials. 
    
    Returns:
    creds(dict)
    '''
    with open(file_path, "r") as file:
        creds = safe_load(file)
    return creds

class RDSDatabaseConnector:
    '''
    This class is used to connect to the desired database. 
    
    Paramters:
    db_creds (dict): A dictionary of the credentials.
    
    Methods:
    db_engine(): Creates an SQLalchemy engine that interprets the database.
    db_extraction(): Connects to and queries the database to extract
    the loan_payments table.
    sav_to_csv(data, file_path): Saves the queried data to a csv file. 
    '''
    
    def __init__(self, db_creds):
        self.db_creds = db_creds

    def db_engine(self):
        db_url = f"postgresql://{self.db_creds['RDS_USER']}:{self.db_creds['RDS_PASSWORD']}@{self.db_creds['RDS_HOST']}:{self.db_creds['RDS_PORT']}/{self.db_creds['RDS_DATABASE']}"
        self.engine = create_engine(db_url)
 
    def db_extraction(self) :
         connection = self.engine.connect()  
         query = "SELECT * FROM loan_payments"
         data = pd.read_sql(query, connection)
         connection.close()
         return data
    
    def save_to_csv(self, data, file_path):
        data.to_csv(file_path, index=False)


if __name__ == "__main__": 
    creds = load_creds("credentials.yaml")
    db_connect = RDSDatabaseConnector(creds)
    db_connect.db_engine()
    data = db_connect.db_extraction()
    db_connect.save_to_csv(data, "loan_payments_data.csv")
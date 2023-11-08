import yaml
from sqlalchemy import create_engine



def load_creds(file_path):
    with open(file_path, "r") as file:
        creds = yaml.safe_load(file)
    return creds
class RDSDatabaseConnector:
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

creds = load_creds("credentials.yaml")
db_connect = RDSDatabaseConnector(creds)
db_connect.db_engine()
data = db_connect.db_extraction()
db_connect.save_to_csv(data, "loan_payments_data.csv")
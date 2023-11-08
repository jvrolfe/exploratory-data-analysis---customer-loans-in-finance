# Exploratory Data Analysis - Customer Loans in Finance

In this project, I have explored a loan payments database to generate exploratory data analysis, and pull together learning content up to this point. This was done as part of the AiCore Data Analytics pathway content. [Exploratory data analysis](https://en.wikipedia.org/wiki/Exploratory_data_analysis) is an approach commonly used in data analysis to summarise key characteristics of a dataset. 


## Requirements

- Fork this repo
- Clone this repo
- Python3

## Usage


## File Structure 

**db_utils.py**: This module connects to the database.
- __`load_creds()`__: This function loads a .yaml file and returns the credentials (creds). The.yaml file containing the credetials is not in this repo for privacy reasons. In order to connect your own credentials, either name the yaml file `credentials.yaml` or alterhe code accordingly. 
- __`RDSDatabaseConnector()`__: This class connects to the database using the credentials loaded in from __`load_creds()`__.
    - __`__init__()`__: This intialises the main variables of the class. It one parameter along with self:
        - `db_creds` (dict): A dictionary containing the credentials required to access the appropriate database.



## Installation

    $ git clone https://github.com/jvrolfe/exploratory-data-analysis---customer-loans-in-finance.git

## Licence

Licence: `None`
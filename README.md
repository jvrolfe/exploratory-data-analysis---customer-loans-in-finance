# Exploratory Data Analysis - Customer Loans in Finance

In this project, I have explored a loan payments database to generate exploratory data analysis, and pull together learning content up to this point. This was done as part of the AiCore Data Analytics pathway content. [Exploratory data analysis](https://en.wikipedia.org/wiki/Exploratory_data_analysis) is an approach commonly used in data analysis to summarise key characteristics of a dataset. 

Here, I have created a set of classes that are able to perform all of the key steps in EDA. Then, I have taken a loan payments dataset and described each step of the EDA process as I have performed them. 

Throughout this process, I have gained a better understanding of the important factors of EDA and have appreciated that there is no blueprint for the "perfect" EDA, but rather it is the reasoning behind your decisions that are the most important factor. 

## Requirements

- Fork this repo
- Clone this repo
- Python3

## Usage

To use this jupyter notebook, open it and load in your own data. 

Once you have done this, you can use the classes and methods show to work through you analysis. I have provided my own reasoning for my dataset, so feel free to use this as a guide. 

Uncomment lines as necessary when describing the dataset. 

## File Structure 

**db_utils.py**: This module connects to the database.
- __`load_creds()`__: This function loads a .yaml file and returns the credentials (creds). The.yaml file containing the credetials is not in this repo for privacy reasons. In order to connect your own credentials, either name the yaml file `credentials.yaml` or alterhe code accordingly. 
- __`RDSDatabaseConnector()`__: This class connects to the database using the credentials loaded in from __`load_creds()`__.
    - __`__init__()`__: This intialises the main variables of the class. It one parameter along with self:
        - `db_creds` (dict): A dictionary containing the credentials required to access the appropriate database.

**loan_data_dict.md**: This file contains the definitions of all the columns in the dataset. 

**loans.ipynb**: This module contains all the classes needed to analyse the dataset, alongside a walkthtough of analysing the data with markdown cells. There are five classes within the file (see the DocString for more information): 
- __`DataTransform`__: With this class, simple columns transformations can be performed. 
- __`DistributionChecker`__: With this class, the distribution of columns can be assessed. 
- __`DataFrameInfo`__: Summary statistics on the dataframe can be performed. 
- __`Plotter`__: This class contains methods to plot the data in different ways.
- __`DataFrameTransform`__: This class contains a set of methods to transform the data in different ways e.g null imputations and log transformations.

For more information on each of these, please see the docstrings in the jupyter notebook. 

## Installation

    $ git clone https://github.com/jvrolfe/exploratory-data-analysis---customer-loans-in-finance.git

## Licence

Licence: `None`
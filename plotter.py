
class Plotter:
    '''
    This class is used to create plots of the dataframe. 

    Parameters:
    df (dataframe): A dataframe of data. This can also be a subset of the data.
            
    Methods:
    histogram(): Generates a histogram.
    q_q_plot(): Generates a Q-Q plot.
    box_plot(): Generates a box plot. 
    bar_plot(): Generates a bar plot.
    '''
    def __init__(self, df):
        self.df = df
    
    def histogram(self):
        '''
        This function creates a histogram with 40 bins. Both the size of the 
        histogram and the bin size can be changed as needed.

        '''
        self.df.hist(figsize=(15, 15), bins=40)
        
    
    def q_q_plot(self, column_list=None):
        '''
        This function generates a Q-Q plot to further analyse the distribution
        of the dataframe. It can take either a list of columns or the whole 
        dataframe. 

        '''
        if isinstance(self.df, pd.DataFrame): 
            # Check if the columns are numeric and create a list of those that 
            # are numeric.. 
            if column_list is None:
                column_list = self.df.select_dtypes(include=[np.number]).columns
            elif isinstance(column_list, list):
                column_list = [col for col in columns if col in \
                    self.df.select_dtypes(include=[np.number]).columns]
            else:
                raise ValueError("Invalid input. Please provide a list of \
                                 numeric column names.")
            
            # Applies the Q-Q plot function to each column depending on whether
            # df is a list of columns or a datarame. 
            for col in column_list: 
                qq_plot = qqplot(self.df[col], scale=1 ,line='q')
                plt.title(f"Q-Q Plot for {col}")
                plt.show()
        elif isinstance(self.df, pd.Series): 
                qq_plot = qqplot(self.df, scale=1 ,line='q')
                plt.show()
        else:
                raise ValueError("Invalid input. Please provide a list of \
                                 numeric column names.")
    
    def box_plot(self, column_list=None):
        '''
        This function generates a box plot. This function can take either a 
        list of columns or the whole dataframe

        '''
        # Check if the columns are numeric and create a list of those that 
        # are numeric. 
        if isinstance(self.df, pd.DataFrame): 
            if column_list is None:
                column_list = self.df.select_dtypes(include=[np.number]).columns
            elif isinstance(column_list, list):
                column_list = [col for col in column_list if col in \
                    self.df.select_dtypes(include=[np.number]).columns]
            else:
                raise ValueError("Invalid input. Please provide a list of \
                                 numeric column names.")
            # Applies the box plot function to each column depending on whether
            # df is a list of columns or a datarame. 
            for col in column_list: 
                box_plot = plt.boxplot(self.df[col])
                plt.title(f"Boxplot Plot for {col}")
                plt.show()
        elif isinstance(self.df, pd.Series): 
                qq_plot = plt.boxplot(self.df)
                plt.show()
        else:
                raise ValueError("Invalid input. Please provide a list of \
                                 numeric column names.")
            
    def bar_plot(self):
        '''
        This function generates a bar plot to compare the number of nulls in 
        each column of the dataframe. It can be useful to ensure that all 
        nulls have been imputed/removed from the dataframe.
        '''
        null_counts = self.df.isnull().sum()
        null_counts = null_counts[null_counts > 0]
        if not null_counts.empty:
            plt.figure(figsize=(10, 5))
            sns.barplot(x=null_counts.index, y=null_counts, color='red', \
                        alpha=0.7)

            plt.title('Number of Null Values in Each Column')
            plt.ylabel('Count')
            plt.xticks(rotation=73)
            plt.show()
        else:
            print('No null values in the DataFrame.')
    
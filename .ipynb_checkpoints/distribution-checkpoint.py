from scipy.stats import normaltest

class DistributionChecker:
    '''
    This class is used to check the distribution of the data in the 
    dataframe. 

    Parameters:
    df (dataframe): A dataframe of data.
            
    Methods:
    dagostino(): Applies the D'Agostino normalisation test to  each 
        column in the the dataframe.
    mean_vs_median(): Prints the median and mean of each column in 
        the dataframe. 
    '''
    def __init__(self, df):
        self.df = df 
    
    def dagostino(self):
        '''
        This function applies the D'Agostino K^2 test to all columns in the 
        dataframe. This is a goodness-of-fit measure.

        '''
        stat, p = normaltest(self.df, nan_policy='omit')
        print('Statistics=%.3f, p=%.3f' % (stat, p))       
        
    def mean_vs_median(self):
        '''
        This function calculates the mean and median of each column in the 
        dataframe.
        
        '''
        print(f'The median is {self.df.median()}')
        print(f'The mean is {self.df.mean()}')
    
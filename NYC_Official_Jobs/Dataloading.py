import pandas as pd



def Clean_df(df):

    """
    returns a new dataframe after removing some error data, 
    duplicate data from data frame and also changed type of 'date' to datatypes
    """
    df['Posting Date']=pd.to_datetime(df['Posting Date'])#converted to 'date' type
    df1=df.drop_duplicates(cols=['Job ID'])
    #remove duplicate since some jobs opening to internal and external share the same job id
    df2=df1[df1['# Of Positions']<int(100)]
    #number of open position should not be more than 100 for each job id,otherwise it's abnormal
    return df2
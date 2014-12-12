import pandas as pd



def Clean_df(df):
    """
    clean the raw dataset, convert date type drop duplicate, drop invalid entries

    :param df: the raw dataframe

    :return: a cleaned dataframe
    """

    df['Posting Date'] = pd.to_datetime(df['Posting Date'])         # converted to 'date' type

    #remove duplicate since some jobs opening to internal and external share the same job id
    df1 = df.drop_duplicates(cols=['Job ID'])

    #number of open position should not be more than 100 for each job id,otherwise it's abnormal
    df2 = df1[df1['# Of Positions'] < int(100)]

    return df2
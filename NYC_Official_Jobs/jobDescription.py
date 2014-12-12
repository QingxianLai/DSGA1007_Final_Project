import pandas as pd
import matplotlib.pyplot as plt
from Dataloading import Clean_df

def show_job_info(jobID,kwd,df):
    """
    function takes the job id, keyword and dataframes as  inputs and print brief information about the job
    """
    jobFeatures=['Business Title','Salary Range From','Salary Range To','Salary Frequency','Minimum Qual Requirements']
    #list the features of job info 
    job_info=df[df['Job ID']==int(jobID)][jobFeatures]#slim the dataframe to an instance of inputed job ID 
    job_info=job_info.values#extract values into ndarray from dataframe
    print '\nJob Title: %s\n%s salary level: $%s --$%s \nMin Requirements:\n%s \n'%(job_info[0][0],job_info[0][3],job_info[0][1],job_info[0][2],job_info[0][4])
 


def degreeDict(dataframe):
    """
    takes the dataframe as input, 
    returns a dictionary  with key: Degree,  Values: total number of available jobs 
    """
    #print df.dtypes
    df=dataframe.set_index('Job ID')#set the Job ID be the index of dataframe
    df1=df['Minimum Qual Requirements'].dropna()#remove null value
    position= df['# Of Positions']
    degree={}
    #initialize degree dictionary
    degree['Bachelor']=0
    degree['Master']=0
    degree['High School or others non-degree']=0
    
    for jobid in df1.index:
        wordList=df1[jobid].rstrip().split()
        wordList=map(lambda x: x.lower(), wordList)
        #the following calculates the number of positions that needs a certain degree at least
        #cumulate the corresponding number of positions to generate the value of a specific key( education level)
        if 'baccalaureate' in wordList or 'bachelor' in wordList:
            if 'high' not in wordList:
                numPositions1=position.get(jobid)
                degree['Bachelor']+=1*numPositions1#at least a bachelor degree 
        if "master's" in wordList:
            if 'baccalaureate' not in wordList or 'bachelor' not in wordList:
                numPositions2=position.get(jobid)
                degree['Master']+=1*numPositions2#at least a master degree
    degree['High School or others non-degree']=position.sum()-degree['Master']-degree['Bachelor']

    return degree



def test():
     df = pd.read_csv("../NYC_Jobs.csv")
     df = Clean_df(df)
     degree = degreeDict(df)
     print degree


if __name__ == "__main__":
    test()
    
    
    
    
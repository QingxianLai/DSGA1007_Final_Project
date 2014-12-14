import pandas as pd
from input_filter import filter_the_job
import re


def show_job_infomation_df(df):
    job_features = ['Job ID', 'Business Title']
    df2 = df.loc[:, job_features]
    df3 = df2.set_index('Job ID')
    print df3

def show_job_infomation_s(series):
    for i in list(series.index)[:13]:
        print i,':   ',series[i],'\n'

    Job_description = series['Job Description']
    Job_description = re.sub(' +',' ',Job_description)
    Job_description = Job_description.replace('\xc3\xa2\xe2\x82\xac\xc2\xa2','\n  ')
    print 'Job Description:  \n'
    print Job_description,'\n'

    min_requirment = series['Minimum Qual Requirements']
    min_requirment = re.sub(' +',' ',min_requirment)
    min_requirment = min_requirment.replace('\xc3\xa2\xe2\x82\xac\xc2\xa2','\n  ')
    print 'Minimum Qual Requirements:  \n'
    print min_requirment,'\n'

    prefer_skill = series['Preferred Skills']
    prefer_skill = re.sub(' +',' ',prefer_skill)
    prefer_skill = prefer_skill.replace('\xc3\xa2\xe2\x82\xac\xc2\xa2','\n  ')
    print 'Preferred Skills:  \n'
    print prefer_skill,'\n'

    a_info = series['Additional Information']
    a_info = re.sub(' +',' ',a_info)
    a_info = a_info.replace('\xc3\xa2\xe2\x82\xac\xc2\xa2','\n  ')
    print 'Additional Information:  \n'
    print a_info,'\n'

    for i in list(series.index)[18:]:
        print i,':   ',series[i],'\n'

def test():
     df = pd.read_csv("../NYC_Jobs.csv")
     a_job = df.iloc[15,:]
     #show_job_infomation_s(a_job)
     keyword = 'code'
     job_list = filter_the_job(df,keyword)
     show_job_infomation_df(job_list)


if __name__ == "__main__":
    test()
    
    
    
    
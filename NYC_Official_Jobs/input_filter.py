import numpy as np
import pandas as pd

def filter_the_job(df,keyword):
    """
    input a datafame and a keyword, return all the job that related to this keyword
    return type: datafame
    """

    keyword = keyword.lower()
    keyword1 = keyword[0].upper() + keyword[1:]
    filtered = df[df.apply(lambda x:(keyword in x[u"Business Title"])or(keyword1 in x[u"Business Title"])or(keyword in df[u"Job Description"])or(keyword1 in df[u"Job Description"])  ,axis =1)]
    return filtered


def main():
    """
    test the functions
    """
    kwd = raw_input("Please input a keyword of the job you interested in: ")
    job_data = pd.read_csv("NYC_Jobs.csv")
    interested_jobs = filter_the_job(job_data,kwd)
    output_feature = ['Job ID','Agency','Business Title','Civil Service Title']
    print interested_jobs[output_feature].head()


if __name__ == "__main__":
    main()

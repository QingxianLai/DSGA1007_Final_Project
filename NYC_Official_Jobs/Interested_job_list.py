__author__ = 'LaiQX'
import pandas as pd
from Job_list_overall import Job_data
from input_filter import filter_the_job
from map_of_location import plot_the_location_map, plot_one_job_location
from jobDescription import show_job_infomation_s,show_job_infomation_df
from exception_list import invalid_ID_Exception


class interested_job_list(Job_data):

    def __init__(self, df, kwd):
        self.data = df
        self.keyword = kwd
        self.attribute = df.columns.get_values()   #this is a numpy ndarray

    def map_of_locations(self,num,):
        plot_the_location_map(self.data,num,self.keyword)

    def filter_kwd(self):
        self.data = filter_the_job(self.data,self.keyword)

    def preview_data(self, n=30):
        if len(self.data) <= n:
            n = len(self.data)
        print self.data.iloc[:n, :]

    def show_job_list(self):
        show_job_infomation_df(self.data)

    def _verify(self, job_id):
        if not(job_id in  self.data.loc[:,'Job ID'].values):
            raise invalid_ID_Exception

    def select(self, job_id):
        self._verify(job_id)            # if invalid, raise an exception
        selected_job = self.data[self.data['Job ID']==job_id].iloc[0,:]
        return job(selected_job)

    def __repr__(self):
        return "Job list corresponding to keyword '{}'".format(self.keyword)


class job:
    def __init__(self,job):
        self.data = job                 # job should be a pandas Series with attributes as its index
        self.id = job['Job ID']
        self.title = job['Business Title']

    def description(self):
        show_job_infomation_s(self.data)

    def location(self):
        plot_one_job_location(self.id)

    def __repr__(self):
        return "Detailed information about job '{}'".format(self.title)


def test_class():
    df = pd.read_csv("../NYC_Jobs.csv")
    keyword = 'manager'
    job_list = filter_the_job(df,keyword)
    job_list = interested_job_list(job_list,keyword)
    print job_list
    job_list.map_of_locations(30)
    id= 170881
    job_i = job_list.select(id)
    print job_i
    job_i.location()


if __name__ == "__main__":
    test_class()


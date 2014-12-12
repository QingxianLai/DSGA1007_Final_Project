import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pieplot import plot_Degree
from barplot import *
from input_filter import filter_the_job
from Dataloading import Clean_df

class Job_data:

    def __init__(self, df):
        self.data = df
        self.attribute = df.columns.get_values()   #this is a numpy ndarray

    def degree_pie_plot(self):
        plot_Degree(self.data)

    def top_demanding_jobs(self):
        plot_DemandJob(self.data)

    def nun_of_job_by_date(self):
        plot_NumJob_byDate(self.data)

    def top_ten_agency(self):
        plot_numPosition(self.data)

    def preview_data(self):
        index = np.random.choice(len(self.data),size=50)
        print self.data.iloc[index, :]

    def salary_range(self):
        show_salary_range(self.data)

    def __repr__(self):
        return "NYC_OFFICIAL_JOB_DATASET Object"

    def corralation_level_salary(self):
        pass  # TODO: write this function


def class_test():
    df = pd.read_csv("../NYC_Jobs.csv")
    df = Clean_df(df)
    nyc_job_data = Job_data(df)
    nyc_job_data.degree_pie_plot()
    nyc_job_data.top_demanding_jobs()
    nyc_job_data.top_ten_agency()
    nyc_job_data.num_of_job_by_date()
    nyc_job_data.preview_data()
#    keyword = 'manager'
#    job_list = filter_the_job(df, keyword)


if __name__ == "__main__":
    class_test()

__author__ = 'LaiQX'

import numpy as np
import pandas as pd


def main():


    Job_data = safely_input()
    Job_data = clean_data()
    Overall_analysis(Job_data)
    Job_list = filter_data(Job_data)
    Interested_jobs_anaysis(Job_list)
    show_certain_job(Job_list)



if __name__=="__main__":
    main()





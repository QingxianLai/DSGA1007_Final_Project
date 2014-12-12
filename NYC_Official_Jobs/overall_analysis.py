__author__ = 'LaiQX'
import sys
from exception_list import *
from Job_list_overall import Job_data
from input_filter import filter_the_job

def overall_analysis(df):
    """

    :param df:
    :return:
    """

    df_obj = Job_data(df)

    print "=================  NYC Official Job Analysis  =============================="
    print ""
    print "You can choose to learn more about the whole dataset: "
    print " <a>  :  pie plot show the percentage of degree requirement"
    print " <b>  :  bar plot show ten most hiring agency"
    print " <c>  :  bar plot show the most demanded positions"
    print " <d>  :  line plot of the number of job vs date"
    print " <e>  :  show the corralation b/t level and salary"
    print " <f>  :  get a preview about the whole dataset"
    print " <g>  :  search for a keyword about jobs you interested in"
    print " <q>  :  quit the prgram"
    print ""
    print "============================================================================"


    while 1:
        option = option_input()
        operation(df_obj,option)



def option_input():
    key = raw_input("your_choose: ")
    options = list('abcdefgq')
    if not(key in options):
        raise wrong_option_exception
    if key == 'q':
        print 'program shut down! bye!'
        sys.exit()
    return key

def operation(df,key):
    if key == 'a':
        df.degree_pie_plot()
    if key == 'b':
        df.top_ten_agency()
    if key == 'c':
        df.top_demanding_jobs()
    if key == 'd':
        df.num_of_job_by_date()
    if key == 'e':
        pass
    if key == 'f':
        df.preview_data()
    if key == 'g':
        seach_keyword(df.data)
        break

def search_keyword(df):
    keyword = raw_input("please input a keyword of the job you interested in: \n")
    job_list = filter_the_job(df, keyword)
    if len(job_list) == 0:
        raise no_related_jobs_exception




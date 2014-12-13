__author__ = 'LaiQX'
import sys
from exception_list import *
from Interested_job_list import interested_job_list, job
from input_filter import filter_the_job
import pandas as pd
from Dataloading import Clean_df


def job_list_analysis(df,kwd):
    """
    This function used to display an interactive system letting the user to learn more
    about his interested jobs. Detail instructions will be shown at the
    beginning of the program.

    argument
    =========
    df: a dataframe

    return
    ======

    """

    df = interested_job_list(df,kwd)          # turn the data frame into a Interested job list object
    df.show_job_list()

    print_list_operator(df.keyword)

    while 1:
        try:
            key = option_input()
            if key == 'm':
                df.map_of_locations(75)
            if key == 'a':
                df.degree_pie_plot()
            if key == 'b':
                df.top_ten_agency()
            if key == 'c':
                df.top_demanding_jobs()
            if key == 'd':
                df.num_of_job_by_date()
            if key == 'e':
                skill_list = df.high_demand_skill()
                print "top demanded skills: "
                print skill_list
            if key == 'g':
                cjob = select_a_job(df)
                view_job_info(cjob)
                df.show_job_list()
                print_list_operator(df.keyword)
        except wrong_option_exception:
            print "invalid option, please select from [m,a,b,c,d,e,f,g] or input 'q' to quit: "


def print_list_operator(kwd):
    print ""
    print "================================  keyword:{}  ==============================".format(kwd)
    print ""
    print "                 You can choose to learn more about this job list: "
    print "              <m>  :  draw a map to show all the job location"
    print "              <a>  :  pie plot show the percentage of degree requirement"
    print "              <b>  :  bar plot show the most hiring agency"
    print "              <c>  :  bar plot show the most demanded positions"
    print "              <d>  :  line plot of the number of job vs date"
    print "              <e>  :  show the most demanded skills of all the related jobs"
    print "              <g>  :  select a job id to get more information about that job"
    print "              <q>  :  quit the program"
    print ""
    print "==========================================================================================="




def option_input():
    """
    get the option selected by user, and verify it.

    Return
    ======
    return a verified option

    """
    key = raw_input("your_choose: ")
    options = list('mabcdefgq')
    if not(key in options):
        raise wrong_option_exception
    if key == 'q':
        print 'program shut down! bye!'
        sys.exit()
    return key


def select_a_job(df):
    while 1:
        try:
            job_id = raw_input("please input a Job ID of which you want to learn details: \n")
            if job_id == 'b':
                break
            id = select_id_job(job_id)
            Job = df.select(id)
            break
        except invalid_ID_Exception:
            print "job id not exist in this list, please try again or type 'b' to go back"
        except id_not_int_exception:
            print "job id should be integer, please try again"
    return Job                 # as described in class, this returns an object



def select_id_job(id_str):
    try:
        id = int(id_str)
    except:
        raise id_not_int_exception
    return id


def view_job_info(Job):

    print "successfully select job: {}".format(Job.id)

    print ""
    print "================================  jb ID:{}  ==============================".format(Job.id)
    print ""
    print "                 You can choose to learn more about this job: "
    print "              <a>  :  show the detailed information"
    print "              <b>  :  draw the map of its location"
    print "              <q>  :  back to the job list"
    print ""
    print "==========================================================================================="

    while 1:
        try:
            key = job_key_input()
            if key == 'a':
                Job.description()
            if key == 'b':
                Job.location()
            if key == 'q':
                print "Go back to the job list: >>> \n \n >>>"
                break
        except wrong_option_exception:
            print "invalid option, please select from [a,b,q]: "


def job_key_input():
    """
    get the option selected by user, and verify it.

    Return
    ======
    return a verified option

    """
    key = raw_input("your_choose: ")
    options = list('abq')
    if not(key in options):
        raise wrong_option_exception
    return key


def test():
    df = pd.read_csv("../NYC_Jobs.csv")
    df = Clean_df(df)
    kwd = "data"
    job_list = filter_the_job(df,kwd)
    job_list_analysis(job_list,kwd)


if __name__ == "__main__":
    try:
        test()
    except KeyboardInterrupt:
        sys.exit()
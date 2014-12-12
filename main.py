__author__ = 'LaiQX'



from NYC_Official_Jobs import *

def main():

    raw_data = safely_input()
    print "dataset loaded successfully >>>"
    print ">>>",
    Job_data = Clean_df(raw_data)
    print "data cleaned >>>"
    job_list = overall_analysis(Job_data)
#    Job_list = filter_data(Job_data)
#    Interested_jobs_anaysis(Job_list)
#    show_certain_job(Job_list)



if __name__=="__main__":
    main()





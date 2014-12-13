__author__ = 'LaiQX'

import pandas as pd
from NYC_Official_Jobs import *
import sys


def main():

    raw_data = safely_input()
    print "dataset loaded successfully >>>"
    print ">>>",
    job_data = Clean_df(raw_data)
    print "data cleaned >>>"
    job_list,keyword = overall_analysis(job_data)
    "Matching >>>"
    if type(job_list) == pd.DataFrame:
        job_list_analysis(job_list,keyword)
    elif type(job_list) == pd.Series:
        one_job_info(job_list)


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt,EOFError):
        sys.exit()





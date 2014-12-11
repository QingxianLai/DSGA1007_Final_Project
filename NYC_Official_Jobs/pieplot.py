from jobDescription import degreeDict
from pylab import *


def plot_Degree(dataframe):
    """plot a pie that shows the proportion of jobs that need a specific level of education degree"""
    degree=degreeDict(dataframe)
    bach=degree['Bachelor']
    master=degree['Master']
    others=degree['High School or others non-degree']
    # make a square figure and axes
    figure(2, figsize=(6,6))
    ax = axes([0.1, 0.1, 0.8,0.8])
    # The slices will be ordered and plotted counter-clockwise.
    labels = 'At least \n a Bachelor degree', 'At least\n   A Master \n degree','Others:\nHigh school \nDiploma or \nSome experiences '
    fracs = [bach, master, others]
    explode=(0.05, 0.05, 0.05)
    pie(fracs, explode=explode, labels=labels,autopct='%1.1f%%', shadow=True, startangle=90)
    title('Minimum Degree Requirement', bbox={'facecolor':'1.0', 'pad':5})
    show()


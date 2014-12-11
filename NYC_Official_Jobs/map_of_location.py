# -*- coding: utf-8 -*-
"""
Created on Sat Dec  6 22:16:51 2014

@author: LaiQX
"""

import pandas as pd
from input_filter import filter_the_job
from cStringIO import StringIO
from PIL import Image
import urllib


def plot_the_location_map(df,geo_map,num):
    df = df[['Job ID','Business Title']]
    
    #===========marker======================================================
    # size:  {tiny, mid, small} 
    # color: {black, brown, green, purple, yellow, blue, gray, orange, red, white} 
        
    marker_start = "markers=color:red"
    marker = marker_start
    for i in range(num):
        job_id = df.iloc[i,0]
        lat = geo_map.loc[job_id,'lat']
        lng = geo_map.loc[job_id,'lng']
        marker = marker+"%7C{},{}".format(lat,lng)     
    
    #==========parameters======================================================
    url_start = "http://maps.googleapis.com/maps/api/staticmap?"
    #center_point = "center=%4.5f,%4.5f" % (loc_point[0],loc_point[1])          # New+York+City
    center_point = 'center=New+York+City'    
    size = "size=800x800"
    zoom = "zoom=11"
    sensor = "sensor=false"    
    maptype = "maptype=terrain"  #satellite ; terrain
    c = '&'
    url = url_start+center_point+c+size+c+zoom+c+marker+c+maptype+c+sensor

    #=======plot================================================================   
    buffer = StringIO(urllib.urlopen(url).read())
    image = Image.open(buffer)
    image.save('location_map.png')


def main():
    df = pd.read_csv("NYC_Jobs.csv")
    keyword = 'manager'
    job_list = filter_the_job(df,keyword)
    id_geo_map = pd.read_csv('id_geo_location.csv',index_col='Job ID')
    num=79       # maximum : 79
    plot_the_location_map(job_list,id_geo_map,num)
    print "hello world"
    
if __name__=="__main__":
    main()
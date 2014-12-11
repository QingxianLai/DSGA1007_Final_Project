# -*- coding: utf-8 -*-
"""
Created on Sun Dec  7 14:51:24 2014

@author: LaiQX
"""

import pandas as pd
import re
import googlemaps


def clean_the_location(IBW_df):
    """
    clean the location to add some city information 
    """
    IBW_df = IBW_df[IBW_df['Work Location']!='Not Used']
    IBW_df['NewLocation']=0
    n = IBW_df.columns.get_loc('Work Location')
    t = IBW_df.columns.get_loc('NewLocation')
    a = IBW_df.columns.get_loc('Agency')
    for i in range(len(IBW_df)):
        location = IBW_df.iloc[i,n]
        agency = IBW_df.iloc[i,a]
        
        # correct some location that cannot be parsered by googlemap
        if location.find('280 Broadway') != -1:
            newlocation = '280 Broadway, New York, NY'
            IBW_df.iloc[i,t] = newlocation
            continue

        if location.find('Clove Lake, Faber') != -1:
            newlocation = 'Clove Lakes Park 1150 Clove Rd Staten Island, New York, NY'
            IBW_df.iloc[i,t] = newlocation
            continue

        if agency.find('HOUSING AUTHORITY') != -1:
            newlocation = '175 Eldridge St New York, New York, NY'
            IBW_df.iloc[i,t] = newlocation
            continue

        if agency.find('ENVIRONMENT PROTECTION') != -1:
            newlocation = '105 Mill Rd Staten Island, New York, NY'
            IBW_df.iloc[i,t] = newlocation
            continue

        if agency.find('CORRECTION') != -1:
            newlocation = '75-20 Astoria Blvd. East Elmhurst, New York, NY'
            IBW_df.iloc[i,t] = newlocation
            continue

        if agency.find('HEALTH/MENTAL HYGIENE') != -1:
            newlocation = '42-09 28th St Long Island City, NY'
            IBW_df.iloc[i,t] = newlocation
            continue

        if agency.find('PARKS & RECREATION') != -1:
            newlocation = '830 5th Ave New York, NY'
            IBW_df.iloc[i,t] = newlocation
            continue

        if agency.find('TECH & TELECOMM') != -1:
            newlocation = '75 Park Pl New York, NY'
            IBW_df.iloc[i,t] = newlocation
            continue
        
        if location.find('48-34 35Th St., Queens') != -1:
            newlocation = '48-39 35th St, Long Island City, New York, NY'
            IBW_df.iloc[i,t] = newlocation
            continue

        if location.find('1 Metro Tech, Brooklyn') != -1:
            newlocation = '1 MetroTech Roadway Brooklyn, New York, NY'
            IBW_df.iloc[i,t] = newlocation
            continue 

        if location.find('55 Water St') != -1:
            newlocation = '55 Water Street, New York, NY'
            IBW_df.iloc[i,t] = newlocation
            continue 
 
        if location.find('470 Vanderbilt Ave') != -1:
            newlocation = '470 Vanderbilt Ave, Brooklyn, New York, NY'
            IBW_df.iloc[i,t] = newlocation
            continue 

        if location.find('32-02 Queens Blvd') != -1:
            newlocation = '32-2 Queens Blvd, Long Island City, New York 11101'
            IBW_df.iloc[i,t] = newlocation
            continue  

        if location.find('60 Bay St. S.I') != -1:
            newlocation = '60 Bay St, Staten Island, New York, NY'
            IBW_df.iloc[i,t] = newlocation
            continue   

        if location.find('1 Bay St') != -1:
            newlocation = '1 Bay Street, Staten Island, New York, NY'
            IBW_df.iloc[i,t] = newlocation
            continue 

        if location.find('65-10 Douglaston Pkwy') != -1:
            newlocation = '65-11 Douglaston Pkwy, Flushing, New York, NY'
            IBW_df.iloc[i,t] = newlocation
            continue

        if location.find('P.O. Box 41, Chelsea') != -1:
            newlocation = '41 Chelsea, New York, NY'
            IBW_df.iloc[i,t] = newlocation
            continue

        if location.find('9 Bond Street') != -1:
            newlocation = '9 Bond St, New York, 10001'
            IBW_df.iloc[i,t] = newlocation
            continue

        if location.find('Family Services') != -1:
            newlocation = '2029 2nd Ave New York, NY'
            IBW_df.iloc[i,t] = newlocation
            continue
        
        
        # change endings to the standard "New York, NY"
        if location.find('N.Y.') != -1:
            newlocation = location[:location.find('N.Y.')-1]+' New York, NY'
            newlocation = re.sub(' +',' ',newlocation)
            IBW_df.iloc[i,t] = newlocation
            continue
        if location.find('New York') != -1:
            newlocation = location[:location.find('New York')-1]+'  New York, NY'
            newlocation = re.sub(' +',' ',newlocation)
            IBW_df.iloc[i,t] = newlocation
            continue
        if location.find('Ny') != -1:
            newlocation = location[:location.find('Ny')-1]+'  New York, NY'
            newlocation = re.sub(' +',' ',newlocation)
            IBW_df.iloc[i,t] = newlocation
            continue
        if location.find('NY') != -1:
            newlocation = location[:location.find('NY')-1]+'  New York, NY'
            newlocation = re.sub(' +',' ',newlocation)
            IBW_df.iloc[i,t] = newlocation
            continue
        newlocation = location + '  New York, NY'
        newlocation = re.sub(' +',' ',newlocation)
        IBW_df.iloc[i,t] = newlocation
    return IBW_df



def get_geocode_information(df):
    location_code_map = {}
    t = df.columns.get_loc('NewLocation')
    n = df.columns.get_loc('Business Title')
    d = df.columns.get_loc('Job ID')
    a = df.columns.get_loc('Agency')
    api_keys = 'AIzaSyA0M0zkr9nt6obKXja2ng0TbDOrbLK7POQ'
    gmaps = googlemaps.Client(key=api_keys)
    for i in range(len(df)):
        job_id = df.iloc[i,d]
        location = df.iloc[i,t]
        while 1:
            gcode = gmaps.geocode(location)
            if (gcode[0]['formatted_address'] !='New York, NY, USA')and(len(gcode)==1):
                break
            print df.iloc[i,a]
            print location
            print df.iloc[i,n]
            location = raw_input('please input an alternative address: ')
            df.iloc[i,t] = location
        address = gcode[0]['formatted_address']
        latitude = gcode[0]['geometry']['location']['lat']
        longitude = gcode[0]['geometry']['location']['lng']
        location_code_map[job_id] = [address,latitude,longitude]
    geo_df = pd.DataFrame.from_dict(location_code_map,orient='index')
    geo_df.columns = ['address','lat','lng']
    geo_df.index.name = 'Job ID'
    return geo_df
        

        

def main():
    df = pd.read_csv("NYC_Jobs.csv")
    df = df[['Job ID','Business Title','Agency','Work Location']].drop_duplicates()
    df = clean_the_location(df)
    geo_df = get_geocode_information(df)
    geo_df.to_csv('id_geo_location.csv')





if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt,EOFError):
        pass
    
    
    
























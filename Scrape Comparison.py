# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 13:26:04 2022

@author: saransh.s
"""

#import json
import os
import pandas as pd
pd.set_option("display.max_columns", None)
from bs4 import BeautifulSoup
#from urllib.request import urlopen
import requests
os.chdir(r"D:\Personal\Football Analysis\Analysis\Player Analysis") 
scrape_url = "https://fbref.com/en/stathead/player_comparison.cgi?request=1&sum=1&dom_lg=1&player_id1=e46012d4&p1yrfrom=2017-2018&p1yrto=2022-2023&player_id2=a167537f&p2yrfrom=2017-2018&p2yrto=2022-2023"
stats = ['standard_stats','shooting_stats','passing_stats','passing_types_stats',
         'gca_stats','defense_stats','possession_stats','playing_time_stats',
         'misc_stats']
#for i in stats:
 #   print('df'+'_'+str(i) + '.csv')
try:
    os.mkdir("final_data")
 #   os.mkdir("complete_data") 
except OSError:
    print("Folder Results Already Exists")
    
os.chdir(r"D:\Personal\Football Analysis\Analysis\Player Analysis\final_data")   
def get_df(url):
    content = requests.get(url)
    html_content = content.content
    soup=BeautifulSoup(html_content,'html.parser')
    for i in stats:
        table = soup.find('table',id = i)
        df = pd.read_html(str(table))
        data = df[0]
        data.columns = data.columns.droplevel()
        df=data.apply(pd.to_numeric, errors="ignore")
        #file_name = str(i) + '_Pedri' + '.csv'
        file_name = str(i) + '.csv'
        df.to_csv(file_name)
        
get_df(scrape_url)
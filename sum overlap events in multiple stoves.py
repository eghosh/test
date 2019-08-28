# -*- coding: utf-8 -*-
"""
SCRIPT CHECKS FOR OVERLAPPING SUM EVENTS
Created on Wed May 15 12:56:15 2019

@author: emily
"""

import pandas as pd
import sqlite3

hhstove = [['\'HH004\'','\'LPG2%\''], ['\'HH005\'','\'LPG2%\''], ['\'HH007\'','\'LPG4%\''],['\'HH008\'','\'LPG4%\''],['\'HH009\'','\'LPG2%\''], ['\'HH012\'','\'LPG2%\''], ['\'HH017\'','\'LPG2%\''],['\'HH026\'','\'LPG2%\''],['\'HH030\'','\'LPG4%\'']]
df = pd.DataFrame()

for i in hhstove:

    commhh = i[0]       
    algorithm = '\'bimodal\''
    stove = i[1]
    sql = 'SELECT commhh, stove, algorithm, cooking_start, cooking_end, cooking_duration, cooking_duration_hrs, start_temp, max_temp, end_temp FROM V01__check_duplicates WHERE commhh = ' +  commhh + ' and algorithm = ' + algorithm + ' and stove like ' + stove + ' GROUP BY commhh, stove, algorithm, cooking_start, cooking_duration  ORDER BY 4 asc'
    
    meta_conn = sqlite3.connect('C:/Users/emily/Dropbox/CCAC GACHIE FIELDWORK/Analysis/SUMS Program Results/SUMS 30 min join events - 2019June24.sql3')
    df1 = pd.read_sql_query(sql,meta_conn)
    df1['Overlap'] = None
    
    pd.set_option('mode.chained_assignment', None) # temporary disables SettingwithCopyWarning
    for x in range(0,len(df1.index)-1):
        if df1['cooking_start'][x+1] < df1['cooking_end'][x]:
            diff1 = df1['max_temp'][x] - df1['start_temp'][x]
            diff2 = df1['max_temp'][x+1] - df1['start_temp'][x+1]
            if diff1 > diff2:
                df1['Overlap'][x+1] = 1
            else:
                df1['Overlap'][x] = 1
    check1 = df1.copy()
    pd.set_option('mode.chained_assignment', 'raise') # enables SettingwithCopyWarning
    
    remove = []
    for x in range(0,len(df1.index)):
        if df1['Overlap'][x] == 1:
            remove.append(x)
    
    df1.drop(df1.index[remove], inplace=True)
    df1.drop(['Overlap'], axis=1, inplace=True)
    #df1 = df1.reset_index(drop=True)
    
    algorithm = '\'sd\''
    sql = 'SELECT commhh, stove, algorithm, cooking_start, cooking_end, cooking_duration, cooking_duration_hrs, start_temp, max_temp, end_temp FROM V01__check_duplicates WHERE commhh = ' +  commhh + ' and algorithm = ' + algorithm + ' and stove like ' + stove + ' GROUP BY commhh, stove, algorithm, cooking_start, cooking_duration  ORDER BY 4 asc'
    
    df2 = pd.read_sql_query(sql,meta_conn)
    df2['Overlap'] = None
    
    pd.set_option('mode.chained_assignment', None) # temporary disables SettingwithCopyWarning
    for x in range(0,len(df2.index)-1):
        if df2['cooking_start'][x+1] < df2['cooking_end'][x]:
            diff1 = df2['max_temp'][x] - df2['start_temp'][x]
            diff2 = df2['max_temp'][x+1] - df2['start_temp'][x+1]
            if diff1 > diff2:
                df2['Overlap'][x+1] = 1
            else:
                df2['Overlap'][x] = 1
    check2 = df2.copy()
    pd.set_option('mode.chained_assignment', 'raise') # enables SettingwithCopyWarning
    
    remove = []
    for x in range(0,len(df2.index)):
        if df2['Overlap'][x] == 1:
            remove.append(x)
    
    df2.drop(df2.index[remove], inplace=True)
    df2.drop(['Overlap'], axis=1, inplace=True)
    #df2 = df2.reset_index(drop=True)
    
    algorithm = '\'temp\''
    sql = 'SELECT commhh, stove, algorithm, cooking_start, cooking_end, cooking_duration, cooking_duration_hrs, start_temp, max_temp, end_temp FROM V01__check_duplicates WHERE commhh = ' +  commhh + ' and algorithm = ' + algorithm + ' and stove like ' + stove + ' GROUP BY commhh, stove, algorithm, cooking_start, cooking_duration  ORDER BY 4 asc'
    
    df3 = pd.read_sql_query(sql,meta_conn)
    df3['Overlap'] = None
    
    pd.set_option('mode.chained_assignment', None) # temporary disables SettingwithCopyWarning
    for x in range(0,len(df3.index)-1):
        if df3['cooking_start'][x+1] < df3['cooking_end'][x]:
            diff1 = df3['max_temp'][x] - df3['start_temp'][x]
            diff2 = df3['max_temp'][x+1] - df3['start_temp'][x+1]
            if diff1 > diff2:
                df3['Overlap'][x+1] = 1
            else:
                df3['Overlap'][x] = 1
    check3 = df3.copy()
    pd.set_option('mode.chained_assignment', 'raise') # enables SettingwithCopyWarning
    
    remove = []
    for x in range(0,len(df3.index)):
        if df3['Overlap'][x] == 1:
            remove.append(x)
    
    df3.drop(df3.index[remove], inplace=True)
    df3.drop(['Overlap'], axis=1, inplace=True)
    #df3 = df3.reset_index(drop=True)
    
    df = pd.concat([df,df1,df2,df3])
    df = df.reset_index(drop=True)

next
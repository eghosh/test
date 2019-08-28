# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 16:35:50 2018

@author: emily
"""
import numpy as np
import pandas as pd
import scipy
import glob
import os
import re
import yaml
import argparse
import sqlite3
import csv
import sys
from datetime import datetime, timedelta

#from win32com.client import Dispatch
 
#L = Dispatch('LEAP.LEAPApplication')   

#L.ActiveArea = "Freedonia"
#L.ActiveView = "Results"

#setscenario = "Reference"
#typebranch = 3 #"Transformation Process"

#if L.Scenarios(setscenario):
#    for b in L.branches:
#        if b.branchtype == typebranch:
#            for y in range(L.baseyear, L.endyear):
#                print "year", y, " ", b.name, " ", b.Variable("Outputs by Output Fuel").Value(y, "Gigajoule"), "GJ"

"""
def insert_into_dataframe(df, value, row, col, fill = 0):
    
    new_row = df.iloc[0].copy()
    new_row[:] = fill
    res = df.append(new_row, ignore_index=True)

use_temp = np.array([[2367, 219, 219],[2445, 284, 333], [3009, 2367, 1576]])

row_id = 0
row = use_temp[row_id]
end_row = use_temp[row_id+1]

test_ind = min(row[row > 0])
test_ind_end = min(end_row[row == test_ind])
non_mtching = (((row - test_ind) > 15.0) | (abs(end_row - test_ind_end) > 15.0)) & (row > 0)

print test_ind
print test_ind_end
print row - test_ind
print row - test_ind > 15.0
print end_row - test_ind_end
print end_row - test_ind_end > 15.0
print non_mtching.index


for alg in non_mtching.index[non_mtching]:
    use_temp = insert_into_dataframe(use_temp, 0, row_id, alg)
    use_temp = insert_into_dataframe(use_temp, 0, row_id, alg)
              

class Student(object):
    #Returns a ```Student``` object with the given name, branch and year.

    
    def __init__(self, name, branch, year):
            self.name = name
            self.branch = branch
            self.year = year
            print("A student object is created.")

    def print_details(self):
       
    #    Prints the details of the student.
        
        print("Name:", self.name)
        print("Branch:", self.branch)
        print("Year:", self.year)
        
std1 = Student('Kushal','CSE','2005')

std1.print_details()

#file_path = 'C:\\Users\\emily\\Desktop\\TEmP\\epa\\test\\GA36\\SA203_2016-04-29_GA36_LPG.csv'
file_path = 'C:\\Users\\emily\\Desktop\\TEmP\\epa\\test\\Sa 16_2017-12-20_HU32_LPG.csv'

with open(file_path, 'rb') as f:
    f.readline()
    test = f.readline().split(',')
    print test[0]
    teststart = pd.Timestamp(test[0])
    start = pd.Timestamp(f.readline()[:15])
    f.seek(-2, os.SEEK_END)
    while f.read(1) != b'\n':
        f.seek(-2, os.SEEK_CUR)
    end = pd.Timestamp(f.readline()[:15])

print teststart
print start
print end


null_ind = [ 0,  1,  7, 68, 69]
null_ind_diff = np.diff[null_ind]
print null_ind_diff

test = zip(null_ind, null_ind[1:])
cut_l = 0

if null_ind[0] == 0:
    for p1, p2 in test:
        #print p1, ' ', p2
        #print p2-p1
        if p2-p1 == 1:
            cut_l = p2
            #print 'cut_l: ', cut_l
        else:
            continue

# stop when p2 - p2 != 0

cut_l = 0 

if null_ind[0] == 0:
    for x in null_ind:
        print x
        if x - cut_l == 1:
            cut_l = x

print 'cut_l: ' , cut_l

#data = pd.read_csv(file_path, encoding='latin1', usecols=[0,1], parse_dates=[0], names=[STATIC_STRS.TIME, STATIC_STRS.TEMP], header=0, na_values=['blank'], infer_datetime_format = True)
sig_data = pd.read_csv('C:\Users\emily\Desktop\TEmP\Book3.csv', na_values=['blank'])

print sig_data
print ' '

null_ind = np.where(pd.isnull(sig_data))[0]

diff = np.diff(null_ind)

#start from beginning to when the number isn't null
cut_l = 0
cut_h = len(sig_data)

if null_ind[0] == 0:
    # if there is only one blank and it is at the start
    if len(diff) == 0:
        cut_l = 1
    else:
        multi_nulls = np.argmax(diff>1)
        # if there are multple blanks at the start
        if multi_nulls == 0:
            cut_l = len(diff)+1
        # if there are multiple blanks in different parts of the data file
        else:
            cut_l = np.argmax(diff>1)+1
        
if null_ind[-1]+1 == cut_h:
    # if there is only one blank and it is at the end
    if len(diff) == 0:
        cut_h = null_ind[-1]
    else:
        rev_null_diff = diff[::-1]
        multi_nulls = np.argmax(rev_null_diff>1)
        lastnull = len(rev_null_diff) - multi_nulls
        # if there are multiple blanks at the end
        if multi_nulls == 0 and len(diff) > 0:
            if null_ind[-2]+2 == cut_h:
                cut_h = null_ind[-1] - lastnull
        # if there is only one blank at the end and blanks throughout the file
            else:
                cut_h = null_ind[-1]
        # if there are multiple blanks at the end and throughout the file
        else:
            cut_h = null_ind[lastnull]

sig_data = sig_data.iloc[cut_l:cut_h]
#sig_data = sig_data.reset_index(drop=True)

print sig_data
---
treat_type = x.treat_type.item()
treat_code = x.treat_code.item()
print treat_code


file_path = 'C:\Users\emily\Documents\GitHub\SUMs\Digit_HHIDs_trtmt-ctrl_Samuha.csv'
commhh = 'NN97'

f = pd.read_csv(file_path,header=0, names=['HHID', 'treat_type', 'treat_code'])
f.HHID = map(lambda x: x.upper(), f.HHID)
treatment = {}
treatment = f.loc[f.HHID == commhh]
if len(treatment) ==0:
    treatment = treatment.append({'HHID': commhh, 'treat_type':'NotFound','treat_code':'NotFound'}, ignore_index=True)
    print treatment
print str(treatment['treat_type'].item())
----
sig_data = [0, 1, 2, 3, 4, 5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
null_ind = [17, 18, 19, 25]
null_diff = [1, 1, 93600]


for index, value in enumerate(null_diff):
    if value == 1:
        if index == 0:
            sig_data[null_ind[index]] = sig_data[null_ind[index]-1]
            sig_data[null_ind[index+1]] = sig_data[null_ind[index]-1]
        else:
            sig_data[null_ind[index+1]] = sig_data[null_ind[index]-1]


# re-index files ending in .p
# create metadata file based on .p files

n_files = 4
skipped_file = 0

for i in range(n_files):
    print 'n_files', n_files
    print 'i', i
    if skipped_file == 1:
        # reset skipped file
        skipped_file = 0 
        # jump to next file
        continue
    for j in range(i+1, n_files):
        print 'j', j
        if i == j-1:
            # delete file from SUMS_md
            skipped_file = 1
            print skipped_file


#test pandas group by https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.groupby.html

df = pd.DataFrame({'Animal' : ['Falcon', 'Falcon','Parrot', 'Parrot'],'Max Speed' : [380., 370., 24., 26.]})
print df
grouped_data = df.groupby(['Animal']).mean()
print grouped_data


    
file_path = 'C:\\Users\\emily\\Desktop\\TEmP\\CCAC Gachie\\test\\test\\T025_2018-11-20_HH012_KCJ.csv'

def read_csv_with_defaults(file_path):
    #Reads in a csv file using pandas, applying default arguments
    # Currently, this function assumes that the first column is the time data, second is temperature.
    # Other colunns are dropped (though could be adjusted with the usecols argument)
    data = pd.read_csv(file_path, encoding='latin1', usecols=[0], parse_dates=[0], names=['TIME'], header=0, na_values=['blank'], infer_datetime_format = True)
    return data

test = read_csv_with_defaults(file_path)
test['TIME'] = pd.to_datetime(test.TIME)
#test['situation'] = false

cutoff = timedelta(hours=1)
wrong = 0
wrong_files = []

# checks to see if any dates are out of sequence
for i in range(1,len(test)):
    if (test['TIME'][i] - test['TIME'][i-1]) > cutoff: wrong = wrong + 1

# list of files with dates that are out of sequence
if wrong > 0: wrong_files.append(file_path)

print ('Files out of sequence: %s' % wrong_files)


# Extract filename, strip extension, split on underscore
elements = os.path.basename(file_path).split('.')[0].split('_')
metadata = {}
metadata['ST'] = elements[-1] # Stove type
if ambient:
    cchh = elements[0]
else:
    cchh = elements[-2]

# Replaces any spaces in the community/household name
cchh = cchh.replace(" ","")

metadata['CC'] = cchh[:2] # Community code
metadata['HH'] = cchh[2:] # Household code

# Replaces any spaces in the SUMS ID
elements[0] = elements[0].replace(" ","")
  
metadata['ID'] = elements[0] # SUMS ID
return metadata


fname_test_path = 'processed_data\\*_T191_HH030_LPG4(BL)_2018-10-17_to_2019-04-17.p'
fnames = glob.glob(fname_test_path)
fnames_dates = []
try: 
    if fnames[0]:
        for i, f in enumerate(fnames):
            fnames_dates.append(os.stat(f).st_mtime)
except:
    print('no hello')
    
fname_index = max(xrange(len(fnames_dates)), key=fnames_dates.__getitem__)
print(fnames[fname_index])

import win32com.client
LEAP = win32com.client.Dispatch("Leap.LEAPApplication")
LEAP.ActiveView = "Results"
"""        

hhstove = [['\'HH004\'','\'LPG2%\''], ['\'HH005\'','\'LPG2%\''], ['\'HH007\'','\'LPG4%\''],['\'HH008\'','\'LPG4%\''],['\'HH009\'','\'LPG2%\''], ['\'HH012\'','\'LPG2%\''], ['\'HH017\'','\'LPG2%\''],['\'HH026\'','\'LPG2%\''],['\'HH030\'','\'LPG4%\'']]

for i in hhstove:
    print i[0]
    print i[1]
next
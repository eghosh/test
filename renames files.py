# -*- coding: utf-8 -*-
"""
SCRIPT FIXES FILE ERRORS
Created on Mon May 20 18:07:14 2019

@author: emily
"""

import os
import sys

# Input file path
fname = 'C:\\Users\\emily\\Desktop\\TEmP\\epa\\test\\Kullu All Files No Ambient Fixed'

# Lists all of the files in the directory, broken down by file name elements (commhh, sumsid, stove type, data collection date)
# Also lists all stove types indicated in the file names
stovelist = []
for path, subdirs, files in os.walk(fname):
    for f in files:
        elements = f.split('.')[0].split('_')
        if elements[3] not in stovelist: stovelist.append(elements[3])
        print elements

print stovelist

# Asks user if they want to continue fixing the file names
user_input = raw_input('Continue fixing files (Y/N)? ')
if (user_input == "N") or (user_input == "n") or (user_input == "no") or (user_input == "No") or (user_input == "NO"):
    sys.exit(1)

# Rearranges the order of the elements in the file name and renames the file name
for path, subdirs, files in os.walk(fname):
    for f in files:
        elements = f.split('.')[0].split('_')
        
        # Checks that the SUMS ID is 5 characters, otherwise adds a '0'
        if len(elements[0]) < 5:
            ID = elements[0] 
            area = ID[:2]
            idno = ID[2:]
            elements[0] = area + "0" + idno

        # If the SUMS ID has a space, it removes it
        if len(elements[0]) > 5:
            ID = elements[0] 
            area = ID[:2]
            idno = ID[3:]
            elements[0] = area + idno

        # Fixes stove names            
#        if elements[3] == "Mud stove": elements[3] = "MUD"
#        if elements[3] == "Mud Stove": elements[3] = "MUD"
#        if elements[3] == "Mud stve": elements[3] = "MUD"
#        if elements[3] == "mud stove": elements[3] = "MUD"
#        if elements[3] == "Inductio": elements[3] = "INDUCTION"
#        if elements[3] == "Prakati": elements[3] = "PRAKTI"
#        if elements[3] == "TriPod": elements[3] = "TRIPOD"
#        if elements[3] == "PCS1": elements[3] = "PCS-1"
#        if elements[3] == "Enviorofit Dubble Pot": elements[3] = "ENVIROFIT DOUBLE"
#        if elements[3] == "Envirofit Double-pot": elements[3] = "ENVIROFIT DOUBLE"
        if elements[3] == "HIMANSHU": elements[3] = "TANDOOR"
        if elements[3] == "NEW INDUCTION": elements[3] = "INDUCTION"
        if elements[3] == "PCS-1": elements[3] = "ENVIROFIT DOUBLE"
        
        ID = elements[0].upper()     
        date = elements[1]
        HH = elements[2].upper()
        stove = elements[3].upper()
        
        # Fixes the file names by rearranging the order of the elements in the file name            
        # CHANGE ORDER OF ELEMENTS IN THE DESIRED ORDER
        f_new = ID + '_' + date + '_' + HH + '_' + stove + '.csv'
        print elements
        os.rename(os.path.join(path, f), os.path.join(path, f_new))
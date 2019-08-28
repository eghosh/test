# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 16:36:11 2018

@author: emily
"""

elements = ['KU258', '2016-04-29', 'GA36', 'MUD']

metadata = {}

temp = elements[0].replace(" ","") # SUMS ID

if len(temp) < 5:
    temparea = temp[:2]
    tempstoveid = temp[2:]
    temp = temparea + "0" + tempstoveid
    print temp

print temp

#elements[0] = elements[0].split[
#print elements[0]

#print [w[0] for w in elements[0]]

#metadata['ID'] = elements[0]
#print metadata['ID']

elements[0] = "A0".join(elements[0])

#if len(metadata['ID']) < 5:
#    for a in metadata['ID'].split():
#        print a
#    metadata['ID'] = "0".join(metadata['ID'])
    
#print metadata['ID']

#if len(metadata['ID']) < 5:
#    for a in metadata['ID']:
#        if a = "A" or a = "a":
            
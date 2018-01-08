#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 14:32:43 2018

@author: noramariamititelu
"""

import json 
#import csv 

with open ('precipitation.json') as file :
    precipitation_data = json.load (file)
    
#this way you could open the json file 

list_seattle = list()

for item in precipitation_data:
    if item ['station'] == 'GHCND:US1WAKG0038':
           list_seattle.append(item)
           
# you only select the items which contain the seattle code in them and in this manner, you also form a new list, which only contains them (list_seattle)
seattle_precipitationjan = list ()
for item in list_seattle:
     if '2010-01-' in item ['date']:
         seattle_precipitationjan.append(item['value'])

#manually, i created new lists for every month, containing only the values
# after that, i printed the sum of every variable and then i created a new variable for each sum of variables for each month 

print (sum(seattle_precipitationjan))
total_jan = sum(seattle_precipitationjan)
#
           
           
seattle_precipitationfeb = list()
for item in list_seattle: 
    if '2010-02-' in item ['date']:
        seattle_precipitationfeb.append(item['value'])

print (sum(seattle_precipitationfeb))
total_feb = sum(seattle_precipitationfeb)
           
           

seattle_precipitationmarch = list()
for item in list_seattle: 
    if '2010-03-' in item ['date']:
        seattle_precipitationmarch.append(item['value'])

print (sum(seattle_precipitationmarch))
total_march = sum(seattle_precipitationmarch)


seattle_precipitationapril = list()
for item in list_seattle: 
    if '2010-04-' in item ['date']:
        seattle_precipitationapril.append(item['value'])

print (sum(seattle_precipitationapril))
total_april = sum(seattle_precipitationapril)



seattle_precipitationmay = list()
for item in list_seattle: 
    if '2010-05-' in item ['date']:
        seattle_precipitationmay.append(item['value'])

print (sum(seattle_precipitationmay))
total_may = sum(seattle_precipitationmay)


seattle_precipitationjune = list()
for item in list_seattle: 
    if '2010-06-' in item ['date']:
        seattle_precipitationjune.append(item['value'])

print (sum(seattle_precipitationjune))
total_june = sum(seattle_precipitationjune)


seattle_precipitationjuly = list()
for item in list_seattle: 
    if '2010-07-' in item ['date']:
        seattle_precipitationjuly.append(item['value'])

print (sum(seattle_precipitationjuly))
total_july = sum(seattle_precipitationjuly)

seattle_precipitationaugust = list()
for item in list_seattle: 
    if '2010-08-' in item ['date']:
        seattle_precipitationaugust.append(item['value'])

print (sum(seattle_precipitationaugust))
total_august = sum(seattle_precipitationaugust)

seattle_precipitationsept = list()
for item in list_seattle: 
    if '2010-09-' in item ['date']:
        seattle_precipitationsept.append(item['value'])

print (sum(seattle_precipitationsept))
total_sept = sum(seattle_precipitationsept)

seattle_precipitationoct = list()
for item in list_seattle: 
    if '2010-10-' in item ['date']:
        seattle_precipitationoct.append(item['value'])

print (sum(seattle_precipitationoct))
total_oct = sum(seattle_precipitationoct)


seattle_precipitationnov = list()
for item in list_seattle: 
    if '2010-11-' in item ['date']:
        seattle_precipitationnov.append(item['value'])

print (sum(seattle_precipitationnov))
total_nov = sum(seattle_precipitationnov)


seattle_precipitationdec = list()
for item in list_seattle: 
    if '2010-12-' in item ['date']:
        seattle_precipitationdec.append(item['value'])

print (sum(seattle_precipitationdec))
total_dec = sum(seattle_precipitationdec)
#    
all_months = list ()
all_months = [total_jan,total_feb,total_march,total_april, total_may, total_june, total_july, total_august, total_sept, total_oct, total_nov, total_dec]
print (all_months)

# in the end, i made a new list with all the sum values for each month and i summed up these values, getting to the final sum for the entire year 





print (sum(all_months))

yearly_total = sum(all_months)

relative_precipitationjan = total_jan / yearly_total

relative_precipitationfeb = total_feb / yearly_total

relative_precipitationmarch = total_march / yearly_total

relative_precipitationapril = total_april / yearly_total

relative_precipitationmay = total_may / yearly_total

relative_precipitationjune = total_june / yearly_total

relative_precipitationjuly = total_july / yearly_total

relative_precipitationaugust = total_august/ yearly_total

relative_precipitationseptember = total_sept / yearly_total 

relative_precipitationoctober = total_oct / yearly_total

relative_precipitationnovember = total_nov/ yearly_total

relative_precipitationdecember = total_dec / yearly_total 


relative_precipitation = list()

relative_precipitation = [relative_precipitationjan, relative_precipitationfeb,relative_precipitationmarch, relative_precipitationapril, relative_precipitationmay, relative_precipitationjune, relative_precipitationjuly, relative_precipitationaugust, relative_precipitationseptember, relative_precipitationoctober, relative_precipitationnovember, relative_precipitationdecember ]

relative_yearly_prec = sum (relative_precipitation) 

# you manage to find the relative precipitation for every month by dividing the monthly precipitation by the yearly precipitation for each month 






import json 

with open ('file.json', 'w') as file: 
    json.dump ({"Seattle": { 
        "totalYearlyPrecipitation" : yearly_total, 
        "totalMonthlyPrecipitation" : all_months, 
        "state" : "WA", 
        "realtiveMonthlyPrecipitation" : relative_precipitation, 
        "station" : "GHCND :US1WAKG0038", 
        "relativeYearlyPrecipitation" : relative_yearly_prec 
        }
    }, file ) 






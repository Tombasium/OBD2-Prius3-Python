# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 17:48:41 2019

@author: TomLap
"""

import pandas as pd
import csv

source = []

with open("C:/Users/TomLap/CanTest/candump-2019-10-04_125707.log", "r") as fb:
    for line in fb:
        broken = line.split()
        if len(broken) > 1:
            time = broken[0][1:-1]
            code = broken[2][0:3]
            msg = broken[2][4:]
            data = [msg[i:i+2] for i in range(0, len(msg)-1, 2)]
            
            source.append([time, code] + data)

sourceDF = pd.DataFrame(source)

codeDetails = sourceDF[1].value_counts()

condensed = []

for code in list(codeDetails.index):
#    snippet = sourceDF.loc[sourceDF[1] == code]
#    val = 
    rangeData = [sourceDF.loc[sourceDF[1] == code][i].nunique() for i in 
                 range(2, len(sourceDF.loc[sourceDF[1] == code].columns))]
    condensed.append([code, codeDetails.loc[code]] + rangeData)


with open("value_ranges_by_code.csv", "w") as output:
    csv_writer = csv.writer(output, lineterminator="\n")
    for line in condensed:       
        csv_writer.writerow(list(line))

#print(condensed)
#sourceDF.loc[sourceDF[1] == "631"]
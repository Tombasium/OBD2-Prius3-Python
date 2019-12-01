# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 19:27:22 2019

@author:    Tom Walton
@date:      24/11/2019

Thanks to Brent Stone for his work on reverse engineering CAN-Bus data, on which
much of this work is based. 

his github repository can be found at:
    
    https://github.com/brent-stone/CAN_Reverse_Engineering
"""

import pandas as pd
import time


## Takes the original DataFrame and outputs a DataFrame with general info
## For each code, including:
## Code value
## Number of instances
## frequency / second
## number of different values that each byte can take.

## The assumption is that if the byte can take many values it may be part of 
## a continuous variable.


def get_data_general_stats(data):
    
    start_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(data.iloc[0]["time"]))
    
    end_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(data.iloc[len(data)-1]["time"]))
    
    time_elapsed = data.iloc[len(data)-1]["time"] - data.iloc[0]["time"]
    
    print("start of data: %s" % start_time)
    print("end of data  : %s" % end_time)
    print("Time elapsed : %.2f seconds" % time_elapsed)
        
    output = []
    
    codes_grouped = data.groupby("code")
    
    for code in codes_grouped:
        output.append([code[0], len(code[1]), len(code[1])/time_elapsed, 
                       code[1]["b0"].nunique(), code[1]["b1"].nunique(), 
                       code[1]["b2"].nunique(), code[1]["b3"].nunique(), 
                       code[1]["b4"].nunique(), code[1]["b5"].nunique(), 
                       code[1]["b6"].nunique(), code[1]["b7"].nunique()])
    
    return pd.DataFrame(output, columns = ["Code", "Number", "Frequency/s",
                                           "b0 range", "b1 range", "b2 range",
                                           "b3 range", "b4 range", "b5 range",
                                           "b6 range", "b7 range"])

## This method extends the assumption that a byte with many values can be
## part of a continuous dataset, and that if nothing changes it contains 
## either switch data or static values

def initial_guesses(data):
    output = []
    for index, row in data.iterrows():
        code = row["Code"]
        number = row ["Number"]
        freq = "%.2f" % row["Frequency/s"]
        b0_type = get_b_type(row["b0 range"])
        b1_type = get_b_type(row["b1 range"])
        b2_type = get_b_type(row["b2 range"])
        b3_type = get_b_type(row["b3 range"])
        b4_type = get_b_type(row["b4 range"])
        b5_type = get_b_type(row["b5 range"])
        b6_type = get_b_type(row["b6 range"])
        b7_type = get_b_type(row["b7 range"])
        
        if any([x == "Continuous data?" for x in [b0_type, b1_type, 
                                                          b2_type, b3_type, 
                                                          b4_type, b5_type,
                                                          b6_type, b7_type]]):
            output.append([code, number, freq, b0_type, b1_type, b2_type, b3_type,
                          b4_type, b5_type, b6_type, b7_type])

    return pd.DataFrame(output)

def get_b_type(byte_range):
    if byte_range == 1:
        return "Static or rarely changed"
    if 5 >= byte_range and byte_range > 1:
        return "Little movement - switch?"
    if byte_range > 5:
        return "Continuous data?"
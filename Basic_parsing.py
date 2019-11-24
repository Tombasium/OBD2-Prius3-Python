# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 19:11:14 2019

@author:    Tom Walton
@date:      24/11/2019

Thanks to Brent Stone for his work on reverse engineering CAN-Bus data, on which
much of this work is based. 

his github repository can be found at:
    
    https://github.com/brent-stone/CAN_Reverse_Engineering

"""

import pandas as pd

## This code gets the data in from the dump file and outputs as a pandas dataframe

def get_data_as_df():
    
    output = []

    with open("C:/Users/TomLap/CanTest/candump-2019-10-04_125707.log", "r") as fb:
        for line in fb:
            broken = line.split()
            if len(broken) > 1:
                time = float(broken[0][1:-1])
                code = broken[2][0:3]
                msg = broken[2][4:]
                data = [msg[i:i+2] for i in range(0, len(msg)-1, 2)]
                
                output.append([time, code] + data)
    
    return pd.DataFrame(output, columns = ["time", "code", "b0", "b1", "b2", 
                                           "b3", "b4", "b5", "b6", "b7"])
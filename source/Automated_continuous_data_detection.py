# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 19:56:58 2019

@author:    Tom Walton
@date:      24/11/2019

Thanks to Brent Stone for his work on reverse engineering CAN-Bus data, on which
much of this work is based. 

his github repository can be found at:
    
    https://github.com/brent-stone/CAN_Reverse_Engineering

"""

import util

import pandas as pd

## This method takes in CANbus data that has already been parsed into a dataframe
## with the following 10 columns: 
## time | code | b0...b7
##
## It first converts the data into a uint64 to be analysed bit by bit.
##
##
## This may not be necessary in the context of vehicle CANbus data as it is 
## explicitly 


def find_continuous_data(input_dataframe):
    
    input_dataframe["bytes_concat"] = (input_dataframe.b0 + input_dataframe.b1 
                           + input_dataframe.b2 + input_dataframe.b3
                            + input_dataframe.b4 + input_dataframe.b5
                             + input_dataframe.b6 + input_dataframe.b7
                             )
    
    input_dataframe["bytes_as_uint64"] = input_dataframe.apply(lambda row: util.hex_to_dec_variable_length(str(row.bytes_concat)), axis=1)
    
    input_dataframe["bytes_as_bits"] = input_dataframe.apply(lambda row: util.uint64_to_bits(int(row.bytes_as_uint64)), axis=1)
    
    modified_dataframe = input_dataframe.drop(columns=["b0", "b1", "b2", "b3",
                                                       "b4", "b5", "b6", "b7"])#.join(concatenated_bytes)
        
    
    print(modified_dataframe.head())
    #data_grouped_by_code = input_dataframe.groupby("code")
    
#    for code in data_grouped_by_code:
#        print(code[1])
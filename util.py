# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 18:17:00 2019

@author: TomLap
"""

def hex_to_dec(value):
    if ord(value[0]) in range(48, 58):
        decimal = ord(value[0]) - 48
    if ord(value[0]) in range(65, 71):
        decimal = ord(value[0]) - 55
    return int(decimal)

def hex_byte_to_dec_11bit(value):
    
    byte_1 = hex_to_dec(value[0])
    multiplier = hex_to_dec(value[1])
    addition = hex_to_dec(value[2])
    
    value = (byte_1 * 256) + (multiplier * 16) + addition
    
    return value

def hex_to_dec_variable_length(value):
    result = 0
    multiplier = 1
    for i in range(len(value) - 1, -1, -1):
        result += hex_to_dec(value[i]) * multiplier
        multiplier = multiplier * 16
    return result
    
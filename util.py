# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 18:17:00 2019

@author: TomLap
"""

def hex_byte_to_dec_11bit(value):
    
    byte_1 = hex_to_dec(value[0])
    multiplier = hex_to_dec(value[1])
    addition = hex_to_dec(value[2])
    
    value = (byte_1 * 256) + (multiplier * 16) + addition
    
    return value

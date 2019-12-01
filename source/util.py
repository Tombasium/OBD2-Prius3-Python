# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 18:17:00 2019

@author:    Tom Walton
@date:      24/11/2019

Thanks to Brent Stone for his work on reverse engineering CAN-Bus data, on which
much of this work is based. 

his github repository can be found at:
    
    https://github.com/brent-stone/CAN_Reverse_Engineering

"""

def hex_to_dec(value):
    if ord(value) in range(48, 58):
        decimal = ord(value[0]) - 48
    elif ord(value) in range(65, 71):
        decimal = ord(value[0]) - 55
    else:
        decimal = 0
    return int(decimal)

def hex_byte_to_dec_11bit(value):
    
    byte_1 = hex_to_dec(value[0])
    multiplier = hex_to_dec(value[1])
    addition = hex_to_dec(value[2])
    
    value = (byte_1 * 256) + (multiplier * 16) + addition
    
    return value

def hex_to_dec_variable_length(value):
    assert type(value) == str
    result = 0
    multiplier = 1
    for i in range(len(value) - 1, -1, -1):
        result += hex_to_dec(value[i]) * multiplier
        multiplier = multiplier * 16
    return result

def uint64_to_bits(value):
    assert type(value) == int
    
    output = [0] * 64
    
    for i in range(0, 64, 1):
        bit_value = 2 ** (64-(i+1))
        if (value - bit_value) >= 0:
            output[i] = 1
            value = value - bit_value
    return output
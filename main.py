# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import time
import csv

def convert_to_csv(file_name = "C:/Users/TomLap/CanTest/candump-2019-10-04_125707.log"):
    csv_writer = csv.writer
    with open(file_name, "r", newline = "\n") as source:
        with open("CANdata.csv", "w") as output:
            csv_writer = csv.writer(output, lineterminator="\n")
            for line in source:
                
                output_line = prepare_line_for_csv(line)
                csv_writer.writerow(list(output_line))
                #print(output_line)

def prepare_line_for_csv(line):
    data = line.split(" ")
#    date_time = [epoch_to_timestamp(data[0])]
    if len(data) == 3:
        date_time = [float(data[0][1:-1])]
        code = [get_line_code(data[2])]
        data = parse_line_data_to_list(data[2])
        
        output = date_time + code + data
        
        return output

    else:
        return

def convert_and_strip_file(file_name = "C:/Users/TomLap/CanTest/candump-2019-10-04_125707.log"):
    with open(file_name, "r", newline = "\n") as source:
        with open("modded_output2.log", "w") as output:
            for line in source:
                parts = line.split(" ")
                if len(line.split(" ")) == 3:
                    output.write(epoch_to_timestamp(parts[0]) + " " + parts[2])

def get_address_lists(file_name = "modded_output.log"):
    code_list = {}
    with open("modded_output.log", "r") as source:
        for line in source:
            code = line[0:3]
            if code in code_list.keys():
                count = code_list[code] + 1
            else: 
                count = 1
            code_list.update({code : count})
    
    return code_list            

def hex_to_dec(value):
    if ord(value[0]) in range(48, 58):
        decimal = ord(value[0]) - 48
    if ord(value[0]) in range(65, 71):
        decimal = ord(value[0]) - 55
    return int(decimal)

def hex_byte_to_dec(byte):
    multiplier = hex_to_dec(byte[0])
    addition = hex_to_dec(byte[1])
    
    value = (multiplier * 16) + addition
    
    return value

def hex_byte_to_dec_11bit(value):
    
    byte_1 = hex_to_dec(value[0])
    multiplier = hex_to_dec(value[1])
    addition = hex_to_dec(value[2])
    
    value = (byte_1 * 256) + (multiplier * 16) + addition
    
    return value


def get_line_code(line, style = 'dec'):
    if style == 'dec':
        output = (hex_byte_to_dec_11bit(line[:3]))

    if style == 'hex':
        output = (line[:3])

    return output
    
    
def parse_line_data_to_list(line, style = 'dec'):
    output = []
    if style == 'dec':
        for i in range(4, len(line) - 2, 2):
            output.append(hex_byte_to_dec(line[i:i+2]))

    if style == 'hex':
        for i in range(4, len(line) - 2, 2):
            output.append(line[i:i+2])

    return output
            
def parse_line_data_to_str(line, style = 'dec'):
    output = ''
    if style == 'dec':
        for i in range(4, len(line) - 2, 2):
            output += str(hex_byte_to_dec(line[i:i+2])) + ' ' 

    if style == 'hex':
        for i in range(4, len(line) - 2, 2):
            output += str(line[i:i+2]) + ' ' 

    return output

def epoch_to_timestamp(epoch_value):
    value = epoch_value.split(".")[0][1:]
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(value)))   

def print_parsed_lines(file_name = "modded_output.log"):
    
    with open("modded_output.log", "r") as source:
        for line in source:
            print(parse_line_data(line))
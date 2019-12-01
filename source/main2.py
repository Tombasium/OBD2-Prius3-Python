# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 19:55:50 2019

@author:    Tom Walton
@date:      24/11/2019

Thanks to Brent Stone for his work on reverse engineering CAN-Bus data, on which
much of this work is based. 

his github repository can be found at:
    
    https://github.com/brent-stone/CAN_Reverse_Engineering

"""

import Basic_parsing
import General_data_stats
import Automated_continuous_data_detection

data = Basic_parsing.get_data_as_df()

Automated_continuous_data_detection.find_continuous_data(data)

#summary = General_data_stats.get_data_general_stats(data)
#
#early_assumptions = General_data_stats.initial_guesses(summary)
#
#print(early_assumptions)
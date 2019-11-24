# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 19:55:50 2019

@author: TomLap
"""

import Basic_parsing
import General_data_stats

data = Basic_parsing.get_data_as_df()

summary = General_data_stats.get_data_general_stats(data)

early_assumptions = General_data_stats.initial_guesses(summary)

print(early_assumptions)
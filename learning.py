# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 14:21:08 2019

@author: tie303295
"""

# import sys
import fasttext as ft

# argvs = sys.argv
# input_file = argvs[1]
# output_file = argvs[2]

classifier = ft.supervised('model.txt', 'learning')
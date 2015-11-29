#!/home/emilia/anaconda3/bin/ipython
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 21:58:54 2015

@author: emilia
"""


import re
import sys
from module1 import *
from module2 import *
import numpy as np
import scipy.io.wavfile
import scipy.fftpack
import os




utwor = sys.argv[1]  
print(utwor)  

beatbox(utwor, fs = 44100)

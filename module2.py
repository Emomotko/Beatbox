#!/home/emilia/anaconda3/bin/ipython
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 18:22:16 2015

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


def save_music(y, fs, fname):
    
    scipy.io.wavfile.write(fname,
                       fs,
                       np.int16(y/max(np.abs(y))*32767))

def beatbox(utwor, fs = 44100):
    
    number_song = re.search('[0-9]', utwor).group(0)
    
    path_name = ''.join(['utwor/','song0',number_song])   
    paths = open(path_name).readlines()
    paths = list(map(str.strip,paths))
    
    
    bpm = open(''.join(['utwor/','defs.txt']) ).readlines()
    bpm = list(map(str.strip,bpm))
    bpm = float(re.search('[0-9]+', bpm[1]).group(0))
    
    wave = create_music(bpm, paths)
    
    fname = ''.join(['./',utwor,'/',utwor,'.wav'])
    save_music(wave, fs, fname)

#!/home/emilia/anaconda3/bin/ipython
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 23:01:08 2015

@author: Emilia Momotko

In this file the notes will be generated and the music based in them will be
created. Additional samples will also be added in order to emphasize the beat.
Hope you will enjoy this beatbox!!
"""

import numpy as np
import scipy.io.wavfile
import scipy.fftpack
import os


def generate_note(name, fs, l):
    
    decay = int(0.01*l)
    import numpy as np
    
    freq = np.array([131, 147, 156, 175, 196, 220, 247, 262, 294, 330, 349, 389, 440, 494, 523, 587, 659, 698, 784, 880, 988])
    names = np.array(['C-3', 'D-3', 'E-3', 'F-3','G-3', 'A-3', 'H-3', 'C-4', 'D-4', 'E-4', 'F-4','G-4', 'A-4', 'H-4','C-5', 'D-5', 'E-5', 'F-5','G-5', 'A-5', 'H-5'])
    
    f = freq[np.where(names==name)]
    
    t = np.linspace(0, 1, l)
    
    y = np.sin(2*np.pi*f*t)
    
    return y


def lengths(utwor, bpm, tracks):
    
    tracks = open(tracks).readlines()
    tracks = list(map(str.strip,tracks))
    
    g = int(44100.0/(bpm/60.0))
    
    n = len(tracks)
    l = len(tracks[0].rsplit(" "))
    
    result = np.zeros(shape = (n, l))
    
    for j in range(len(tracks)):
         
        actual = tracks[j].rsplit(" ")
           

        for k in range(len(actual)):
            
            if len(actual[k]) == 3:
                result[j, k] = g
            else:
                if actual[k] == '--':
                    result[j, k] = 0
                else:
                    sample = ''.join([utwor,'sample', actual[k],'.wav'])
                    
                    fs, y =   scipy.io.wavfile.read(sample)
                    result[j, k] = len(y)
                    
                    
    return result        
            
    


def overall_bias(bpm, lista):
    
    g = int(44100.0/(bpm/60.0))
    w = g
    
    for i in range(0, len(lista)):
        
        w = w - g
        
        if w < 0:
            w = 0
        
        x = lista[i] - g
        if x > w:
            w = x
    return w
    
def create_music(utwor, bpm, paths):
    
    N = len(paths)  
    g = int(44100.0/(bpm/60.0))
    
    l = [lengths(utwor, bpm, x) for x in [''.join([utwor,'track',p]) for p in paths]]
    
    main_lengths = []
    for i in range(len(paths)):
        main_lengths.append([np.max(x) for x in l[i]])
    
    bias = [overall_bias(bpm, x) for x in main_lengths]
    
    a = [len(x)*g for x in main_lengths]
    l = list(map(sum,zip(a, bias)))
    
    result = np.zeros(int(np.sum(l)))
    
    pom = np.r_[[0], np.cumsum(l)]
    
    h = 0
    
    for i in range(len(paths)):
        
        track_name = ''.join([utwor,'track',paths[i]])
        
        tracks = open(track_name).readlines()
        tracks = list(map(str.strip,tracks))
        
        for j in range(len(tracks)):
            
            actual = tracks[j].rsplit(" ")
            
            for k in actual:
                if len(k) == 3:
                    result[pom[i] + j*g:pom[i] +j*g + g] = result[pom[i] +j*g:pom[i] +j*g + g] + generate_note(k, 44100, g)
                else:
                    if k != '--':
                        sample = ''.join([utwor,'sample', k,'.wav'])
                        fs, y =   scipy.io.wavfile.read(sample)
                        y = np.mean(y, axis = 1)
                        y = y/32767
                        result[pom[i] + j*g:pom[i] +j*g + len(y)] = result[pom[i] +j*g:pom[i] +j*g + len(y)] + y
                    else: 
                        result[pom[i] + j*g:pom[i] +j*g + g] = result[pom[i] +j*g:pom[i] +j*g + g] + np.zeros(g)
            
    return result     

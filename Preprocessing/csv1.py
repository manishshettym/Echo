import csv
import matplotlib.pyplot as plt
import wave
import librosa
import numpy as np
import pandas as pd
import os

destpdir = "../../CSVs/"
if not os.path.exists(destpdir):
    os.makedirs(destpdir)


male_amplitudes = []
female_amplitudes = []
for i in range(1,10):
    srcdir = "../Dataset/Audio_Speech_Actors_01-24/Actor_0"+str(i)
    destdir = "../../CSVs/Actor_0"+str(i)+"/"
    if not os.path.exists(destdir):
        os.makedirs(destdir)
    for root, dirs, files in os.walk(srcdir):  
        for filename in files:
            time = []
            print(filename)
            wave_file = wave.open(srcdir+'/'+filename, "rb")
            frame_rate = wave_file.getframerate()
            data, sampling_rate = librosa.load(srcdir+'/'+filename, sr = frame_rate)
            if(i%2 == 0):
                female_amplitudes+=data.tolist()
                #female_amplitudes+=data
            else:
                male_amplitudes+=data.tolist()
            '''for i in range(len(data)):
                time.append(i+1)'''
            #dictData = {'Time': time, 'Amplitude': data}
            #df = pd.DataFrame(dictData)
            #df.to_csv(destdir+filename.split(".")[0]+'.csv', index = False)
        
for i in range(10,25):
    srcdir = "../Dataset/Audio_Speech_Actors_01-24/Actor_"+str(i)
    destdir = "../../CSVs/Actor_"+str(i)+"/"
    if not os.path.exists(destdir):
        os.makedirs(destdir)
    for root, dirs, files in os.walk(srcdir):  
        for filename in files:
            print(filename)
            time = []
            wave_file = wave.open(srcdir+'/'+filename, "rb")
            frame_rate = wave_file.getframerate()
            data, sampling_rate = librosa.load(srcdir+'/'+filename, sr = frame_rate)
            if(i%2 == 0):
                female_amplitudes+=data.tolist()
            else:
                male_amplitudes+=data.tolist()
            '''for i in range(len(data)):
                time.append(i+1)'''
            #dictData = {'Time': time, 'Amplitude': data}
            #df = pd.DataFrame(dictData)
            #df.to_csv(destdir+filename.split(".")[0]+'.csv', index = False)
d = {"Amplitudes",male_amplitudes}
df = pd.DataFrame(d)
df.to_csv("/home/nishant/Documents/sem6/ML Project/Echo/Analysis/males.csv",index=False)
d = {"Amplitudes",female_amplitudes}
df = pd.DataFrame(d)
df.to_csv("/home/nishant/Documents/sem6/ML Project/Echo/Analysis/females.csv",index=False)

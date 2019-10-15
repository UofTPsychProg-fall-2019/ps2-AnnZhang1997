#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scene-cat problem set for PSY 1210 - Fall 2018

@author: Michael Mack
"""

#%% import block 
import numpy as np
import scipy as sp
import scipy.stats
import os
import shutil


#%%
# copy files from testing room folders to raw data, rename files to include
# testing room letter in the filename
#
testingrooms = ['A','B','C']
for room in testingrooms:
# Ann Z: the path to the current & new folders
    curr_path = os.getcwd() + "\\testingroom" + room
    new_path = os.getcwd() + "\\rawdata"
# Ann Z: gets the current name of the file and the new name
    filename = os.listdir(curr_path)[0]
    new_filename = "experiment_data" + room + ".csv"
# Ann Z: the path to the file
    curr_path = curr_path + "\\" + filename
    new_path = new_path + "\\" + new_filename
# Ann Z: move file & change name
    shutil.move(curr_path, new_path)
        

#%%
# read in all the data files in rawdata directory using a for loop
# columns: subject, stimulus, pairing, accuracy, median RT
#
data = np.empty((0,5))
# Ann Z: change the current path to rawdata
os.chdir("C:\\Users\\lenovo\\Documents\\GitHub\\ps2-AnnZhang1997\\rawdata")
for room in testingrooms:
    datafile = "experiment_data" + room + ".csv"
    tmp_data = sp.loadtxt(datafile, delimiter = ',')
    data = np.vstack([data, tmp_data])

#%%
# calculate overall average accuracy and average median RT
#
# acc_avg = 91.48%
# mrt_avg = 477.3ms
acc_sum = 0
mrt_sum = 0
for trial in data:
    acc_sum = acc_sum + trial[3]
    mrt_sum = mrt_sum + trial[4]
# Ann Z: get the summed acc and mrt of each trial, divide by number of trials
acc_avg = acc_sum/len(data)
mrt_avg = mrt_sum/len(data)


#%%
# calculate averages (accuracy & RT) split by stimulus using a for loop and an 
# if statement. (i.e., loop through the data to make a sum for each condition, 
# then divide by the number of data points going into the sum)
words = 1
faces = 2
# Ann Z: first try to calculate the sums for each stimulus
acc_words_sum = 0
mrt_words_sum = 0
trials_words = 0
acc_faces_sum = 0
mrt_faces_sum = 0
trials_faces = 0

for trial in data:
    if trial[1] == words:
        acc_words_sum += trial[3]
        mrt_words_sum += trial[4]
        trials_words += 1
    elif trial[1] == faces:
        acc_faces_sum += trial[3]
        mrt_faces_sum += trial[4]
        trials_faces += 1
# Ann Z: after getting sums,divide by trials.
acc_words = acc_words_sum/trials_words
mrt_words = mrt_words_sum/trials_words
acc_faces = acc_faces_sum/trials_faces
mrt_faces = mrt_faces_sum/trials_faces

# words: 88.6%, 489.4ms   faces: 94.4%, 465.3ms


#%%
# calculate averages (accuracy & RT) split by congruency using indexing, 
# slicing, and numpy's mean function 
# wp - white/pleasant, bp - black/pleasant
# (hint: only one line of code is needed per average)
#
acc_wp = np.mean(data[np.argsort(data[:, 2], axis = 0)][0:46], axis = 0)[3] 
# 94.0%
acc_bp = np.mean(data[np.argsort(data[:, 2], axis = 0)][46:], axis = 0)[3]  
# 88.9%
mrt_wp = np.mean(data[np.argsort(data[:, 2], axis = 0)][0:46], axis = 0)[4]  
# 469.6ms
mrt_bp = np.mean(data[np.argsort(data[:, 2], axis = 0)][46:], axis = 0)[4]  
# 485.1ms


#%% 
# calculate average median RT for each of the four conditions
# use for loops, indexing/slicing, or both!
# (hint: might be easier to slice data into separate words and faces datasets)
#
...
# TO DO
# Ann Z: sort data based on words or faces
sorted_data = data[np.argsort(data[:, 1], axis = 0)]
words_data = sorted_data[0: 46]
faces_data = sorted_data[46:]
# Ann Z: sort words and faces data based on pairing
words_wp = words_data[np.argsort(words_data[:, 2], axis = 0)][0:23]
words_bp = words_data[np.argsort(words_data[:, 2], axis = 0)][23:]
faces_wp = faces_data[np.argsort(faces_data[:, 2], axis = 0)][0:23]
faces_bp = faces_data[np.argsort(faces_data[:, 2], axis = 0)][23:]

mrt_words_wp = np.mean(words_wp, axis = 0)[4]
mrt_words_bp = np.mean(words_bp, axis = 0)[4]
mrt_faces_wp = np.mean(faces_wp, axis = 0)[4]
mrt_faces_bp = np.mean(faces_bp, axis = 0)[4]
# words - white/pleasant: 478.4ms
# words - black/pleasant: 500.3ms
# faces - white/pleasant: 460.8ms
# faces - black/pleasant: 469.9ms

#%%        
# compare pairing conditions' effect on RT within stimulus using scipy's 
# paired-sample t-test: scipy.stats.ttest_rel()
#
import scipy.stats
# because this is dependent sample, must sort the list so that subjects
# correspond with each other
words_wp = words_wp[np.argsort(words_wp[:, 0], axis = 0)]
words_bp = words_bp[np.argsort(words_bp[:, 0], axis = 0)]
faces_wp = faces_wp[np.argsort(faces_wp[:, 0], axis = 0)]
faces_bp = faces_bp[np.argsort(faces_bp[:, 0], axis = 0)]

# Ann Z: Answer is incorrect, can't figure out where is wrong. -- Done! Yeah!
words_t = scipy.stats.ttest_rel(words_wp, words_bp)[0][4]
words_p = scipy.stats.ttest_rel(words_wp, words_bp)[1][4]
faces_t = scipy.stats.ttest_rel(faces_wp, faces_bp)[0][4]
faces_p = scipy.stats.ttest_rel(faces_wp, faces_bp)[1][4]

# words: t=-5.36, p=2.19e-5
# faces: t=-2.84, p=0.0096.

#%%
# print out averages and t-test results
# (hint: use the ''.format() method to create formatted strings)
#
print('\nOVERALL: {:.2f}%, {:.1f} ms'.format(100*acc_avg,mrt_avg))
print('\nSTIMULUS-WORDS: {:.2f}%, {:.1f} ms'.format(100*acc_words,mrt_words))
print('\nSTIMULUS-FACES: {:.2f}%, {:.1f} ms'.format(100*acc_faces,mrt_faces))
print('\nPAIRING-WHITE/PLEASANT: {:.2f}%, {:.1f} ms'.format(100*acc_wp,mrt_wp))
print('\nPAIRING-BLACK/PLEASANT: {:.2f}%, {:.1f} ms'.format(100*acc_bp,mrt_bp))
print('\nCONDITION-WORDS+WHITE/PLEASANT: {:.1f} ms'.format(mrt_words_wp))
print('\nCONDITION-WORDS+BLACK/PLEASANT: {:.1f} ms'.format(mrt_words_bp))
print('\nCONDITION-FACES+WHITE/PLEASANT: {:.1f} ms'.format(mrt_faces_wp))
print('\nCONDITION-FACES+BLACK/PLEASANT: {:.1f} ms'.format(mrt_faces_bp))
print('\nTTEST-WORDS: t = {:.2f} , p = {:.2}'.format(words_t, words_p))
print('\nTTEST-FACES: t = {:.2f} , p = {:.2}'.format(faces_t, faces_p))
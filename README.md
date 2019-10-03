# scene-cat
PSY 1210 Problem Assignment 2

We're giving you some data files and the skeleton of a data analysis script. You need to flesh out the missing sections of the analysis script to implement a simple analysis of the data.

## The experiment
The experiment behind the data: 23 participants performed the Race Implicit Association Test in which they rapidly categorized words as pleasant or unpleasant and faces as White or Black. Across blocks, these two decisions were combined in different ways such that the response key for one category of words was also the response for one category of faces: pleasant/White vs. unpleasant/Black OR pleasant/Black vs. unpleasant/White. The question is whether or not pairing pleasant or unpleasant with White or Black leads to more accurate and/or faster responses. Results from this task suggest that people generally show a bias when pleasant is paired with White and unpleasant is paired with Black such that responses are more accurate and faster than with the opposite pairing. You can [try out the experiment](https://implicit.harvard.edu/implicit/user/agg/blindspot/indexrk.htm).

## The data
We provide the summary data for each participant including their accuracy and median reaction time (RT) for each of the four conditions (words - White/Pleasant, faces - White/Pleasant, words - Black/Pleasant, faces - Black/Pleasant). Since the data was collected in three different testing rooms, these summary data files (all named experiment_data.csv) are separated into three different directories (testingroom{A,B,C}). Each file contains data from 7 or 8 participants.

The data is formatted into 5 columns:
* subject number
* stimulus: 1 = words, 2 = faces
* pairing: 1 = white/pleasant, 2 = black/pleasant
* accuracy
* median RT (ms)

## Your task
Fill in the missing sections of the skeleton analysis script with python code in order to:
1. Copy these files into the rawdata directory, renaming each file to include the corresponding testing room letter (e.g., experiment_data_A.csv). _hint:_ check out the `os` and `shutil` python libraries.
2. Read in all the data from the newly copied data files.
3. Calculate the following:
   * Overall average accuracy and median RT
   * Averages of accuracy and median RT split by stimulus (words vs. faces) using a `for` loop, `if` statement, and arithmetic
   * Averages of accuracy and median RT split by pairing (white/pleasant vs. black/pleasant) using numpy's mean function
   * Average median RT for each of the four conditions
4. Conduct t-tests to compare median RT for the two pairings for each stimulus using `scipy.stats.ttest_rel()`
5. Print out all of the averages and t-test results in a coherent format.

The analysis script skeleton repeats these instructions and gives you a few more pointers on how to accomplish these tasks. This is not a group assignment, but you are strongly encouraged to help each other.

Good luck!

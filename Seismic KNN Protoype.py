
# to make this code work, you have to add another row to the csv file and add 12 to the row_value_list
# a the bottom of the script is optional code to graph a visual of the data points
# there are 4 cluster groups

import pandas as pd
from scipy import spatial
import math
import operator

df = pd.read_csv('Seismic KNN Sample Data.csv')

def Compute_Distance(a, b):
    x1 = df['Highest Avg Load'][a]
    x2 = df['Highest Avg Load'][b]
    y1 = df['Volume'][a]
    y2 = df['Volume'][b]
    distance = math.sqrt( ((x2-x1)**2)+((y2-y1)**2) )
    return distance

row_value_list = [0,1,2,3,4,5,6,7,8,9,10,11]
distances = []
K_value_plus_one = 4

def find_k(a):
    for b in row_value_list:
        Compute_Distance(a, b)
        distances.append(Compute_Distance(a, b))

# finds the closest values in the data set to the id number specificed
# the number of K is K_value_plus_one
# the mode of the Phase will determine the Phase of the new or already exisiting value
find_k(7)
df3 = df["Phase"]
columnNames = ["Distances"]
df2 = pd.DataFrame(distances, columns=columnNames)
df2.sort_values('Distances').head(K_value_plus_one).join(df3)


#%matplotlib inline
# import matplotlib.pyplot as plt
# plt.style.use('seaborn-whitegrid')
# import numpy as np

# x = df['Highest Avg Load']
# y = df['Volume']
# n = df['Exercise Id']
# scat = plt.plot(x, y, 'o', color='black')    
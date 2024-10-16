import math
from math import exp

import pandas as pd
import matplotlib.pyplot as plt

# read csv file
path = "C:\\Users\\yingx.DESKTOP-K7RP8AE\\Downloads\\hw2_data.txt"
col_names = ['exam1', 'exam2', 'status']
data = pd.read_csv(path, header=None, names=col_names)

# logisticRegression
def logisticRegression(data, theta, i):
    return 1 / (1 + exp(-(theta[2] * data.exam2[i] + theta[1] * data.exam1[i] + theta[0])))


# maximum likelihood / loss function
def maxLikelihood(data, theta):
    sum = 0
    n = len(data)
    for i in range(n):
        sum += math.log(logisticRegression(data, theta, i)) ** data.status[i] * (1 - logisticRegression(data, theta, i)) ** (1-data.status[i])
    return -(1/n) * sum


# gradient descent
def grad_exam1(data, theta):
    sum = 0
    n = len(data)
    for i in range(n):
        sum += (logisticRegression(data, theta, i) - data.status[i]) * data.exam1[i]
    return sum


def grad_exam2(data, theta):
    sum = 0
    n = len(data)
    for i in range(n):
        sum += (logisticRegression(data, theta, i) - data.status[i]) * data.exam2[i]
    return sum


theta = [1, 0, 0]  # theta[0] is bias, theta[1] is exam1, theta[2] is exam2
learningRate = 0.001
epochs = 100
for i in range(epochs):
    theta[1] = theta[1] - (learningRate * grad_exam1(data, theta))
    theta[2] = theta[2] - (learningRate * grad_exam2(data, theta))
    print("Theta1 is", theta[1])
    print("Theta2 is", theta[2], "\n")



import math
from math import exp

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# read csv file
path = "C:\\...\\hw2_data.txt" #enter path
col_names = ['exam1', 'exam2', 'status']
df = pd.read_csv(path, header=None, names=col_names)

# get train x and train y in np array
X_train = df[['exam1', 'exam2']].values.T
Y_train = df['status'].values.reshape(1, X_train.shape[1])


#Log function 
# 1 / (1+e^(-z))
def sigmoid(z):
    return 1/(1 + np.exp(-z))


#Gradient Descent
def dW(X, Y):
    return (1/m)*np.dot(A-Y, X.T)

def dB(X, Y):
    return (1/m)*np.sum(A - Y)

def graphPoints():
    # graph
    # X-axis for Exam 1 Score
    # Y-axis for Exam 2 Score, + for admitted, o for not admitted
    exam1_scores = df['exam1'].values
    exam2_scores = df['exam2'].values
    admitted = df[df['status'] == 1]['exam1'].values
    not_admitted = df[df['status'] == 0]['exam1'].values

    plt.scatter(x = exam1_scores, y = exam2_scores, c='blue', label='All Data', s=70)
    plt.scatter(x = admitted, y = exam2_scores[df['status'] == 1], c='green', marker='o', label='Admitted', alpha = 0.80, s=50)
    plt.scatter(x = not_admitted, y = exam2_scores[df['status'] == 0], c='red', marker='x', label='Not Admitted', alpha= 0.80, s=50)

    plt.xlabel('Exam 1 Score')
    plt.ylabel('Exam 2 Score')
    plt.title('Exam Scores vs. Admission Status')

    # Add legend
    plt.legend()
    plt.show()

def graphCost():
    # plot of the cost function
    plt.plot(cost_list)
    plt.xlabel('iteration')
    plt.ylabel('Cost')
    plt.title('Cost value in each iteration')
    plt.show()

def inequality(x1, x2):
    b = (-1)*B
    m1 = W[0][0]
    m2 = W[1][0]
    return m1*x1 + m2*x2 >= b

def decisionBoundary():
    m1 = (-1)*W[0][0] / W[1][0]
    b = (-1)*B / W[1][0]

    # x2 >= m1x1 + b
    x = np.linspace(0, 100, 100)
    y = m1 * x + b


    exam1_scores = df['exam1'].values
    exam2_scores = df['exam2'].values
    admitted = df[df['status'] == 1]['exam1'].values
    not_admitted = df[df['status'] == 0]['exam1'].values

    plt.scatter(x = admitted, y = exam2_scores[df['status'] == 1], c='green', marker='o', label='Admitted', alpha = 0.80, s=50)
    plt.scatter(x = not_admitted, y = exam2_scores[df['status'] == 0], c='red', marker='x', label='Not Admitted', alpha= 0.80, s=50)


    plt.plot(x, y)
    plt.xlabel("exam1 score")
    plt.ylabel("exam2 score")
    plt.title("Decision Boundary")
    plt.show()





#call functions
m = X_train.shape[1] # 100
n = X_train.shape[0] # 2

W = np.zeros((n, 1)) #weight on exam1 and exam2, w1=0 w2=0
B = 0 # bias

learningRate = 0.0011
epochs = 999999
cost_list = []



for i in range(epochs):

    Z = np.dot(W.T, X_train) + B
    A = sigmoid(Z)

    W = W - learningRate*dW(X_train, Y_train).T
    B = B - learningRate*dB(X_train, Y_train)

    cost = -(1/m)*np.sum( Y_train*np.log(A) + (1-Y_train)*np.log(1-A))
    print(cost)
    cost_list.append(cost)

    if i > 2:
        temp_error = cost_list.__getitem__(i-1)
        if cost < 0.25 and abs(temp_error - cost_list.__getitem__(i)) < 0.00001:
            print('Small Differences')
            break

    
print("W is ", W) # w1 = 0.0.10089014 w2 = 0.09509842
print("B is ", B) # B = -11.970399906571215
print("Cost function is ", cost_list.pop()) #0.24999996992122817

graphPoints()
graphCost()
decisionBoundary()

X_test = [[100],[50]]
Z = np.dot(W.T, X_test) + B
A = sigmoid(Z)
print("Admission probability is ", A)



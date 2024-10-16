import pandas as pd
import matplotlib.pyplot as plt

# read csv file
path = "C:\\...\\linear-regression.train.csv" #enter path of where the csv file is
col_names = ['x', 'y']
data = pd.read_csv(path, header=None, names=col_names)

# calculate the least square (1/2m) * sum(h(xi)-yi)^2
def cost_function(b, m, points):
    sum = 0
    for i in range(len(points)):
        x = points.iloc[i].x
        y = points.iloc[i].y
        sum += (b + m*x - y) ** 2
    return (1/(2 * len(points))) * sum

# calculate m_gradient descent
def m_gradient(b, m, points):
    sum = 0
    n = len(points)
    for i in range(n):
        x = points.iloc[i].x
        y = points.iloc[i].y
        sum += (b + m*x - y) * x
    return (1/n) * sum

# calculate b_gradient descent
def b_gradient(b, m, points):
    sum = 0
    n = len(points)
    for i in range(n):
        x = points.iloc[i].x
        y = points.iloc[i].y
        sum += (b + m*x - y)
    return (1/n) * sum

m = 1
b = 1
L = 0.001
epochs = 100
square_error = []
temp_error = 99999
for i in range(epochs):
    square_error.append(cost_function(b, m, data))

    new_m = m - L * m_gradient(b, m, data)
    new_b = b - L * b_gradient(b, m, data)

    m = new_m
    b = new_b

    if i > 2:
        temp_error = square_error.__getitem__(i-1)
        if abs(temp_error - square_error.__getitem__(i)) < 0.001:
            print('Small Differences')
            break

print('Least Squares Error: ', cost_function(b, m, data))
print('m = ', m, 'b = ', b)

# plot of the least square error
plt.plot(square_error)
plt.xlabel('iteration')
plt.ylabel('least squares error')
plt.title('Least squares error in each iteration')
plt.show()

# scatter plot of data
plt.scatter(x = data.x, y = data.y, color = 'blue')
plt.plot(range(0, 10), [m * x + b for x in range(0, 10)], color="red")
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Linear Regression Model')
plt.show()

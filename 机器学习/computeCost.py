from matplotlib import pyplot as plt
import numpy as np
import math

# 梯度下降算法
def computeCost(X, y, theta):
    inner = np.power(((X * theta.T)-y),2)
    return np.sum(inner) / (2 * len(X))

# 正规方程
def normalEqn(X,y):
    theta = np.linalg.inv(X.T@X)@X.t@y  # X.T@X等价于X.T.dot(X)
    return theta

#
def cost(theta, X, y):
    theta = np.matrix(theta)
    X = np.matrix(X)
    y = np.matrix(y)
    # first =

def sigmoid_function(z):
    fz = []
    for num in z:
        fz.append(1/(1 + math.exp(-num)))
    return fz

if __name__ == '__main__':
    x = -math.log(1/(1+math.e**-1),10)
    print(x)
    # z = np.arange(-10, 10, 0.01)
    # fz = sigmoid_function(z)
    # plt.title('Sigmoid Function')
    # plt.xlabel('z')
    # plt.ylabel('σ(z)')
    # plt.plot(z, fz)
    # plt.show()



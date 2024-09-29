import numpy 
import math
import numpy as np
import matplotlib.pyplot as plt

x = np.array([[0.697,0.460],[0.774,0.376],[0.634,0.264],[0.608,0.318],[0.556,0.215],[0.403,0.237],[0.481,0.149],[0.437,0.211],[0.666,0.091],
            [0.243,0.267],[0.245,0.057],[0.343,0.099],[0.639,0.161],[0.657,0.198],[0.360,0.370],[0.591,0.042],[0.719,0.103]])
y = np.array([1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0])

ones1 = np.array([[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]])
ones1 = ones1.T
x1 = np.concatenate((x,ones1),axis = 1)
beta = np.array([1,1,1])
n = 1000;

def func_sigmod(beta,x0):
    y = math.exp(np.dot(beta,x0))/(1+math.exp(np.dot(beta,x0)))
    return y

for k  in range(0,n):
    B1 = 0
    for j in range(len(x)):
        B1 = B1 - x1[j,:]*(y[j] - func_sigmod(beta,x1[j,:]))
    B2 = 0
    for j in range(len(x)):
        B2 = B2 + (x1[j,:]**2).sum()*func_sigmod(beta,x1[j,:])*(1 - func_sigmod(beta,x1[j,:]))
    beta = beta - 1/B2*B1
print(beta)
f1 = plt.figure(1)
plt.title('watermelon_chapter3-3')
plt.xlabel('density')
plt.ylabel('ratio_sugar')
plt.scatter(x[y==1,0],x[y==1,1],marker = '+',color = 'r',s = 100,label = 'good')
plt.scatter(x[y==0,0],x[y==0,1],marker = '*',color = 'b',s = 100,label = 'bad')
plt.show()


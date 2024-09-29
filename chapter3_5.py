import numpy as np
import math
import matplotlib.pyplot as plt


data_miu_g_density = (0.697 + 0.774 + 0.634 + 0.608 + 0.556 + 0.403 + 0.481 + 0.437)/8
data_miu_g_sugar = (0.460 + 0.376 + 0.264 + 0.318 + 0.215 + 0.237 + 0.149 + 0.211)/8
miu_g = np.array([data_miu_g_density,data_miu_g_sugar])

data_miu_b_density = (0.666 + 0.243 + 0.245 + 0.343 + 0.639 + 0.657 + 0.360 + 0.593 + 0.719)/9
data_miu_b_sugar  = (0.091 + 0.267 + 0.057 + 0.099 + 0.161 + 0.198 + 0.370 + 0.042 + 0.103)/9
miu_b = np.array([data_miu_b_density,data_miu_b_sugar])

x_g = np.array([[0.697,0.460],[0.774,0.376],[0.634,0.264],[0.608,0.318],[0.556,0.215],[0.403,0.237],[0.481,0.149],[0.437,0.211]])
x_b = np.array([[0.666,0.091],[0.243,0.267],[0.245,0.057],[0.343,0.099],[0.639,0.161],[0.657,0.198],[0.360,0.370],[0.593,0.042],[0.719,0.103]])

Sw = 0
for i in range(len(x_g)):
    a = (x_g[i] - miu_g)
    a = a.reshape(len(a),1)
    b = a.reshape(1,len(a))   
    Sw = Sw + np.dot(a,b)
for j in range(len(x_b)):
    b = (x_b[j] - miu_b)
    b = b.reshape(len(b),1)
    a = b.reshape(1,len(b))   
    Sw = Sw + np.dot(b,a)    
    
print(Sw)    
W = np.dot(np.linalg.pinv(Sw),miu_g - miu_b)
print(W)



w = W.flatten()
x1 = np.linspace(-1, 1, 102)
x2 = w[0] * x1 / w[1]
plt.plot(x1, x2, label="LDA")
plt.legend()
    #plt.savefig(r'C:\Users\hp\Desktop\《机器学习》笔记\LDA.png', dpi=300)
plt.show()

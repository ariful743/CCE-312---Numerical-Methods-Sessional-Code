
import numpy as np

x = np.array([    0.698132 , 0.959931, 1.134464, 1.570796,  1.919862  ])
y = np.array([    0.188224,  0.209138, 0.230052 , 0.250965 ,   0.313707 ])


# x = []
# a = int(input("Size of array:"))
# for i in range(a):
#     x.append(float(input("Element of x :")))
# x = np.array(x)


# y = []
# for i in range(a):
#     y.append(float(input("Element of y :")))
# y = np.array(y)




n = np.size(x)

m_x = np.mean(x)
m_y = np.mean(y)

SS_xy = np.sum(y*x) - n*m_y*m_x
SS_xx = np.sum(x*x) - n*m_x*m_x

a_1 = SS_xy / SS_xx
a_0 = m_y - a_1*m_x

print(a_0)
print(a_1)
print("y = " + str(round(a_0, 2)) + "+ " + str(round(a_1, 2)) + " x")


future = float(input())
print(a_0 + a_1* future)

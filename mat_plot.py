# -*- coding: utf-8 -*-
"""
Created on Mon May  8 09:44:39 2017

@author: user
"""

import matplotlib.pyplot as plt
import numpy as np
import mpl_toolkits.mplot3d # 3D 图库
import matplotlib.image as mplimg

t = np.arange(0,5,0.2)

plt.plot(t,t,'r--',t,t**2,'bs',t,t**3,'g^')

# DOUBLE Y
x = np.arange(0., np.e, 0.01)
y1 = np.exp(-x)
y2 = np.log(x)

fig = plt.figure()

ax1 = fig.add_subplot(111)
ax1.plot(x, y1)
ax1.set_ylabel('Y values for exp(-x)')
ax1.set_title("Double Y axis")

ax2 = ax1.twinx()  # this is the important function
ax2.plot(x, y2, 'r')
ax2.set_xlim([0, np.e])
ax2.set_ylabel('Y values for ln(x)')
ax2.set_xlabel('Same X for both exp(-x) and ln(x)')

plt.show()

# 3D图

x,y=np.mgrid[-2:2:20j,-2:2:20j]
z=x*np.exp(-x**2-y**2)
ax=plt.subplot(111,projection='3d')
ax.plot_surface(x,y,z,rstride=2,cstride=1,cmap=plt.cm.coolwarm,alpha=0.8)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.show()

# hist
t = np.arange(10)
fig = plt.figure()
ax = fig.add_subplot()
plt.hist(t,2*t+1)
plt.show()

# scarter
t = np.arange(10)
fig = plt.figure()
ax = fig.add_subplot()
plt.scatter(t,t*2+1)
plt.savefig("scatter.png")

# pie
t = np.arange(5)
fig = plt.figure()
ax = fig.add_subplot()
a=['A','B','C','D','F']
plt.pie(t,labels=a)
# plt.pie(t,labels=labels,autopct='%1.2f%%')

plt.show()

# inport image
img = mplimg.imread("stinkbug.png")

# print(img) read img information
lum_img =img[:,:,0]
imgplot =plt.imshow(lum_img)
imgplot.set_cmap('hot')
imgplot.set_cmap('spectral')
plt.colorbar()








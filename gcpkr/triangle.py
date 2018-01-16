

import numpy as np
import matplotlib.pyplot as plt
markers=['v','^','v','^','v','^','v','^']
#descriptions=['triangle_down','triangle_down']
# x=[]
# y=[]
# for i in range(20):
#     for j in range(20):
#         x.append(i)
#         y.append(j)
xs = np.linspace(-np.pi, np.pi, 30)
ys = np.sin(xs)
markers_on = [12, 17, 18, 19]
plt.plot(xs, ys )
for x,y,m in zip(xs,ys,markers):
# if x%2==0:
   plt.scatter(x, y,color='g',marker='v')
   plt.scatter(x, y,color='g',marker=m)

#plt.tight_layout()
#plt.axis('off')
plt.show()

#
# import matplotlib.pylab as plt
# markers=['v','^','v','^']
# descriptions=['triangle_down','triangle_down','triangle_down','triangle_down']
# x=[]
# y=[]
# for i in range(20):
#     for j in range(20):
#         x.append(i)
#         y.append(j)
# plt.figure()
# for i,j,m,l in zip(x,y,markers,descriptions):
#     plt.scatter(i,j,marker=m)
#     #plt.text(i-0.15,j+0.15,s=m+' : '+l)
# #plt.axis([-0.1,4.8,-0.1,4.5,10,15,20])
# plt.tight_layout()
# plt.axis('off')
# plt.show()

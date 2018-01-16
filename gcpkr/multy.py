import numpy as np
import matplotlib.pyplot as plt
import random
fig=plt.figure()

fig, axes=plt.subplots(2,2, sharex=True, sharey=True)

for i in range(2):
    for j in range(2):
      axes[i,j].hist(random.randrange(1,500), bins=50, color='k', alpha=0.5)

    # 서브플롯 간 간격 조절하기
plt.subplots_adjust(wspace=0, hspace=0)
plt.show()
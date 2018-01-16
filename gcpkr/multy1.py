import matplotlib.pyplot as plt
import numpy as np

# x 좌표는 0부터 0.01씩 더해져 최대 5까지
x = np.arange(0.0, 5.0, 0.01)
# y = x^2 그래프
plt.subplot(211)
plt.plot(x, x ** 2, 'r--')
# y = 2^x 그래프
plt.subplot(212)
plt.plot(x, 2 ** x, 'b-')

# # y = x
# plt.subplot(223)
# plt.plot(x, x, 'g')
#
# # y = 1/(x+1)
# plt.subplot(224)
# plt.plot(x, 1 / (x + 1))
#
# plt.subplot(224)
# plt.plot(x, 1 / (x + 1))

plt.show()


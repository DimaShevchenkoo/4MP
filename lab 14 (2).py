import numpy as np
import matplotlib.pyplot as plt


fig, ax = plt.subplots()




x1 = np.linspace(0.9, 1.9)
y2 = np.linspace(1.7, 3.2)

ax.plot(x1, y2)
ax.grid()
plt.title('---')
plt.xlabel("x")
plt.ylabel("y")

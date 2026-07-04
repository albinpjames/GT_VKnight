# %%
import matplotlib.pyplot as plt
import numpy as np

# %%
x = np.linspace(0, 10, 100)
plt.plot(x, np.sin(x))
plt.title("My First Plot")
plt.grid(True)
plt.show()
# %%

import numpy as np
import matplotlib.pyplot as plt
import skimage.io as io

def fshs(x): 
    x_max = np.max(x)
    x_min = np.min(x)
    
    a = (255) / (x_max - x_min)
    b = x_min
    
    y = a * (x - b)
    
    return y

x = io.imread("spettro.jpg")

y = np.log(x + 1)

z = x ** 3
z = fshs(z)

fig, axes = plt.subplots(1, 3, figsize=(15, 5))

axes[0].imshow(x, clim=None, cmap="gray")
axes[0].set_title('Originale')

axes[1].imshow(y, clim=None, cmap="gray")
axes[1].set_title('Logaritmo')

axes[2].imshow(z, clim=None, cmap="gray")
axes[2].set_title('Potenza')

plt.tight_layout()
plt.show()

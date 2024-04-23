import numpy as np              # importa Numpy
import matplotlib.pyplot as plt # importa Matplotlib
import scipy.ndimage as ndi     # importa Scipy per le immagini
import skimage.io as io         # importa il modulo Input/Output di SK-Image

def medie(x, k):
    """
    Data un'immagine x fornisce l'immagine delle medie locali usando una finestra
    K x K
    """
    y = ndi.generic_filter(x, np.mean, (k,k))
    return y

x = io.imread("dorian.jpg")

y1 = medie(x, 3)
y2 = medie(x, 5)
y3 = medie(x, 7)
y4 = medie(x, 9)

fig, axes = plt.subplots(2, 2, figsize=(10, 10))

axes[0, 0].imshow(y1, clim=[0, 255], cmap="gray")
axes[0, 0].set_title('K = 3')

axes[0, 1].imshow(y2, clim=[0, 255], cmap="gray")
axes[0, 1].set_title('K = 5')

axes[1, 0].imshow(y3, clim=[0, 255], cmap="gray")
axes[1, 0].set_title('K = 7')

axes[1, 1].imshow(y4, clim=[0, 255], cmap="gray")
axes[1, 1].set_title('K = 9')

plt.tight_layout()
plt.show()

# più la finestratura è grande, meno è dettagliata l'immagine delle medie
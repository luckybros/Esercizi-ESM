# Il dataset risulta già suddiviso in due parti: un training set di 60.000 immagini e un test set di 10.000 
# immagini. Per ogni insieme sono state caricate due variabili. Ad esempio, per il training set si ha la 
# variabile y train che `e il vettore di 60.000 etichette e la variabile x train che è un array contentente 
# le 60.000 immagini.           # importa Numpy
import numpy as np 
import matplotlib.pyplot as plt # importa Matplotlib
from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical
from tensorflow import keras
from tensorflow.keras import layers  

(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_val   = x_train[::12]
y_val   = y_train[::12]
x_train = np.delete(x_train, np.arange(0, x_train.shape[0], 12), 0)
y_train = np.delete(y_train, np.arange(0, y_train.shape[0], 12), 0)

# Preparazione dei dati per la compatibilità con Keras:
# - Le immagini devono essere convertite in float a 32 bit.
# - Le immagini devono essere organizzate secondo la convenzione Channels-Last.
#   Questo significa che le immagini sono organizzate in un array di 4 dimensioni:
#   la prima dimensione per accedere alle immagini, seguita da righe e colonne,
#   e infine la banda (o canale) dell'immagine.
img_rows = 28
img_cols = 28
img_channels = 1

# reshape nel formato Channels-Last
x_train = np.reshape(x_train, (55000, img_rows, img_cols, img_channels))
x_val = np.reshape(x_val, (5000, img_rows, img_cols, img_channels))
x_test = np.reshape(x_test, (10000, img_rows, img_cols, img_channels))

# conversione a float e normalizzazione
x_train = np.float32(x_train) / 255
x_val = np.float32(x_val) / 255
x_test = np.float32(x_test) / 255

# Preparazione delle etichette nel formato One-Hot:
# Nel formato One-Hot, ogni etichetta viene rappresentata come un vettore
# la cui lunghezza è uguale al numero di classi presenti.
# Il vettore contiene tutti valori nulli eccetto un singolo 1 nella posizione
# relativa all'etichetta. Ad esempio, se il numero di classi è 10, 
# l'etichetta 8 sarà convertita nella sequenza 0000000010, mentre
# l'etichetta 0 sarà convertita in 1000000000.
# Usiamo la funzione keras.utils.to_categorical per convertire
# il vettore di etichette nel formato One-Hot.
num_classes = 10

# Conversione delle etichette nel formato One-Hot
y_train = to_categorical(y_train, num_classes)
y_val = to_categorical(y_val, num_classes)
y_test = to_categorical(y_test, num_classes)

# Rappresenta l’intera architettura ed a cui aggiungeremo man mano i vari strati tramite il metodo add
lenet = keras.models.Sequential()

lenet.add(layers.Conv2D(6, (5, 5), padding="same", activation="relu",
            input_shape=(img_rows,img_cols,img_channels)))

lenet.add(layers.MaxPooling2D((2, 2) ))

lenet.add(layers.Conv2D(16, (5, 5), padding="valid", activation="relu"))
lenet.add(layers.MaxPooling2D((2, 2) ))

lenet.add(layers.Flatten())

lenet.add(layers.Dense(120, activation="relu"))
lenet.add(layers.Dense(84, activation="relu"))
lenet.add(layers.Dense(num_classes, activation="softmax"))

lenet.summary()

# Addestramento
lenet.compile(loss = keras.losses.categorical_crossentropy,
          optimizer = keras.optimizers.SGD(lr=0.01),
          metrics = ["accuracy"])


lenet.fit(x_train, y_train, batch_size=200, epochs=10,
           validation_data=(x_val, y_val), verbose=True)

ID = 1000 # indice dell’immagine da analizzare
img   = x_test[ID]
label = y_test[ID]
img   = np.reshape(img, (-1,img_rows,img_cols,img_channels))
pred  = lenet.predict(img)
print("vettore delle probabilità predette:", pred)
plt.figure()
plt.imshow(img[0,:,:,0], cmap="gray", clim=[0,1])
plt.title("Etichetta vera: %d; Etichetta predetta: %d" %
                 (np.argmax(label), np.argmax(pred)))
plt.show()

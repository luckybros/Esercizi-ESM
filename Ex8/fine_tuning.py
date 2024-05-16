#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Esercizio 1.4.1.2
Dataset CIFAR-10. Utilizzate LeNet per la classificazione di oggetti 
adoperando il dataset CIFAR- 10 composto da 60.000 immagini 32 × 32 a 
colori di 10 classi (Aereo, Automobile, Uccello, Gat- to, Cervo, Cane, Rana, 
Cavallo, Barca, Camion). Potete caricare il dataset utilizzando la funzione 
keras.datasets.cifar10.load data.
"""

# !pip install --upgrade git+https://github.com/davin11/easy-cv-dataset keras-cv

# !wget -q -c https://www.grip.unina.it/download/guide_TF/TrafficSigns.zip
# !unzip -q -n TrafficSigns.zip

import matplotlib.pyplot as plt  # importa Matplotlib
import easy_cv_dataset as ds
import keras
from sklearn.model_selection import train_test_split
from keras_cv.layers import Resizing
from tensorflow.keras import layers
import skimage.io as io   

img0 = io.imread("TrafficSigns/train/mandatory/img0065_00.png")
img1 = io.imread("TrafficSigns/train/prohibition/img2929_00.png")
img2 = io.imread("TrafficSigns/train/warning/img2470_00.png")

plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.imshow(img0)
plt.title("mandatory")

plt.subplot(1, 3, 2)
plt.imshow(img1)
plt.title("prohibition")

plt.subplot(1, 3, 3)
plt.imshow(img2)
plt.title("warning")

plt.show()

train_table = ds.image_dataframe_from_directory("TrafficSigns/train")

display(train_table)

train_table, valid_table = train_test_split(train_table, test_size=0.2,
                                            random_state=34,
                                            stratify=train_table["class"])

batch_size = 8
img_height, img_width = 150, 150

train_dataset = ds.image_classification_dataset_from_dataframe(
    train_table,
    batch_size=batch_size,
    shuffle=True,
    pre_batching_processing=Resizing(img_height, img_width),
    post_batching_processing=None,
    do_normalization=True,
    class_mode="categorical"
)

test_dataset = ds.image_classification_dataset_from_dataframe(
    valid_table,
    batch_size=batch_size,
    shuffle=False,
    pre_batching_processing=Resizing(img_height, img_width),
    do_normalization=True,
    class_mode="categorical"
)

# ResNet50 pre-addestrata
base_model = keras.applications.ResNet50(
    weights="imagenet",
    include_top=False,
    input_shape=(img_width, img_height, 3)
)

model = keras.models.Sequential()
model.add(base_model)
model.add(layers.GlobalAveragePooling2D())
model.add(layers.Dense(3, activation="softmax"))

train_after_layer = 25
for layer in base_model.layers[:train_after_layer]:
    layer.trainable = False

model.compile(
    loss="categorical_crossentropy",
    optimizer=keras.optimizers.SGD(learning_rate=1e-4, momentum=0.9),
    metrics=["accuracy"]
)

model.fit(train_dataset, epochs=1, validation_data=test_dataset, verbose=True)

test_loss, test_accuracy = model.evaluate(test_dataset, verbose=True)
print("Test loss: ", test_loss)
print("Test accuracy: ", test_accuracy)


from keras_cv.layers import RandomBrightness, RandomRoom
augmenter = keras.Sequential(layers=[
        RandomBrightness(factor=(-0.1, 0.1), value_range=(0, 255)),
        RandomRoom((-0.2,0.2)),
])

train_dataset = ds.image_classification_dataset_from_dataframe( 
      train_table, 
      batch_size=batch_size, 
      shuffle=True, 
      pre_batching_processing=Resizing(img_height, img_width), 
      post_batching_processing=augmenter,
      do_normalization=True,
      class_mode="categorical"
)

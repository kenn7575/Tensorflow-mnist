import tensorflow as tf
import keras
import keras.datasets.mnist
import keras.layers
import numpy as np
#import pandas as pd
import matplotlib.pyplot as plt


from data_visualyzing import Visualyzation

# distrubute data
data = keras.datasets.mnist  # get data
(train_images, train_labels), (test_images,
                               test_labels) = data.load_data()  # asign data

train_images = train_images/255.0
train_images = train_images/255.0

# output categorie classes
class_names = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

model = keras.Sequential([
    # input layer 784/28*28 neurons
    keras.layers.Flatten(input_shape=(28, 28)),

    # hidden layer 128 neurons
    keras.layers.Dense(128, activation="relu"),

    # output layer 10 neurons
    keras.layers.Dense(10, activation="softmax")
])

# configures the model for training
model.compile(optimizer="adam",
              loss="sparse_categorical_crossentropy", metrics=["accuracy"])


# train model
model.fit(train_images, train_labels, epochs=15)

# evaluate model
test_loss, test_acc = model.evaluate(test_images, test_labels)

# hooray! the model is done.
# save model
model.save("digit_classifier.h5")


# lets test the model.
a = 1
while a == 1:
    num = int(input("pick an image "))
    predictions = model.predict(test_images)

    display = Visualyzation(num, predictions)
    display.visualyze2()

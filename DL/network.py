import numpy as np
from keras.layers.core import Activation, Dense, Dropout
from keras.models import Sequential
from keras.optimizers import SGD, Adam

import preprocess as prepro

batch_size = 64
nb_epoch = 100
data = None


def model_build():
    model = Sequential()

    model.add(Dense(512, input_shape=(12,)))
    model.add(Activation('relu'))
    model.add(Dropout(0.5))
    model.add(Dense(512))
    model.add(Activation('relu'))
    model.add(Dropout(0.5))
    model.add(Dense(18))
    model.add(Activation('softmax'))

    model.summary()


def model_train():
    model.compile(optimizer='adam',
                  loss='categorical_crossentropy', metrics=['accuracy'])
    model.fit(X_train, Y_train, batch_size=batch_size,
              nb_epoch=nb_epoch, verbose=1, validation_split=0.2)


def model_predict():
    None

if __name__ == '__main__':
    data = prepro.csv_load()
    for x in data:
        print(x)
    print()
    model_build()

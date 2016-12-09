import preprocess as prepro
import numpy as np
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation
from keras.optimizers import SGD, Adam


batch_size = 64
nb_epoch = 100


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

if __name__ == '__main__':
    
    model_build()

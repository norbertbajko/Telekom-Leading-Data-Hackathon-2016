import numpy as np
from keras.callbacks import EarlyStopping, ModelCheckpoint
from keras.layers.core import Activation, Dense, Dropout
from keras.models import Sequential
from keras.optimizers import SGD, Adam

import preprocess as pp

batch_size = 32
nb_epoch = 10000


def model_build():
    model = Sequential()

    model.add(Dense(256, input_shape=(12,)))
    model.add(Activation('relu'))
    model.add(Dropout(0.5))
    model.add(Dense(256))
    model.add(Activation('relu'))
    model.add(Dropout(0.5))
    model.add(Dense(9))
    model.add(Activation('softmax'))

    model.summary()
    return model


def model_train(model, X, Y):
    checkpoint = ModelCheckpoint(filepath, monitor='val_acc', verbose=0,
                                 save_best_only=True, mode='auto')
    early_stopping = EarlyStopping(monitor='val_acc', min_delta=0.005, patience=50, mode='auto')
    model.compile(optimizer='adam',
                  loss='categorical_crossentropy', metrics=['accuracy'])
    model.fit(X, Y, batch_size=batch_size,
              nb_epoch=nb_epoch, verbose=1, validation_split=0.2, callbacks=[early_stopping, checkpoint])


def model_predict():
    None

if __name__ == '__main__':
    data_x, data_y = pp.prepare_for_train(pp.aggregate(pp.csv_load()))

    model = model_build()
    model_train(model, data_x, data_y)

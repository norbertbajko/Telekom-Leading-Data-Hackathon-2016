import numpy as np
from keras.callbacks import EarlyStopping, ModelCheckpoint
from keras.layers.core import Activation, Dense, Dropout
from keras.models import Sequential
from keras.optimizers import SGD, Adam

import preprocess as pp

batch_size = 64
nb_epoch = 10000


def model_build():
    model = Sequential()

    model.add(Dense(512, input_shape=(12,)))
    model.add(Activation('relu'))
    model.add(Dropout(0.5))
    model.add(Dense(512))
    model.add(Activation('relu'))
    model.add(Dropout(0.5))
    # model.add(Dense(128))
    # model.add(Activation('relu'))
    # model.add(Dropout(0.5))
    model.add(Dense(9))
    model.add(Activation('softmax'))

    # model.load_weights("weights/weights-batch_size:32-dense:256_512-732-0.31.hdf5")

    # model.summary()

    return model


def model_train(model, X, Y):
    checkpoint = ModelCheckpoint(
        filepath="weights/weights-batch_size:" + str(batch_size) + "-{epoch:02d}-{val_acc:.2f}.hdf5", monitor='val_acc', verbose=0, save_best_only=True, mode='auto')
    early_stopping = EarlyStopping(monitor='val_acc', min_delta=0.005, patience=200, mode='auto')
    model.compile(optimizer='adam',
                  loss='categorical_crossentropy', metrics=['accuracy'])
    model.fit(X, Y, batch_size=batch_size,
              nb_epoch=nb_epoch, verbose=2, validation_split=0.2, callbacks=[early_stopping, checkpoint])


def model_predict(model, m, f, a, days, city)
    coordinates = {}
    pp.load_hungarian_coordinates()
    city = coordinates[city]
    lat = city[0]
    lon = city[1]

    max_lat = 48.58512448
    min_lat = 45.73711415
    max_lon = 22.89696693
    min_lon = 16.11411095

    norm_lat = (lat - min_lat) / (max_lat - min_lat)
    norm_lon = (lon - min_lon) / (max_lon - min_lon)

    tmp = [m, f, a]
    for element in days:
        tmp.append(element)
    tmp.append(norm_lat)
    tmp.append(norm_lon)

    results = model.predict(tmp, batch_size=1, verbose=0)
    return results

if __name__ == '__main__':
    data_x, data_y = pp.prepare_for_train(pp.aggregate(pp.csv_load()))

    model = model_build()
    model_train(model, data_x, data_y)

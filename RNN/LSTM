from keras.models import Sequential
from keras.layers import  LSTM
from keras.layers import Dense, Dropout
from keras.optimizers import Adam
import keras

(X_train, y_train), (X_test, y_test) = keras.datasets.mnist.load_data()
X_train = keras.utils.normalize(X_train, axis=1)
X_test = keras.utils.normalize(X_test, axis=1)

model = Sequential()
#model.add(tf.keras.layers.Flatten())

model.add(LSTM(128, input_shape=(X_train.shape[1:]),activation='relu', return_sequences=True))
model.add(Dropout(0.2))

model.add(LSTM(128, activation='relu'))
model.add(Dropout(0.2))

model.add(Dense(32, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(10, activation='softmax'))

opt = Adam(lr=1e-3, decay=1e-5)
model.compile(loss='sparse_categorical_crossentropy', optimizer=opt, metrics=['accuracy'])
model.fit(X_train, y_train, epochs=3, validation_data=(X_test, y_test))



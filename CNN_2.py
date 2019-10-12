import keras
from keras.model import Sequential
from keras.layer import Activation
from keras.layer.core import Activation

model = Sequential([Dense(16, input_shape=(1,), activation= 'relu'),
                    Dense(32, activation='relu'),
                    Dense(2, activation= 'relu')])

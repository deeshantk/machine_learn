import pickle
from keras.models import Sequential
from keras.layers import Activation, Conv2D, Flatten, MaxPooling2D, Dense
from keras.callbacks import TensorBoard

name = 'dogs_vs_dogs'
tensorboard = TensorBoard(log_dir='logs/{}'.format(name))

pickle_in = open("X.pickle","rb")
X = pickle.load(pickle_in)

pickle_in = open("y.pickle","rb")
y = pickle.load(pickle_in)

X = X/255.0

model = Sequential()
model.add(Conv2D(64, (3,3), input_shape= X.shape[1:]))
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Conv2D(64, (3,3), input_shape= X.shape[1:]))
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Flatten())

model.add(Dense(64))
model.add(Activation("relu"))

model.add(Dense(1))
model.add(Activation('sigmoid'))

model.compile(loss='binary_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

model.fit(X, y,batch_size=32,epochs=10,validation_split=0.1, callbacks=[tensorboard])


model.save('CNN.model')

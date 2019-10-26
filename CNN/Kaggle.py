import pandas as pd
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
path = '/Users/deeshantkotnala/Downloads/All_for_data/digit-recognizer/train.csv'
data = pd.read_csv(path)
y_train = data['label']

X_train = data.drop('label', axis=1, inplace=False)
X_train = X_train/255
X_train = X_train.values.reshape(-1, 28, 28, 1)

model = Sequential()
model.add(Conv2D(32, (5,5), activation='relu', input_shape=X_train.shape[1:]))

model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(128, (5, 5), activation='relu',))

model.add(Conv2D(128, (3,3), activation='relu',))

model.add(Flatten())
model.add(Dense(256, activation='relu'))
model.add(Dense(128, activation='relu'))

model.add(Dense(10, activation='softmax'))


model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

#print(model.summary())

model.fit(X_train, y_train, epochs=3, validation_split=0.1)
model.save('kaggle.model')

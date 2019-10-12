import os
import random
import cv2
import pickle
import matplotlib.pyplot as plt

datadir = "path_here"
#print(os.listdir(datadir))          #Just to show whats inside

CATAGORIES = ["dogs","cats"]

IMG_SIZE = 50


training_data = []
def create_trainin_data():
    for catagories in CATAGORIES:
        path = os.path.join(datadir, catagories)
        class_num = CATAGORIES.index(catagories)
        for img in os.listdir(path):
            try:
                img_array = cv2.imread(os.path.join(path, img), cv2.IMREAD_GRAYSCALE)
                new_array = cv2.resize(img_array,(IMG_SIZE,IMG_SIZE))
                '''
                # If you want see how the image looks 
                plt.imshow(new_array,cmap='grey')
                plt.show()
                '''
                training_data.append([new_array,class_num])
            except Exception as e:
                pass

create_trainin_data()

random.shuffle(training_data)  #Just to shuffle the traning data so that our neutal net can get shuffled data to make hypo.

X, y = [], []
for features, label in training_data:
    X.append(features)
    y.append(label)

# To save our training data.
pickle_out = open("X.pickle","wb")
pickle.dump(X, pickle_out)
pickle_out.close()

pickle_out = open("y.pickle","wb")
pickle.dump(y, pickle_out)
pickle_out.close()

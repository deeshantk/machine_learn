from sklearn.preprocessing import MinMaxScaler
import numpy as np
l  = np.array([1,2,3])
print(l)
data = MinMaxScaler(feature_range=(0,1)) # This will make the data in the range of 0 to 1.
l1 = data.fit_transform(l.reshape(-1,1)) # Data needs to be reshaped into 1X1 as for our data.

print(l1)

import pandas as pd
from sklearn.tree import DecisionTreeRegressor
file_path = 'data.csv' # Your file path comes here. A sample data is also given in repository.
data = pd.read_csv(file_path) # Reads the data and stores it in data.
print(data.describe()) # Prints outs the summery of the data.
print(data.columns). # This will print out the first column of the data.

y = data.Price

data_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude'] 

x = data[data_featuers] 

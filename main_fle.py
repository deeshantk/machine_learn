import pandas as pd
from sklearn.tree import DecisionTreeRegressor
file_path = 'data.csv' # Your file path comes here. A sample data is also given in repository.
data = pd.read_csv(file_path) # Reads the data and stores it in data.
print(data.describe()) # Prints outs the summery of the data.
print(data.columns). # This will print out the first column of the data.

y = data.Price # Target for prediction.

data_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude'] # Features for target prediction.

x = data[data_featuers] 

data_model = DecisionTreeRegressor(random_state = 1)
data_model.fit(x,y) # Train model.
print('Lets make prediction for first 5 houses')
print(X.head())
print(data_model.predict(X.head())) # Predict the value of target according to features.

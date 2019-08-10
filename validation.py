from sklearn.metrics import mean_absolute_error
import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split

'''This part of the code is same as before.


file_path ='/Users/deeshantkotnala/Desktop/project/data.csv'

data = pd.read_csv(file_path)
print(data.describe())
print(data.columns)
y = data.Price

data_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']

X = data[data_features]
print(X.describe())
data_model = DecisionTreeRegressor(random_state = 1)
data_model.fit(X,y)

print('Lets make prediction for first 5 houses')
print(X.head())
print(data_model.predict(X.head())) 
'''

predicted_prices = data_model.predict(X) 
print(mean_absolute_error(y, predicted_prices)) 

# split data into training and validation data, for both features and target
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state = 0) # Define model
data_model = DecisionTreeRegressor(random_state = 0) # Fit model
data_model.fit(train_X, train_y)
val_prediction = data_model.predict(val_X)
print(mean_absolute_error(val_y, val_prediction))

import pandas as pd

file_path = 'data.csv' # Your file path comes here. A sample data is also given in repository.
data = pd.read_csv(file_path) # Reads the data and stores it in data.
print(data.describe()) # Prints outs the summery of the data.
print(data.columns). # This will print out the first column of the data.

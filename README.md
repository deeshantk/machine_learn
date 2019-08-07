# machine_learn

The python library used on line 1 is pandas which is used to store data. You can learn more about it here - https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html 

On line 5, discribe() is used which is a feature of pandas. The data shown by it is-

The first number, the count, shows how many rows have non-missing values.
Missing values arise for many reasons.
The second value is the mean, which is the average. Under that, std is the standard deviation, which measures how numerically spread out the values are.

To interpret the min, 25%, 50%, 75% and max values, imagine sorting each column from lowest to highest value. The first (smallest) value is the min. If you go a quarter way through the list, 
you'll find a number that is bigger than 25% of the values and smaller than 75% of the values. That is the 25% value (pronounced "25th percentile"). The 50th and 75th percentiles are defined analogously, 
and the max is the largest number.


# Selecting data for modeling
Sometimes your data have too many variables to wrap up so, we need to look to each column of the data. This is done with column property which can be seen in line number 6.

# Selecting the target which needs to be predicted later
For this we can select the column with a dot (.) and store it in a variable which will be called prediction target. Generall, we take the variable as y which is done in line number 8. 

Now that we have choosen the target to be predicted, we now have to choose the features which will decide the the prediction.
# Choosing the features
Here, we will choose the columns that will be used to make predictions.
All columns can be used here other than the one we have to predict the value of.
We can select multiple featres by making a list of columns as done in line number 10.

On line number 12, the variable x will store the data of only the features the we selected on line 10.

# Building the model
Scikit-learn is easily the most popular library for modeling the types of data typically stored in DataFrames.

The steps to building and using a model are:
1) Define: Here we have to define the data like what type of model will it be? A decision tree? Some other type of model? Some other parameters of the model type are specified too.
2) Fit: Capture patterns from provided data. This is the heart of modeling.
3) Predict: It will predict the value against the data we have provided to it.
4) Evaluate: Determine how accurate the model's predictions are.

We will define a decision tree model with scikit-learn and fit it with features and target which is done in line 14.
The libery for scikit-learn is on line 2. It is written as sklearn in program.

# Decision Tree
Decision tree builds regression or classification models in the form of a tree structure. It breaks down a dataset into smaller and smaller subsets while at the same time an associated decision tree is incrementally developed. The final result is a tree with decision nodes and leaf nodes. A decision node (e.g., Outlook) has two or more branches (e.g., Sunny, Overcast and Rainy), each representing values for the attribute tested. Leaf node (e.g., Hours Played) represents a decision on the numerical target. The topmost decision node in a tree which corresponds to the best predictor called root node. Decision trees can handle both categorical and numerical data. 

Now we have fitted the model and can proceed to the prediction.

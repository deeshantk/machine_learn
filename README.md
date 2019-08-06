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

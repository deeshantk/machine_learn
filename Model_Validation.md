# Model validation
Now that we have trained our model, we'd like to know how accurate it is?
Here error = actual_value − predicted_value. That means that if the cost was 100,000 and you predicted it 50,000 then the error will be 100,000 - 50,000 = 50,000.
To summerise model accuracy, we'd use mean apsolute error (MAE). With the MAE metric, we take the absolute value of each error. This converts each error to a positive number. We then take the average of those absolute errors. This is our measure of model quality.
On line 1, the library used is for measuring mena_apsolute_error.
Line 29 will print the error in prediction and real price values.

# The problem with in sample 
The value we calculated is called in sample score but it is not good everytime. Imagine if we calculated price by recognising pattern in a data but when we apply that model to a new data, which doesn't hold that patter, the model will be very inaccurate. So we always test our model on some new data.The most straightforward way to do this is to exclude some data from the model-building process, and then use those to test the model's accuracy on data it hasn't seen before. This data is called validation data.

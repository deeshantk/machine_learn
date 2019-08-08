# Model validation
Now that we have trained our model, we'd like to know how accurate it is?
Here error = actual_value − predicted_value. That means that if the cost was 100,000 and you predicted it 50,000 then the error will be 100,000 - 50,000 = 50,000.
To summerise model accuracy, we'd use mean apsolute error (MAE). With the MAE metric, we take the absolute value of each error. This converts each error to a positive number. We then take the average of those absolute errors. This is our measure of model quality.

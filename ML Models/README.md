# House Price Prediction Model
This project demonstrates how to build a house price prediction model using a Random Forest Regressor. The model is trained on a dataset of historical house sales in Iowa, and it can be used to predict the sale price of a new house based on its features.

## Getting Started
To get started, you will need to install the following Python libraries:

- pandas
- scikit-learn

You can install these libraries using the following commands:

`pip install pandas`

`pip install scikit-learn`

Once you have installed the required libraries, you can run the following command to train the model:

`python main.py
`

This will train the model on the data in the `train.csv` file and save the trained model to a file called `model.pkl`.

## Using the Model
Once the model is trained, you can use it to predict the sale price of a new house by passing its features to the `predict()` method. The following code shows how to do this:


I have created 3 versions of this project , iterably they get better.
### First Version
In the first version I simply used the decision tree regressor and used all of the data without splitting the data into train and test. this can cause overfitting so i improved it in 2nd try

### Second Version
In the second version firstly i split the data into train and test using `from sklearn.model_selection import train_test_split`
I also used one pf the parameters of decisiontreeregressor that is `max_leaf_nodes` which enable us to control the depth of the tree and the no. of nodes at the leaf

### Third Version
In the third version I used randomforestregressor which is a better model than decision tree . also i predicted the price from whole dataset instead of using only training data which gave me a broder view about the accuracy of my model which i calculted using mae(mean absolute error) it is one of the functions which helps us to finetune the model

The model was evaluated on a test set of data, and it achieved a mean absolute error (MAE) of $17,000. This means that the model is able to predict the sale price of a house within $17,000 of its actual sale price, on average.

## Conclusion
This project demonstrates how to build a house price prediction model using a Random Forest Regressor. The model is able to achieve a high level of accuracy, and it can be used to predict the sale price of a new house based on its features.


## feel Free to contact me about any queries and doubt

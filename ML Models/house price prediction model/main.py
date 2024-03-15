# # -------------------------------------------Without Splitting the data--------------------------------------------------
# import pandas as pd

# iowa_file_path = "E:/Python/house predection model/data/train.csv"
# try:
#     iowa_data = pd.read_csv(iowa_file_path)
# except FileNotFoundError as e:
#     print(f"Error: {e}. Please check the file path and permissions.")

# iowa_data.columns
# # iowa_data = iowa_data.dropna(axis=0)

# y = iowa_data.SalePrice

# iowa_features = ['LotArea', 'YearBuilt', '1stFlrSF', '2ndFlrSF', 'FullBath', 'BedroomAbvGr', 'TotRmsAbvGrd']

# X = iowa_data[iowa_features]

# # print(X.describe)
# # print(X.head)

# from sklearn.tree import DecisionTreeRegressor

# iowa_model = DecisionTreeRegressor(random_state=1)
# iowa_model.fit(X,y)

# # predictions = iowa_model.predict(X)

# print("First in-sample predictions:", iowa_model.predict(X.head()))
# print("Actual target values for those homes:", y.head().tolist())
# # print(predictions)

# # print(predictions[:5]) 
# # print(y.head())









# #---------------------------------------------By Splitting the data---------------------------------------------------
# import pandas as pd

# iowa_file_path = "E:/Python/house predection model/data/train.csv"
# iowa_data = pd.read_csv(iowa_file_path)

# y = iowa_data.SalePrice
# iowa_features = ['LotArea', 'YearBuilt', '1stFlrSF', '2ndFlrSF', 'FullBath', 'BedroomAbvGr', 'TotRmsAbvGrd']
# X = iowa_data[iowa_features]

# from sklearn.model_selection import train_test_split
# train_X , test_X , train_y , test_y = train_test_split(X,y, random_state=1)

# from sklearn.tree import DecisionTreeRegressor 
# iowa_model = DecisionTreeRegressor(random_state=1)
# iowa_model.fit(train_X,train_y)

# # val_predictions = iowa_model.predict(test_X)
# # print the top few validation predictions along with their corresponding actual values
# print("First in-sample predictions:", iowa_model.predict(test_X.head()))
# print("Actual target values for those homes:", test_y.head().tolist())

# from sklearn.metrics import mean_absolute_error
# test_predictions = iowa_model.predict(test_X)
# print(mean_absolute_error(test_y, test_predictions))

# def get_mae(max_leaf_nodes, train_X, test_X, train_y, test_y):
#     model = DecisionTreeRegressor(max_leaf_nodes=max_leaf_nodes, random_state=0)
#     model.fit(train_X, train_y)
#     preds_test = model.predict(test_X)
#     mae = mean_absolute_error(test_y, preds_test)
#     return(mae)

# candidate_max_leaf_nodes = [5, 25, 50, 100, 250, 500]
# # Write loop to find the ideal tree size from candidate_max_leaf_nodes
# for max_leaf_nodes in candidate_max_leaf_nodes:
#         my_mae = get_mae(max_leaf_nodes, train_X, test_X, train_y, test_y)
#         print("Max leaf nodes: %d \t\t Mean Absolute Error: %d" %(max_leaf_nodes, my_mae))

# # Store the best value of max_leaf_nodes (it will be either 5, 25, 50, 100, 250 or 500)
# best_tree_size = 100

# # now that we have found optimum leaf size so we will get more accurate results by using all of the data
# final_model = DecisionTreeRegressor(max_leaf_nodes=100,random_state=1)
# final_model.fit(X,y)





#-----------------------------------------------Using RandomForest Model------------------------------------------------
import pandas as pd

iowa_file_path = "E:/Python/house predection model/data/train.csv"
iowa_data = pd.read_csv(iowa_file_path)

y = iowa_data.SalePrice
iowa_features = ['LotArea', 'YearBuilt', '1stFlrSF', '2ndFlrSF', 'FullBath', 'BedroomAbvGr', 'TotRmsAbvGrd']
X = iowa_data[iowa_features]

from sklearn.model_selection import train_test_split
train_X , test_X, train_y, test_y = train_test_split(X,y,random_state=0)

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

# without specifying max_leaf_nodes
forest_model = RandomForestRegressor(random_state=1)
forest_model.fit(train_X, train_y)
iowa_predictions = forest_model.predict(test_X)
mae = mean_absolute_error(test_y, iowa_predictions)
print("Validation MAE when not specifying max_leaf_nodes:" ,mae)

#by specifying max_leaf_nodes
forest_model = RandomForestRegressor(max_leaf_nodes=100, random_state=1)
forest_model.fit(train_X,train_y)
iowa_predictions = forest_model.predict(test_X)
mae = mean_absolute_error(test_y , iowa_predictions)
print("Validation MAE for best value of max_leaf_nodes: ",mae)


# To improve accuracy, create a new Random Forest model which you will train on all training data
rf_model_full_data = RandomForestRegressor(random_state=1)
rf_model_full_data.fit(X,y)
predcs = rf_model_full_data.predict(X)
mae = mean_absolute_error(y , predcs)
print("Validation MAE for all data: ",mae)

# prediction on test file's data
test_data_path = "E:/Python/house predection model/data/test.csv"
test_data = pd.read_csv(test_data_path)
data = test_data[iowa_features]
test_predictions = rf_model_full_data.predict(data)
print(test_predictions)

output = pd.DataFrame({'Id': test_data.Id,
                       'SalePrice': test_predictions})
output.to_csv('submission.csv', index=False)
print(output)




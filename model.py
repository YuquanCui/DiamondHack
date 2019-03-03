import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn import preprocessing
import statsmodels.api as sm
from sklearn.model_selection import train_test_split


##############################
#### Load testing Data #######
##############################
test = pd.read_excel(r'Tasks_test.xlsx')
testDF = pd.DataFrame(data=test)
test_column_list = testDF.columns.values.tolist()
test_x_array = np.array(testDF[ [test_column_list[7], test_column_list[8], test_column_list[9], test_column_list[10] ] ] )

##########################################################
######  The dict that is going to be return by main ######
##########################################################
# id: [category_n, duration]
duration = {}
test_id_array = testDF['ID']
length = len(test_id_array)
#print(length)

for i in range(length):
    duration[i] = []

test_category_array = testDF['Category']
#print(test_category_array)
category_num = []

for category in test_category_array:
    if category == "School":
        category_num.append(2)
    elif category == "Personal":
        category_num.append(1)
    elif category == "Health":
        category_num.append(4)
    elif category == "Work":
        category_num.append(3)
#print(category_num)

for i in range(length):
    duration[i] = [ category_num[i] ]
#print(duration)

list = []
my_array = np.array([])
for key in duration:
    key_value = duration[key] #a list
    value = key_value[0]
    #print(value)
    list.append(value)
my_array = np.array(list)

testDF[ test_column_list[2] ] =  my_array
#print(testDF)

test_x_array = np.array(testDF[ [test_column_list[2], test_column_list[7], test_column_list[8], test_column_list[9], test_column_list[10] ] ] )
test_x_array_normalized = preprocessing.normalize(test_x_array)
test_x_array_normalized_df = pd.DataFrame(test_x_array_normalized)
#print(test_x_array_normalized_df)


##############################
### Load training data set ###
##############################
task = pd.read_csv(r'Tasks_Training.csv')
taskDF = pd.DataFrame(data=task)
column_list = taskDF.columns.values.tolist()

#print(taskDF)
##########################
######  Build Model ######
##########################

x_array = np.array(taskDF[ [ column_list[16], column_list[7], column_list[8], column_list[9], column_list[10] ] ] )
#print(x_array)
x_array_normalized = preprocessing.normalize(x_array)
#print(x_array_normalized)

x_array_normalized_df = pd.DataFrame(x_array_normalized)
#print(x_array_normalized_df)
y_df = taskDF[ [column_list[13]] ]
#print(y_df)

### Return a dict for each category ###
multi_regr = linear_model.LinearRegression()
multi_regr.fit(x_array_normalized_df, y_df)
predict_y = multi_regr.predict(test_x_array_normalized)
predict_y_list = predict_y.tolist()
#print(predict_y_list)

for key in duration:
    value_list = duration[key]
    #print (predict_y_list[key][0])
    value_list.append(predict_y_list[key][0])
print(duration)

def main():   
    return duration
    
if __name__ == "__main__":
    main()



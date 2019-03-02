import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn import preprocessing
import statsmodels.api as sm

####Load Input Data#####
event = pd.read_csv(r'Events_test.csv')
eventDF = pd.DataFrame(event, columns=['Event ID', 'Person', 'Name', 
'Category', 'Start Time', 'End date', 
'End Time', 'Repeat', 'Pattern'] )
#print(eventDF)

task = pd.read_csv(r'Tasks_Training.csv')
taskDF = pd.DataFrame(task, columns = ['ID', 'Name','Category', 'Start Date', 'Start Time',
'End date', 'End Time', 'Difficulty Level', 'Priority Level', 'Experience level',
'Interest Level', 'Due Date', 'Due Time', 'Duration', 'Mean', 'Std', 'Category_n'
])
print(taskDF)

###  Build Model ###
# without Start_Time
x_array = np.array(taskDF[['Category_n', 'Difficulty Level', 'Priority Level', 'Experience level', 'Interest Level']])
print(x_array)
#x_array_normalized = preprocessing.normalize([x_array])



### Model Evaluation ###



#if __name__ == '__main__':
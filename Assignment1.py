# Assignment 1 : Data preparation
# Download heart dataset from following link.
# https://www.kaggle.com/zhaoyingzhu/heartcsv
# Perform following operation on given dataset.
# 1. Find Shape of Data
# 2. Find Missing Values
# 3. Find data type of each column
# 4. Finding out Zero's
# 5. Find Mean age of patients
# 6. Now extract only Age, Sex, ChestPain, RestBP, Chol.
# Randomly divide dataset in training (75%) and testing (25%).
# Through the diagnosis test I predicted 100 report as COVID positive, but only 45 of those
# were actually positive. Total 50 people in my sample were actually COVID positive. I have
# total 500 samples. Create confusion matrix based on above data and find I. Accuracy II.
# Precision III. Recall IV. F-1 score
import numpy as np
import pandas as pd
dataFrame=pd.read_csv('/content/Heart.csv')
dataFrame.shape # shape
dataFrame.info()
dataFrame.head()
dataFrame.dtypes # datatype
dataFrame.isnull() # missing values
dataFrame.isnull().sum() # missing values : count
dataFrame.Age.mean() #mean of age
count = (dataFrame['Age'] == 0).sum() # counting zeros
count
# selected columns
var=dataFrame.loc[:,['Age','Sex','ChestPain','RestBP','Chol']]
var
# Splitting the dataset into train and test sets: 75-25 split
from sklearn.model_selection import train_test_split
X_train, X_test = train_test_split(var, test_size = 0.25, random_state = 42)
X_train.shape, X_test.shape
# Find accuracy and precision for given example
tp=45
fp=55
fn=05
tn=395
acc=(tp+tn)/(tp+fp+fn+tn)
pre=tp/(tp+fp)
rec=tp/(tp+fn)
print("Accuracy is : {}".format(acc))
print("Precision is : {}".format(pre))
print("Recall is : {}".format(rec))
print("F1-Score is : {}".format((2*pre*rec)/(pre+rec)))
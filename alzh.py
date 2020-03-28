import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
import random
from sklearn.model_selection import ShuffleSplit
from sklearn.model_selection import cross_validate
from imblearn.over_sampling import SMOTE
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.externals import joblib

data=pd.read_csv("indian_liver_patient.csv")
data=data.fillna(method="ffill")
data.Gender=data.Gender.map({"Female":1,"Male":0})
data["Dataset"]=data["Dataset"].map({1:0,2:1})
np.random.shuffle(data.values)
print(data.columns)


target=data["Dataset"]
source=data.drop(["Dataset"],axis=1)
sm=SMOTE()
sc=StandardScaler()
lr=LogisticRegression()
source=sc.fit_transform(source)
X_train,X_test,y_train,y_test= train_test_split(source,target,test_size=0.01)
X_train, y_train=sm.fit_sample(X_train,y_train)
cv=cross_validate(lr,X_train,y_train,cv=10)
print(cv)
joblib.dump(lr,"model4")




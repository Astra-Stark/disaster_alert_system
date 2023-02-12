import pandas as pd
import warnings
import pickle
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.model_selection import cross_val_score
from sklearn import model_selection
import math
import numpy as np
warnings.filterwarnings("ignore")
risk_data=pd.read_csv('flood.csv')
X=risk_data.drop('FLOODS',axis='columns')
Y=risk_data.FLOODS
X=np.array(X)
Y=np.array(Y)
model2 = DecisionTreeClassifier()
X_train, X_test, Y_train, Y_test=train_test_split(X,Y,random_state=10)
model2.fit(X_train,Y_train)
pickle.dump(model2,open('model2.pkl','wb'))
model2=pickle.load(open('model2.pkl','rb'))
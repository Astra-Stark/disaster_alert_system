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
risk_data=pd.read_csv('hailstorm.csv')
X1=risk_data.drop('PROB',axis='columns')
X=X1.drop('MAXSIZE',axis='columns')
Y=risk_data.PROB
X=np.array(X)
Y=np.array(Y)
X_train, X_test, Y_train, Y_test=train_test_split(X,Y,random_state=10)
Model = LinearRegression()
Model.fit(X_train, Y_train)
pickle.dump(Model,open('model1.pkl','wb'))
model1=pickle.load(open('model1.pkl','rb'))
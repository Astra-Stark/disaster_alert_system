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
risk_data=pd.read_csv('hh.csv')
# risk_data['Date'] = pd.to_datetime(risk_data['Date'],utc=True)
# risk_data['Date'] =pd.to_datetime(risk_data['Date']).dt.date
risk_data['Date'] = risk_data['Date'].str.replace('-', '')
risk_data['Date'] = risk_data['Date'].str.replace(':', '')
risk_data['Date'] = risk_data['Date'].str.replace('/', '')
risk_data['Date'] = risk_data['Date'].str.replace(' ', '')
print(risk_data[risk_data['Date'].isnull()])
risk_data['Date'] = pd.to_numeric(risk_data['Date'], errors='coerce')
risk_data= risk_data.dropna(subset=['Date'])
risk_data['Date'] = risk_data['Date'].astype(int)
risk_data=risk_data.head(20)
X=risk_data.drop('Magnitude',axis='columns')
Y=risk_data.Magnitude
X=np.array(X)
Y=np.array(Y)
X_train, X_test, Y_train, Y_test=train_test_split(X,Y,random_state=10)
Model = LinearRegression()
Model.fit(X_train, Y_train)
pickle.dump(Model,open('model.pkl','wb'))
model=pickle.load(open('model.pkl','rb'))
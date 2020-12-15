import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split


data = pd.read_csv("cc_approvals.csv")

print(data.isnull().values.sum())

# Tratamiento de datos nulos
data = data.replace("?",np.NaN)

#print(data.tail(17))

data = data.fillna(data.mean())

#print(data.isnull().values.sum())


print(data.info())

for col in data.columns:
    if data[col].dtypes == 'object':
        data[col] = data[col].fillna(data[col].value_counts().index[0])
        
#PREPROCESAMIENTO
from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()

#convirtiendo de nan a valores int
for col in data.columns:
    if data[col].dtype=='object':
        data[col]=le.fit_transform(data[col])        
print(data)

#FEACTURE SELECTION 
#DriversLicense and ZipCode SERAN ELIMINADOS
from sklearn.preprocessing import MinMaxScaler

data = data.drop([data.columns[10],data.columns[13]], axis=1)
print(data)       

data = data.values

X,y = data[:,0:13], data[:,13]

scaler = MinMaxScaler(feature_range=(0,1))
rescaledX = scaler.fit_transform(X)

#Entrenamiento y testeo
from sklearn.model_selection import train_test_split

# Split into train and test sets
X_train, X_test, y_train, y_test = train_test_split(rescaledX,
                                                    y,
                                                    test_size=0.20,
                                                    random_state=42)


from sklearn.linear_model import LogisticRegression

logreg = LogisticRegression()
logreg.fit(X_train,y_train)


# MATRIZ DE CONFUSION
from sklearn.metrics import confusion_matrix

y_pred = logreg.predict(X_test)

print("valor de presicion: ", logreg.score(X_test, y_test))
print(confusion_matrix(y_test, y_pred))
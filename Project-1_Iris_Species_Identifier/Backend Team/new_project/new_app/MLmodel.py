from pandas import *
from numpy import *
from seaborn import *
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import *
from sklearn.linear_model import *
from sklearn import metrics
from sklearn import preprocessing
def makePrediction(inp1, inp2, inp3, inp4):
    ds= get_dataset_names()
    ds=load_dataset("iris")
    X=ds.drop("species", axis=1)
    encoder= preprocessing.LabelEncoder()
    ds["species"]= encoder.fit_transform(ds["species"])
    Y=ds.species
    train_x,test_x,train_y,test_y=train_test_split(X,Y,test_size=0.2, random_state=3)
    model=KNeighborsRegressor()
    model.fit(train_x,train_y)
    model.predict(test_x)
    model.score(test_x,test_y)
    result = model.predict([[inp1, inp2, inp3, inp4]])
    if round(result[0])==0:
        return 'setosa'
    if round(result[0])==1:
        return 'versicolor'
    if round(result[0])==2:
        return 'viginica'
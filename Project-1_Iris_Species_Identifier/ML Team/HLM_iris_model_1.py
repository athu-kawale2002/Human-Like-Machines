from pandas import *
from numpy import *
from seaborn import *
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import *
from sklearn.linear_model import *
from sklearn import metrics
from sklearn import preprocessing

ds= get_dataset_names()

ds=load_dataset("iris")

ds.isnull()

X=ds.drop("species", axis=1)

Y=ds.species

encoder= preprocessing.LabelEncoder()
ds["species"]= encoder.fit_transform(ds["species"])
ds["species"].unique()
Y=ds.species

train_x,test_x,train_y,test_y=train_test_split(X,Y,test_size=0.2, random_state=3)

model=KNeighborsRegressor()

model.fit(train_x,train_y)

model.predict(test_x)
model.score(test_x,test_y)

model.predict([[1.2, 3.0, 2.1, 1]])
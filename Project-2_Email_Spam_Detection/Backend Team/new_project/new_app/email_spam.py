import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB


def email_spam_detection(string):
    # # Data gathering

    df=pd.read_csv("new_app\csv\spam.csv")

    df.head()

    df.describe()

    X = df.Message
    y = df.Category
    df.isna().sum()


    # # Data convertion to machine readable format

    label_encoder = preprocessing.LabelEncoder()
    df['Category']= label_encoder.fit_transform(df['Category'])


    # # Train and Test of data

    train_X, test_X, train_y, test_y = train_test_split(X, y, test_size=0.1)
    train_X.shape, test_X.shape, train_y.shape, test_y.shape

    # # Tokenizing the Input String

    model = CountVectorizer()
    train_count = model.fit_transform(train_X)
    test_count = model.transform([string])


    # # Classification

    clf = MultinomialNB()
    clf.fit(train_count, train_y)
    predictions = clf.predict(test_count)
    # # prediction
    return predictions[0]
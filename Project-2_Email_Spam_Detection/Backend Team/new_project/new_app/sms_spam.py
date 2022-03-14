import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB


def sms_spam_detection(string):
    # # Data Gathering

    df=pd.read_csv("new_app\csv\spamraw.csv")

    X = df.text
    y = df.type
    df.isna().sum()

    # # Data conversion to machine readable format

    label_encoder = preprocessing.LabelEncoder()
    df['type']= label_encoder.fit_transform(df['type'])


    # # Training and testing of Data

    train_X, test_X, train_y, test_y = train_test_split(X, y, test_size=0.2)
    train_X.shape, test_X.shape, train_y.shape, test_y.shape


    # # Tokenizing the input data

    model = CountVectorizer()
    train_count = model.fit_transform(train_X)
    test_count = model.transform([string])


    # # Classification

    clf = MultinomialNB()
    clf.fit(train_count, train_y)
    predictions = clf.predict(test_count)\

    # # Prediction final
    return predictions[0]
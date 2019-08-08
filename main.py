#!/usr/bin/env python
# coding: utf-8
import pandas as pd
import numpy as np
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt
import seaborn as sns
import graphviz
import pydotplus
import io
from scipy import misc
import imageio
from sklearn.tree import export_graphviz
from sklearn.metrics import accuracy_score

# # Spotify song attributes EDA
# - import dataset
# - EDA to visualize and observe structure
# - Train a classifier
# - Predict the target using the trained classifier
#


def main():
    data = pd.read_csv('data/data.csv')
    train, test = train_test_split(data, test_size=0.15)
    c = DecisionTreeClassifier(min_samples_split=200)
    features = ["danceability", "acousticness", "loudness", "valence",
                "instrumentalness", "key", "speechiness", "duration_ms"]
    X_train = train[features]
    y_train = train["target"]
    X_test = test[features]
    y_test = test["target"]
    dt = c.fit(X_train, y_train)
    y_pred = c.predict(X_test)
    score = accuracy_score(y_test, y_pred) * 100
    songs = test[y_pred == 1]["song_title"]
    print(type(songs))
    d = dict()
    d['songs'] = songs.to_json(orient='records')
    d['score'] = score

    return d

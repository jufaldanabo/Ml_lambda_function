""" This module contain the functions for tran model of machine learning """

import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.linear_model import SGDClassifier
from sklearn.datasets import load_iris


def load_dataset():
    """

    :return:
    """

    iris = load_iris()
    data = pd.DataFrame(data=np.c_[iris['data'], iris['target']],
                        columns=iris['feature_names'] + ['target'])
    data['target1'] = np.where(data['target'] == 2.0, 1, 0)

    return data


def train_test_split(df: pd.DataFrame) -> tuple:
    """

    :param df:
    :return:
    """

    x = np.array(df[['petal width (cm)', 'petal length (cm)']])
    y = np.array(df.target1)
    sss = StratifiedShuffleSplit(n_splits=1, test_size=0.3, random_state=0)
    for train_index, test_index in sss.split(x, y):
        x_train, x_test = x[train_index], x[test_index]
        y_train, y_test = y[train_index], y[test_index]

    return x_train, x_test, y_train, y_test


def feature_engineering(train_array: np.array, test_array: np.array) -> tuple:
    """

    :param test_array:
    :param train_array:
    :return:
    """
    scaler_ = StandardScaler()
    scaler_.fit(train_array)
    train_array = scaler_.transform(train_array)
    test_array = scaler_.transform(test_array)

    return train_array, test_array, scaler_


def tuning_knn(x_train: np.array, y_train: np.array) -> object:
    """

    :param x_train:
    :param y_train:
    :return:
    """

    clf_knn = KNeighborsClassifier()
    parameters = {'n_neighbors': [3, 4, 5, 6, 7], 'weights': ['uniform', 'distance']}

    clf_knn_gs = GridSearchCV(clf_knn, parameters, cv=3, scoring='f1_macro')
    clf_knn_gs.fit(x_train, y_train)

    return clf_knn_gs


def tuning_sgd(x_train: np.array, y_train: np.array) -> object:
    """

    :param x_train:
    :param y_train:
    :return:
    """

    clf_sgd = SGDClassifier()

    parameters = {'alpha': [10 ** -1, 10 ** -2], 'learning_rate': ['constant'], 'eta0': [0.1, 0.01, 0.001],
                  'penalty': ['l1', 'l2']}

    clf_sgd_gs = GridSearchCV(clf_sgd, parameters, cv=3, scoring='f1_macro')
    clf_sgd_gs.fit(x_train, y_train)

    return clf_sgd_gs


def selection_model(x_test: np.array, y_test: np.array, *args) -> object:
    scores = []
    for x in args:
        score_model = x.score(x_test, y_test)
        scores.append(score_model)
    max_index = scores.index(max(scores))
    model = args[max_index]
    return model


def create_model():
    """

    :return:
    """
    df = load_dataset()
    x_train, x_test, y_train, y_test = train_test_split(df)
    x_train, x_test, scaler_ = feature_engineering(x_train, x_test)
    model_knn = tuning_knn(x_train, y_train)
    model_sgd = tuning_sgd(x_train, y_train)
    model_f = selection_model(x_test, y_test, model_knn, model_sgd)

    return model_f, scaler_

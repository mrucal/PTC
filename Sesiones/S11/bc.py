# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 09:38:20 2017

@author: Mario
"""

from sklearn.cross_validation import train_test_split
from sklearn.datasets import load_breast_cancer
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import GaussianNB

bc = load_breast_cancer()

x_bc, y_bc = bc.data, bc.target

x_train, x_text, y_train, y_test = train_test_split(x_bc, y_bc, random_state=1)

model = GaussianNB()
model.fit(x_train, y_train)
y_model = model.predict(x_text)

print(accuracy_score(y_test, y_model))

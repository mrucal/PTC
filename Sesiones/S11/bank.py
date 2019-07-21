# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 09:59:35 2017

@author: Mario
"""

import pandas as pd
from sklearn import svm
bank_datos = pd.read_csv(open('bank.csv'),sep=';')

from sklearn.cross_validation import train_test_split
from sklearn.datasets import load_breast_cancer
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import GaussianNB

datos = open('bank.csv').readline()
caracteristicas = [i for i in datos.split("\"") if i != ';' and i != '' and i != '\n']
print(caracteristicas)


caracteristicas = {
    'job' : ["admin.","unknown","unemployed","management","housemaid","entrepreneur","student","blue-collar","self-employed","retired","technician","services"],
    'marital' : ["married","divorced","single"; note: "divorced"],
    'education' : ["unknown","secondary","primary","tertiary"],
    'default' : ["yes", "no"],
    'housing' : 
    'loan' :    
    }
'''y_b = bank_datos['y']
del bank_datos['y']
x_b = bank_datos

x_train, x_text, y_train, y_test = train_test_split(x_b, y_b, random_state=1)

model = GaussianNB()
model.fit(x_train, y_train)
y_model = model.predict(x_text)

print(accuracy_score(y_test, y_model))'''
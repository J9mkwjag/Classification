# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 20:15:54 2023

@author: coope
"""

pip install ucimlrepo

from ucimlrepo import fetch_ucirepo 
  
# fetch dataset 
statlog_german_credit_data = fetch_ucirepo(id = 144) 
  
# data (as pandas dataframes) 
X = statlog_german_credit_data.data.features 
y = statlog_german_credit_data.data.targets 
  
# metadata 
print(statlog_german_credit_data.metadata) 
  
# variable information 
print(statlog_german_credit_data.variables) 


## Sklearn


## PySpark





## Pre-Processing

# Check for Rare Event



## ML Pipeline




## General Linear Models (Elastic Net)



## Gradient Boosting Models (XGBoost, AdaBoost, CatBoost, etc)




## Support Vector Machine



## Random Forest Model




## Neural Network Model




## Logistic Regression Model




## General Additive Models




## Naive Bayes Model



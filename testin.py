#!/bin/bash env python3

#in a script we write the following to find our load function

#>>>import sklearn.datasets
#>>>dir(sklearn.datasets)
#>>>[func for func in dir(sklearn.datasets) if func.startswith("load")]

from sklearn.datasets import load_iris

iris_data = load_iris()

dir(iris_data)

###Now, i want to list the properties of the dataset, and what each "mean" 
#TODO:
#'DESCR': this is a dataset description
#data numpy array, in the shape rowa x columns
#feature_name: feature labels for the dataset
#target: numpy array, 1xrows, containing the thing we're trying to predict
#target_names name of teh class we're predicting in the categorical case

#TODO:
#1-first visualie your data from loading it *this way*
#  -this can actually include converting tp pandas, and running your script from before
#2-train & apply either KNN-classifier or KNN-regressor on your dataset
#3-print the output "score" or "performance" of the classifier/regressor
#(if you did 2&3 right, your performance will *not* be perfect) 

iris_data('target')
help(iris_data)

#Examples
#    --------
#    Let's say you are interested in the samples 10, 25, and 50, and want to
#    know their class name.
#    
#    >>> from sklearn.datasets import load_iris
#    >>> data = load_iris()
#    >>> data.target[[10, 25, 50]]
#    array([0, 0, 1])
#    >>> list(data.target_names)
#    ['setosa', 'versicolor', 'virginica']




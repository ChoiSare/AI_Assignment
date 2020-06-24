# import libraries
import os
import pandas as pd
import matplotlib.pyplot as plt

# Set working directory and load data
os.chdir('C:/Users/최지선/Desktop/인공지능과 기계학습/11주차/11주차 과제/')
iris = pd.read_csv('iris.csv')

print(iris.head())
# Create numeric classes for species (0,1,2)
iris.loc[iris['species']=='virginica', 'species']=0
iris.loc[iris['species']=='versicolor', 'species']=1
iris.loc[iris['species']=='setosa', 'species']=2
iris = iris[iris['species']!=2]

# Create input and Output columns
X = iris[['sepal_length', 'sepal_width']].values.T
Y = iris[['species']].values.T
Y = Y.astype('uint8')

# Make a scatter plot
plt.scatter(X[0, :], X[1, :], c=Y[0, :], s=40, cmap=plt.cm.Spectral);
plt.title("IRIS DATA | Blue - Versicolor, Red - Virginica")
plt.xlabel('petal_length')
plt.ylabel('petal_width')
plt.show()

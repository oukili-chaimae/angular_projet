# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 01:13:46 2022

@author: EL_HAMASI
"""
from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 
import sklearn
import pymongo

dataset = pd.read_csv('customer.csv')
X = dataset.iloc[:, [3, 4]].values

from sklearn.cluster import KMeans
wcss = []
for i in range(1, 11): 
    kmeans = KMeans(n_clusters = i, init = 'k-means++', random_state = 42)
    kmeans.fit(X) 
    wcss.append(kmeans.inertia_)
    
plt.plot(range(1, 11), wcss)
plt.xlabel('Number of clusters')
plt.ylabel('WCSS') 
plt.show()

kmeans = KMeans(n_clusters = 5, init = "k-means++", random_state = 42)
y_kmeans = kmeans.fit_predict(X)

centroides = kmeans.cluster_centers_
print("les centroides=====>",centroides)

plt.scatter(dataset['annual_Income'],dataset['spending_Score'])
plt.show()

plt.scatter(X[y_kmeans == 0, 0], X[y_kmeans == 0, 1], s = 60    , c = 'red', label = 'Cluster1') 
plt.scatter(X[y_kmeans == 1 , 0], X[y_kmeans == 1, 1], s = 60, c = 'blue', label = 'Cluster2') 
plt.scatter(X[y_kmeans == 2, 0], X[y_kmeans == 2 , 1], s = 60, c = 'green', label = 'Cluster3') 
plt.scatter(X[y_kmeans == 3, 0], X[y_kmeans == 3, 1], s = 60, c = 'violet', label = 'Cluster4')
plt.scatter(X[y_kmeans == 4, 0], X[y_kmeans == 4, 1], s = 60, c = 'yellow', label = 'Cluster5')

plt .scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s = 100, c = 'gray',marker='*', label = 'Centroids') 
plt.xlabel('annual_Income'); plt.ylabel('spending_Score'); plt.legend() 

plt.show()

dataset['cluster'] = y_kmeans
dataset.head()

data = dataset.to_dict(orient ="records")

client1 = pymongo.MongoClient("mongodb+srv://user:user@cluster0.sc8ot.mongodb.net/myDB?retryWrites=true&w=majority")
#mydb = client1.get_database("Assurance")

db = client1["myDB"]

#print("la base de données=======>",db)
myCollection = db["customer"]

myCollection.insert_many(data)

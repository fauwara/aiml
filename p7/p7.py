import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from sklearn.datasets import load_iris

from sklearn import preprocessing
from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture

# load datasets from sklearn
iris = load_iris()
# Take only the data part and label the columns from iris dataset
df = pd.DataFrame(iris['data'], columns=iris['feature_names'])
# add new column to the data called targets and map it to targets from iris dataset
df['target'] = iris['target']

#           get everything in Y axis and everything but last column in X
x = df.iloc[:,:-1]
y = df['target']


scaler = preprocessing.StandardScaler()

## PREPROCESSING
scaler.fit(x)
x_scaled_array = scaler.transform(x)
x_scaled = pd.DataFrame(x_scaled_array, columns = x.columns)

# print(x_scaled)

# CREATE THE GRAPH
plt.figure(figsize=(14,7))
colormap = np.array(['red', 'green', 'blue'])

## REAL
plt.subplot(1,3,1)
plt.scatter(x_scaled['petal length (cm)'], x_scaled['petal width (cm)'], c=colormap[y], s=40)
plt.title('Real')

## K MEANS
km_model = KMeans(n_clusters=3, random_state=0)
pred_y = km_model.fit_predict(x)
pred_y = np.choose(pred_y, [1,0,2]).astype(np.int64)
# print(pred_y)
plt.subplot(1,3,2)
plt.scatter(x_scaled['petal length (cm)'], x_scaled['petal width (cm)'], c=colormap[pred_y], s=40)
plt.title('K Means')

## GMM
gm_model = GaussianMixture(n_components=3, max_iter=200)
y_cluster_gmm = gm_model.fit_predict(x_scaled)
y_cluster_gmm = np.choose(y_cluster_gmm, [2,0,1]).astype(np.int64)
# print(y_cluster_gmm)
plt.subplot(1,3,3)
plt.scatter(x_scaled['petal length (cm)'], x_scaled['petal width (cm)'], c=colormap[y_cluster_gmm], s=40)
plt.title('GMM')


plt.show()
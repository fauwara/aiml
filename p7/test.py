import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from sklearn.datasets import load_iris

from sklearn import preprocessing
from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture



iris_data = load_iris()
iris_df = pd.DataFrame(iris_data['data'], columns=iris_data['feature_names'])
iris_df['target'] = iris_data['target']


x = iris_df.iloc[::-1]
y = iris_df['target']


scaler = preprocessing.StandardScaler()
scaler.fit(x)
x_scaler_array = scaler.transform(x)
x_scaler = pd.DataFrame(x_scaler_array, columns=x.columns)


plt.figure(figsize=(14,7))
colormap = np.array(['red', 'green', 'blue'])

plt.subplot(1,3,1)
plt.scatter(x_scaler['petal length (cm)'], x_scaler['petal width (cm)'], c=colormap[y], s=40)
plt.title('Real')


km_cluster = KMeans(n_clusters=3, random_state=0)
km_y_pred = km_cluster.fit_predict(x)
km_y_pred = np.choose(km_y_pred, [1,0,2]).astype(np.int64)
plt.subplot(1,3,2)
plt.scatter( x_scaler['petal length (cm)'], x_scaler['petal width (cm)'], c=colormap[km_y_pred], s=40 )
plt.title('KMeans')


gm_mixture = GaussianMixture(n_components=3, max_iter=200)
gm_y_pred = gm_mixture.fit_predict(x_scaler)
gm_y_pred = np.choose(gm_y_pred , [2,0,1]).astype(np.int64)
plt.subplot(1,3,3)
plt.scatter(x_scaler['petal length (cm)'], x_scaler['petal width (cm)'], c=colormap[gm_y_pred], s=40)
plt.title('GMM')

plt.show()
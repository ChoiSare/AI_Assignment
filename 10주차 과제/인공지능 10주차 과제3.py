# 필요한 라이브러리 임포트하기
from sklearn import datasets
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans

# 데이터 로드
iris = datasets.load_iris()

# dlqfur(X)와 출력(y) or target
X = iris.data[:, :2]
y = iris.target

# 데이터 살펴보기
plt.scatter(X[:, 0], X[:, 1], c=y, cmap='gist_rainbow')
plt.xlabel('Speal Length', fontsize=18)
plt.ylabel('Speal Width', fontsize=18)

# k-means 클러스터링
km = KMeans(n_clusters = 3, n_jobs = 4, random_state = 21)
km.fit(X)

# 중심점 위치
centers = km.cluster_centers_
print(centers)

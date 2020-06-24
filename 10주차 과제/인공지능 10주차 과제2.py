from sklearn.datasets import load_iris # scikit-learn의 샘플 데이터 로드
import pandas as pd # 데이터 프레임으로 변환을 위해 임포트
import numpy as np # 연산을 위해 임포트

# 시각화를 위한 패키지 임포트
import matplotlib.pyplot as plt
import seaborn as sns

iris = load_iris() # sample data load

print(iris) # 로드된 데이터가 속성-스타일 접근을 제공하는 딕셔너리와 번치 객체로 표현된 것을 확인
print(iris.DESCR) # Description 속성을 이용해서 데이터셋의 정보를 확인

# 각 key에 저장된 value 확인
print(iris.data)
print(iris.feature_names)

# label
print(iris.target)
print(iris.target_names)

# feature_names 와 target을 레코드로 갖는 데이터프레임 생성
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['target'] = iris.target

# 0.0, 1.0, 2.0으로 표현된 label을 문자열로 매핑
df['target'] = df['target'].map({0:"setosa", 1:"versicolor", 2:"virginica"})
print(df)

# 슬라이싱을 통해 feature와 label 분리
x_data = df.iloc[:, :-1]
y_data = df.iloc[:,[-1]]

sns.pairplot(df, x_vars=["sepal length (cm)"], y_vars=["sepal width (cm)"], hue="target", height=5)
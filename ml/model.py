# Load library

import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import SGDClassifier
import joblib

# Load ROSE processing data

doc = pd.read_csv('ml/rose_data.csv', encoding='cp949')

# New dataframe copy exclude unnecessary column

data = doc[['풍속', '기압', '습도', '기온', '수온', '최대파고.m.', '유의파고.m.', '평균파고.m.', '파주기.sec.', 'check']].copy()

# Variable set

x = np.array(data[['풍속', '기압', '습도', '기온', '수온', '최대파고.m.', '유의파고.m.', '평균파고.m.', '파주기.sec.']])
y = np.array(data[['check']])

# Scaling - MinMaxScaler

scaler = MinMaxScaler()
scaler.fit(x)
scaling_x = scaler.transform(x)

# Train, test data set test_szie: 0.20
# test_size : 테스트 데이터셋의 비율(float)이나 갯수(int) (default = 0.25)

xtrain, xtest, ytrain, ytest = train_test_split(scaling_x, y, test_size=0.20, random_state=88)

# Use SGDClassifier
# Solve warning msg -> .ravel()
# '풍속', '기압', '습도', '기온', '수온', '최대파고.m.', '유의파고.m.', '평균파고.m.', '파주기.sec.'

elastic = SGDClassifier(loss="log", max_iter=10000, penalty="elasticnet", tol=0.01, random_state=36)
elastic_model = elastic.fit(xtrain, ytrain.ravel())

# Load model

joblib.dump(elastic_model, 'model/model.pkl')
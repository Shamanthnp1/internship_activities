import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.preprocessing import PolynomialFeatures
df = pd.read_csv("dataset.csv")
df.info()
le = LabelEncoder()
df['encoded_col'] = le.fit_transform(df['category'])
df = pd.get_dummies(df, columns=['category'], drop_first=True)
scaler = StandardScaler()
scaled_features = scaler.fit_transform(df[['age', 'salary']])
poly = PolynomialFeatures(degree=2, include_bias=False)
poly_features = poly.fit_transform(df[['feature']])
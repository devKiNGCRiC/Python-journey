import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

np.random.seed(42)

X = np.random.rand(100,3)*100
y = (X[:,0]*200 + X[:,1]*50000 - X[:,2]*1000 + np.random.randn(100)*10000)

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

model = LinearRegression()
model.fit(X_scaled,y)

new_house = np.array([[1500,3,10]])
new_house_scaled = scaler.transform(new_house)
predicted_price = model.predict(new_house_scaled)
print(f'Predicted price: ${predicted_price[0]:,.2f}')
print(f'R-squared: {model.score(X_scaled,y):.3f}')
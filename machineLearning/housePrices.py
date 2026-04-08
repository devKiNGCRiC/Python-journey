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

# Matplotlib: Actual vs Predicted price plot
y_pred = model.predict(X_scaled)

plt.figure(figsize=(8,5))
plt.scatter(y, y_pred, alpha=0.7, color='teal')

line_min = min(y.min(), y_pred.min())
line_max = max(y.max(), y_pred.max())
plt.plot([line_min, line_max], [line_min, line_max], 'r--', linewidth=2)

plt.title('Actual vs Predicted House Prices')
plt.xlabel('Actual Prices')
plt.ylabel('Predicted Prices')
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()
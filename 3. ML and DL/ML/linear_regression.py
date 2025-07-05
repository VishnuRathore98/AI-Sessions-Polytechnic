import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

ages = np.array([5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]).reshape(-1, 1)   """A 2D array of ages (reshaped with .reshape(-1, 1) so that it's compatible with scikit-learn which expects 2D input features)."""

heights = np.array([105, 110, 115, 120, 125, 130, 138, 145, 150, 158, 162, 165, 168, 170])

model = LinearRegression()   # create linear regression model
model.fit(ages, heights)     # train model 

age_to_predict = np.array([[15.5]])         # A new input (15.5 years) for which height will be predicted.
predicted_height = model.predict(age_to_predict)[0]   # Predicts the height using the trained model. Since .predict() returns an array, [0] gets the scalar value.
print(f"Predicted height at age 15.5: {predicted_height:.2f} cm")  # Displays the predicted height with 2 decimal places.

plt.scatter(ages, heights, color='blue', label='Actual Data')  # Plots actual age-height data as blue dots.
plt.plot(ages, model.predict(ages), color='green', label='Linear Fit') # Plots the regression line (predicted heights from the model) in green.
plt.scatter(age_to_predict, predicted_height, color='red', label=f'Predicted @ 15.5 = {predicted_height:.1f} cm') # Plots the predicted point in red.

plt.xlabel("Age (years)")
plt.ylabel("Height (cm)")
plt.title("Predicting Height from Age")
plt.legend()
plt.grid(True)
plt.show()

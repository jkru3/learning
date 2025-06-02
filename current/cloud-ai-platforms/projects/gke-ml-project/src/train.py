# train.py
import os
import time
from sklearn.linear_model import LinearRegression
import numpy as np

print("Starting ML training job...")
print(f"Running on hostname: {os.uname().nodename}")
print(f"Current time: {time.ctime()}")

# Simulate some data
X = np.random.rand(100, 10)
y = np.random.rand(100)

# Train a simple model
model = LinearRegression()
model.fit(X, y)

print("Model training complete!")
print(f"Coefficients: {model.coef_}")
print(f"Job finished at: {time.ctime()}")

# Simulate work that might benefit from accelerators
time.sleep(10) # long enough to observe in logs/monitoring
print("Simulated intense computation done.")
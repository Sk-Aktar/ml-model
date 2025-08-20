import pandas as pd
import numpy as np

# Generate synthetic regression dataset
np.random.seed(42)
n_samples = 1000

feature1 = np.random.uniform(-10, 10, n_samples)
feature2 = np.random.normal(5, 2, n_samples)
feature3 = np.random.uniform(-5, 5, n_samples)

# Linear combination + noise
target = 4*feature1 - 3*feature2 + 2*feature3 + np.random.normal(0, 5, n_samples)

# Create DataFrame
df_reg = pd.DataFrame({
    "Feature1": feature1,
    "Feature2": feature2,
    "Feature3": feature3,
    "Target": target
})

# Save as CSV
df_reg.to_csv("regression_dataset.csv", index=False)

print("✅ Dataset saved as regression_dataset.csv")
print(df_reg.head())

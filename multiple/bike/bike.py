import pandas as pd
import numpy as np

# For reproducibility
np.random.seed(42)

# Number of samples
n_samples = 1000

# Independent variables
engine_size = np.random.uniform(1.0, 5.0, n_samples)        # in liters
horsepower = np.random.uniform(70, 400, n_samples)          # HP
car_age = np.random.randint(0, 15, n_samples)               # in years
mileage = np.random.uniform(5000, 200000, n_samples)        # in km

# Dependent variable: Price (USD) with noise
price = (engine_size * 5000) + (horsepower * 150) - (car_age * 800) \
        - (mileage * 0.05) + np.random.normal(0, 2000, n_samples)

# Create DataFrame
df_cars = pd.DataFrame({
    'Engine_Size_L': engine_size,
    'Horsepower': horsepower,
    'Car_Age_Years': car_age,
    'Mileage_km': mileage,
    'Price_USD': price
})

# Save CSV
df_cars.to_csv("car_prices_mlr.csv", index=False)

print("CSV file created: car_prices_mlr.csv")

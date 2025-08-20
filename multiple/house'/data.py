import pandas as pd
import numpy as np

# Reproducibility
np.random.seed(42)

# Number of samples
n_samples = 1000

# Independent variables
square_feet = np.random.uniform(800, 3500, n_samples)          # size in sq ft
bedrooms = np.random.randint(1, 6, n_samples)                  # number of bedrooms
distance_city_center = np.random.uniform(1, 30, n_samples)     # distance in km

# Dependent variable: House Price with noise
price = (square_feet * 150) + (bedrooms * 10000) - (distance_city_center * 2000) \
        + np.random.normal(0, 20000, n_samples)

# Create DataFrame
df_houses = pd.DataFrame({
    'Square_Feet': square_feet,
    'Bedrooms': bedrooms,
    'Distance_to_CityCenter_km': distance_city_center,
    'Price': price
})

# Save to CSV
df_houses.to_csv("house_price.csv", index=False)

print("CSV file created: house_prices_mlr.csv")

import pandas as pd
import numpy as np

# Number of samples
n_samples = 1200

# Independent variable: Temperature in Celsius
np.random.seed(42)
temperature = np.random.uniform(15, 40, n_samples)

# Dependent variable: Ice Cream Sales (in $) with some noise
ice_cream_sales = (temperature * 20) + np.random.normal(0, 30, n_samples)

# Create DataFrame
df_icecream = pd.DataFrame({
    'Temperature_C': temperature,
    'Ice_Cream_Sales': ice_cream_sales
})

# Save to CSV
df_icecream.to_csv("temperature_vs_icecream_sales.csv", index=False)

print("CSV file created: temperature_vs_icecream_sales.csv")

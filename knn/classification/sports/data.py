import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Number of samples
n_samples = 100

# Generate features
ages = np.random.randint(15, 61, size=n_samples)  # Age between 15 and 60
training_hours = np.random.randint(0, 11, size=n_samples)  # Weekly training hours 0-10

# Generate target based on simple rule + randomness
likes_sport = []
for age, hours in zip(ages, training_hours):
    # People who train more likely like sport, younger more likely
    if hours > 3 and age < 40:
        likes_sport.append('Yes' if np.random.rand() > 0.2 else 'No')
    else:
        likes_sport.append('No' if np.random.rand() > 0.3 else 'Yes')

# Create DataFrame
df = pd.DataFrame({
    'Age': ages,
    'WeeklyTrainingHours': training_hours,
    'LikesSport': likes_sport
})

# Save to CSV
df.to_csv('sport_knn.csv', index=False)

print(df.head())
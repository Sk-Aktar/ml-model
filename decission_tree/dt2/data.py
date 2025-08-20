import pandas as pd
from sklearn.datasets import make_classification
# Generate another large synthetic dataset for Decision Tree Classification
# This time let's make it binary classification with more features

X, y = make_classification(
    n_samples=7000,      # bigger dataset
    n_features=8,        # number of features
    n_informative=5,     # informative features
    n_redundant=2,       # redundant features
    n_classes=2,         # binary classification
    random_state=24
)

# Convert to DataFrame
df_tree2 = pd.DataFrame(X, columns=[f"Feature{i}" for i in range(1, 9)])
df_tree2["Label"] = y

# Save CSV
path_tree2 = "decision_tree.csv"
df_tree2.to_csv(path_tree2, index=False)


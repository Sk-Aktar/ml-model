import pandas as pd
import numpy as np

# Set seed
np.random.seed(404)

# Spam and ham templates
spam_templates = [
    "Win a free iPhone now! Click here to claim your prize",
    "Congratulations, you have been selected for a lottery!",
    "Limited offer! Buy one get one free on all items",
    "Earn money from home easily without investment",
    "Get cheap loans with zero interest, apply today",
    "Exclusive deal only for you, click to grab it",
    "You are a lucky winner, claim your gift card now",
    "Urgent: Verify your account to avoid suspension",
    "Lowest prices guaranteed, buy today",
    "Act now to secure your discount coupon"
]

ham_templates = [
    "Meeting scheduled at 3 PM tomorrow, please confirm",
    "Your Amazon order has been shipped successfully",
    "Don't forget the project deadline is next Monday",
    "Your account has been credited with the refund",
    "Dinner at my place tonight? Bring dessert!",
    "Let's catch up this weekend at the cafe",
    "Can you send me the updated report by evening?",
    "Happy birthday! Wishing you a wonderful day",
    "See you at the gym tomorrow morning",
    "Family trip planned for next holiday, excited!"
]

# Generate dataset of 5000 samples
n_samples = 5000
emails = np.random.choice(spam_templates + ham_templates, size=n_samples, replace=True)

# Labels
spam_labels = [1 if e in spam_templates else 0 for e in emails]

# Create DataFrame
df = pd.DataFrame({
    "Email": emails,
    "Spam": spam_labels
})

# Save to CSV
df.to_csv("email_spam.csv", index=False)

print("CSV file 'email_spam_big_dataset.csv' created successfully!")

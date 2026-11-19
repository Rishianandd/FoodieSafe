"""FoodieSafe synthetic dataset analysis. Run: python analyze_foodiesafe.py"""
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "outputs"
OUT.mkdir(exist_ok=True)
df = pd.read_csv(ROOT / "FoodieSafe_app_data.csv")
print("Rows, columns:", df.shape)
print("Missing values:\n", df.isna().sum())
print("Allergen distribution:\n", df['allergen'].value_counts())
print("Privacy consent:\n", df['privacy_consent'].value_counts())

for col, title, filename in [
    ('allergen', 'Reported allergens', 'allergens.png'),
    ('dietary_preference', 'Dietary preferences', 'dietary_preferences.png'),
    ('privacy_concern', 'Privacy concerns', 'privacy_concerns.png'),
    ('privacy_consent', 'Privacy consent', 'privacy_consent.png')]:
    counts = df[col].value_counts()
    ax = counts.plot(kind='bar', figsize=(9,5), title=title)
    ax.set_ylabel('Synthetic customers')
    plt.xticks(rotation=35, ha='right')
    plt.tight_layout()
    plt.savefig(OUT / filename, dpi=160)
    plt.close()

summary = df.groupby('privacy_concern').agg(customers=('customer_id','count'), average_satisfaction=('satisfaction_score','mean')).reset_index()
summary.to_csv(OUT / 'summary.csv', index=False)
print('Saved charts and summary to:', OUT)

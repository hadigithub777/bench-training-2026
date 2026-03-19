"""
Day 5: Titanic Dataset Analysis
Answers 10 questions about the Titanic dataset using pandas.
Dataset: 891 passengers from the Titanic (Kaggle / Data Science Dojo).
"""

import pandas as pd

SEPARATOR = "=" * 70

df = pd.read_csv("titanic.csv")

print(SEPARATOR)
print("TITANIC DATASET ANALYSIS")
print(f"Loaded {len(df)} rows, {len(df.columns)} columns")
print(SEPARATOR)


# --------------------------------------------------------------------------- #
# Q1: How many passengers survived vs. didn't? Counts and percentages.
# --------------------------------------------------------------------------- #
print("\nQ1: Survival counts and percentages")
print("-" * 40)

survived_counts = df["Survived"].value_counts()
survived_pct = df["Survived"].value_counts(normalize=True) * 100

print(f"  Did not survive: {survived_counts[0]:>4}  ({survived_pct[0]:.1f}%)")
print(f"  Survived:        {survived_counts[1]:>4}  ({survived_pct[1]:.1f}%)")


# --------------------------------------------------------------------------- #
# Q2: Survival rate by passenger class (1st, 2nd, 3rd).
# --------------------------------------------------------------------------- #
print(f"\nQ2: Survival rate by passenger class")
print("-" * 40)

class_survival = df.groupby("Pclass")["Survived"].mean() * 100
for pclass, rate in class_survival.items():
    print(f"  Class {pclass}: {rate:.1f}%")


# --------------------------------------------------------------------------- #
# Q3: Average age of survivors vs. non-survivors.
# --------------------------------------------------------------------------- #
print(f"\nQ3: Average age — survivors vs. non-survivors")
print("-" * 40)

avg_age = df.groupby("Survived")["Age"].mean()
print(f"  Non-survivors: {avg_age[0]:.1f} years")
print(f"  Survivors:     {avg_age[1]:.1f} years")


# --------------------------------------------------------------------------- #
# Q4: Which embarkation port had the highest survival rate?
# --------------------------------------------------------------------------- #
print(f"\nQ4: Survival rate by embarkation port")
print("-" * 40)

port_names = {"C": "Cherbourg", "Q": "Queenstown", "S": "Southampton"}
port_survival = df.groupby("Embarked")["Survived"].mean() * 100
best_port = port_survival.idxmax()

for port, rate in port_survival.items():
    marker = " <-- highest" if port == best_port else ""
    print(f"  {port} ({port_names.get(port, port):>12}): {rate:.1f}%{marker}")


# --------------------------------------------------------------------------- #
# Q5: Missing ages — count them, then fill with per-class median.
# --------------------------------------------------------------------------- #
print(f"\nQ5: Missing age values and imputation")
print("-" * 40)

missing_age = df["Age"].isna().sum()
print(f"  Missing Age values: {missing_age} ({missing_age / len(df) * 100:.1f}% of rows)")

# Fill missing ages with the median age for that passenger's class
class_medians = df.groupby("Pclass")["Age"].median()
print(f"  Class median ages used for fill: {dict(class_medians.round(1))}")

df["Age"] = df.groupby("Pclass")["Age"].transform(
    lambda x: x.fillna(x.median())
)
print(f"  Missing Age values after fill: {df['Age'].isna().sum()}")


# --------------------------------------------------------------------------- #
# Q6: Oldest surviving passenger — name, age, class.
# --------------------------------------------------------------------------- #
print(f"\nQ6: Oldest surviving passenger")
print("-" * 40)

survivors = df[df["Survived"] == 1]
oldest = survivors.loc[survivors["Age"].idxmax()]
print(f"  Name:  {oldest['Name']}")
print(f"  Age:   {oldest['Age']:.0f}")
print(f"  Class: {int(oldest['Pclass'])}")


# --------------------------------------------------------------------------- #
# Q7: Survival rate — women vs. men.
# --------------------------------------------------------------------------- #
print(f"\nQ7: Survival rate by sex")
print("-" * 40)

sex_survival = df.groupby("Sex")["Survived"].mean() * 100
print(f"  Women: {sex_survival['female']:.1f}%")
print(f"  Men:   {sex_survival['male']:.1f}%")


# --------------------------------------------------------------------------- #
# Q8: New column 'AgeGroup' — survival rate per group.
# --------------------------------------------------------------------------- #
print(f"\nQ8: Survival rate by age group")
print("-" * 40)

bins = [0, 18, 60, float("inf")]
labels = ["Child (<18)", "Adult (18-60)", "Senior (60+)"]
df["AgeGroup"] = pd.cut(df["Age"], bins=bins, labels=labels, right=False)

age_group_survival = df.groupby("AgeGroup")["Survived"].agg(["mean", "count"])
for group, row in age_group_survival.iterrows():
    print(f"  {group:>15}: {row['mean'] * 100:.1f}%  (n={int(row['count'])})")


# --------------------------------------------------------------------------- #
# Q9: Among 3rd-class passengers, survival rate for men vs. women.
# --------------------------------------------------------------------------- #
print(f"\nQ9: 3rd class survival rate — men vs. women")
print("-" * 40)

third_class = df[df["Pclass"] == 3]
third_sex_survival = third_class.groupby("Sex")["Survived"].mean() * 100
print(f"  Women: {third_sex_survival['female']:.1f}%")
print(f"  Men:   {third_sex_survival['male']:.1f}%")


# --------------------------------------------------------------------------- #
# Q10: Drop rows with missing Cabin data — how many remain?
# --------------------------------------------------------------------------- #
print(f"\nQ10: Dropping rows with missing Cabin data")
print("-" * 40)

original_rows = len(df)
df_cabin = df.dropna(subset=["Cabin"])
remaining = len(df_cabin)
kept_pct = remaining / original_rows * 100

print(f"  Original rows:  {original_rows}")
print(f"  Rows remaining: {remaining}")
print(f"  Data kept:      {kept_pct:.1f}%")

print(f"\n{SEPARATOR}")
print("Analysis complete.")
print(SEPARATOR)

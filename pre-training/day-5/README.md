# Day 5 — Pandas + Data: Titanic Dataset Analysis

## What I Built

A single Python script (`analysis.py`) that loads the Titanic dataset (891 passengers) and answers 10 analytical questions using pandas — survival counts, class breakdowns, age imputation, gender splits, and more.

## How to Run

```bash
cd pre-training/day-5
python analysis.py
```

Requires: `pandas`

## Most Surprising Finding

**3rd-class women had only a 50% survival rate** — compared to 74.2% overall for women. "Women and children first" clearly applied much more strongly in 1st class (where nearly all women survived) than in 3rd class (where half the women died). Class was nearly as powerful a predictor as gender.

Also striking: **77% of the Cabin data is missing** (Q10). Dropping rows with missing Cabin values leaves just 204 of 891 rows. That column is almost unusable without imputation — yet the passengers *with* cabin data skew heavily toward 1st class, which would silently bias any analysis that naively drops those rows.

## What I'd Investigate Next

- **Feature engineering for a survival model**: combine Sex, Pclass, Age, and family size (SibSp + Parch) into a logistic regression or random forest to predict survival. How accurate can we get?
- **Fare vs. survival within the same class**: did paying more for a 3rd-class ticket (better cabin location?) improve your odds?
- **Family size effect**: solo travelers vs. small families vs. large families — who fared best?
- **Name titles** (Mr., Mrs., Master, Miss, Dr.): extracting titles from the Name field could serve as a proxy for social status and age, especially useful for filling missing Age values more accurately than class median.

## Resources

- [Corey Schafer — Pandas Tutorial (videos 1-3)](https://youtube.com/playlist?list=PL-osiE80TeTsWmV9i9c58mdDCSskIFdDS)
- [Titanic dataset (Data Science Dojo)](https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv)

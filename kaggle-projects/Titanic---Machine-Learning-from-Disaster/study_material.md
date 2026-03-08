# Titanic Project – Study Notes

These notes capture all the experiments and explanations that were removed from the clean notebook, so they can be revised later without clutter.

## Column Data

PassengerId | Survived | Pclass | Name | Sex | Age | SibSp | Parch | Ticket | Fare | Cabin | Embarked

---

### Column Analysis

1. **PassengerId** – no use ❌  

2. **Survived** – target class ✅  

3. **Pclass** – 1 / 2 / 3 economic status of passenger ✅  

4. **Name** – contains titles like *Mr, Mrs, Miss*  
   Extract title and convert to numeric → **0,1,2,3,4** ✅  

5. **Sex** – useful feature  
   Convert → **male = 0 , female = 1** ✅  

6. **Age** – useful feature  
   Convert into categories → **0,1,2,3,4** ✅  

7. **SibSp** – number of siblings / spouses onboard → useful ✅  

8. **Parch** – number of parents / children onboard → useful ✅  

9. **Ticket** – not useful ❌  

10. **Fare** – useful feature ✅  

11. **Cabin** – not useful (many missing values) ❌  

12. **Embarked** – port where passenger boarded the ship → useful ✅  

---

### Feature Engineering

Create new column:

**FamilySize**


## 1. Dataset understanding

- Columns and meaning:
  - PassengerId: unique id per passenger (not useful as a feature).
  - Survived: target variable (0 = died, 1 = survived).
  - Pclass: ticket class (1, 2, 3) – proxy for socio-economic status.
  - Name: contains titles (Mr, Mrs, Miss, Master, etc.).
  - Sex: male/female.
  - Age: age in years, has many missing values.
  - SibSp: number of siblings/spouses aboard.
  - Parch: number of parents/children aboard.
  - Ticket: ticket number (high-cardinality, messy).
  - Fare: price paid.
  - Cabin: cabin number, lots of missing values.
  - Embarked: port (C, Q, S).

- Why some columns are dropped in the clean notebook:
  - PassengerId: pure identifier → no predictive info.
  - Ticket and Cabin: high-cardinality strings with many NaNs → more work for low gain (for a first model).
  - Name: could be used to engineer Title, but omitted in the clean version to keep the pipeline simple.

## 2. EDA commands

```python
train_df.head(100)
train_df.describe()
train_df.info()
train_df.isna().sum()
```

Observations:
- Age has many missing values.
- Cabin is mostly missing.
- Embarked has a few missing rows.
- Fare shows some large outliers.

## 3. Feature engineering ideas (not in clean notebook)

1. Title from Name using string operations or regex, grouping rare titles.
2. FamilySize = SibSp + Parch + 1.
3. IsAlone = 1 if FamilySize == 1 else 0.
4. Binning Age and Fare into bands or applying log-transform to Fare.

## 4. Missing value strategies

- Age: impute with median for robustness to outliers.
- Embarked: impute with most frequent value (mode).
- Fare: impute with median.
- Cabin: dropped because of too many missing values.

Implemented conceptually using:

```python
from sklearn.impute import SimpleImputer
numeric_imputer = SimpleImputer(strategy="median")
categorical_imputer = SimpleImputer(strategy="most_frequent")
```

## 5. Categorical encoding rationale

- Models like RandomForest need numeric input.
- Use one-hot encoding for Sex and Embarked.
- handle_unknown="ignore" prevents errors when unseen categories appear in test data.

## 6. Why use Pipeline and ColumnTransformer

- Bundles preprocessing and model into one object.
- Ensures identical transformations on train, validation, and test.
- Reduces data leakage and boilerplate code.

Structure:

1. ColumnTransformer applies numeric imputation and categorical imputation + one-hot.
2. Pipeline chains ColumnTransformer with RandomForestClassifier.

## 7. Model choice: RandomForestClassifier

Reasons:
- Handles non-linear relationships and feature interactions.
- Works well with mixed feature types after encoding.
- Provides feature importance and is relatively robust to hyperparameters.

Key parameters used:
- n_estimators = 200
- random_state = 42
- max_depth = None
- n_jobs = -1

## 8. Train/validation split and metrics

- Use train_test_split with test_size=0.2 and stratify=y.
- Metrics: accuracy_score and classification_report.

Example code:

```python
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

X_train, X_valid, y_train, y_valid = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_valid)
print("Accuracy:", accuracy_score(y_valid, y_pred))
print(classification_report(y_valid, y_pred))
```

## 9. Kaggle submission steps

1. Train final model on full training data (X, y).
2. Predict on processed test_df.
3. Create DataFrame with PassengerId and Survived.
4. Save as submission.csv with index=False.

## 10. Future improvement ideas

- Add engineered features like Title, FamilySize, IsAlone.
- Try gradient boosting models (XGBoost, LightGBM, etc.).
- Perform hyperparameter tuning (GridSearchCV or RandomizedSearchCV).
- Use cross-validation instead of a single train/validation split.

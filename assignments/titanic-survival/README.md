## Surviving the Titanic

In this assignment, you’ll use **pandas** to analyze data from the Titanic. We downloaded the data [from here](https://www.kaggle.com/datasets/yasserh/titanic-dataset).

---

### Step 1: Load the data

1. Load the Titanic dataset CSV file (`titanic_data.csv`) into a pandas dataframe.
2. Print out the number of rows (passengers) in the dataframe.

**Expected output**:

```
We have data on 891 passengers on the titanic.
```

---

### Step 2: Calculate Overall Survival Rate

Write a function called `get_percent_survived(df)` that returns the **percentage of passengers who survived**.

* Use the `"Survived"` column: 1 means survived, 0 means did not survive.
* Count how many rows have `Survived == 1`.
* Divide that number by the total number of rows.
* Multiply by 100 to get a percentage, and round it to two decimal places.

**Expected output**:

```
38.38% of passengers survived the titanic.
```

---

### Step 3: Calculate Female Survival Rate

1. Create a new dataframe that includes **only female passengers**.

   ```python
   females_df = df[df["Sex"] == "female"]
   ```
2. Use your `get_percent_survived` function to calculate and print the **percent of women who survived**.

✅ **Expected output**:

```
74.20% of women survived the titanic.
```

## Introverts vs Extroverts

In this assignment, you’ll use **pandas** to analyze personality data (downloaded [from here](https://www.kaggle.com/datasets/rakeshkapilavai/extrovert-vs-introvert-behavior-data?resource=download)).

---

### Step 1: Load the Data

1. Load the dataset CSV file (`personality_dataset.csv`) into a pandas dataframe.

---

### Step 2: Write a Function to Compute Average Alone Time

Write a function called `avg_time_spent_alone(df)` that returns the **average amount of time spent alone** (in hours) for the people in the given dataframe.

* Remove any rows where the `"Time_spent_Alone"` column is empty (hint: use `.notna()` to determine which cells are not empty).
* Add up the values in the `"Time_spent_Alone"` column and divide by the number of rows.
* Return the result.

You’ll use this function for both introverts and extroverts.

---

### Step 3: Compare Introverts and Extroverts

1. Create a new dataframe that contains **only extroverts**, and use your function to compute their average time spent alone.
2. Then, create a dataframe of **only introverts**, and compute their average as well.
3. Print both results.

**Expected output**:

```
Average alone time for extroverts: 2.07
Average alone time for introverts: 7.08
```

---

### Optional Extensions

Once you’ve completed the main part of the assignment, consider exploring some of the following optional challenges to deepen your understanding of data analysis and uncover interesting patterns in the dataset:

* **Top Friends Circle Sizes**: Sort the dataset by `"Friends_circle_size"` in descending order and print the top 3 individuals with the largest social circles.

**Expected output**:
```
Top 3 most friends:
      Time_spent_Alone Stage_fear  Social_event_attendance  Going_outside Drained_after_socializing  Friends_circle_size  Post_frequency Personality
2158               3.0         No                      7.0            5.0                        No                 15.0             6.0   Extrovert
2048               0.0        NaN                      9.0            5.0                        No                 15.0             7.0   Extrovert
174                1.0         No                      5.0            5.0                        No                 15.0             5.0   Extrovert
```

* **Missing Data on Going Outside**: Count how many people did **not** report how much time they spend going outside. Use `.isna()` to identify missing values.

**Expected output**:
```
Number of people who did not report on going outside: 66
```

* **Drop Rows with Missing Key Data**: Create a new dataframe by removing all rows with missing values in either the `"Time_spent_Alone"` or `"Going_outside"` columns. Print how many rows remain after cleaning.

**Expected output**:
```
Number of entries after dropping missing data: 2774
```

* **Social and Stage-Shy Individuals**: Find how many people attend more than 3 social events per week **and** report having stage fear. Use boolean indexing to filter the dataframe.

**Expected output**:
```
Number of people who attend >3 social events and have stage fear: 0
```

* **Bootstrapping for Group Comparison**: Implement bootstrapping, described [here](https://probabilityforcs.firebaseapp.com/book/bootstrapping), which gives you p-values when you compare group differences. You can then use your bootstrapping function to determine the significance of the differences between extroverts and introverts.

* **Drained After Socializing**: Compare the percentage of introverts and extroverts who report being `"Drained_after_socializing"` as `"Yes"`.

* **Stage Fear by Personality**: Analyze how common stage fright is among introverts and extroverts by comparing the number of `"Yes"` and `"No"` responses in the `"Stage_fear"` column for each group.

* **Social Event Attendance**: Calculate the average number of social events attended per week by introverts and extroverts using the `"Social_event_attendance"` column.

* **Going Outside Habits**: Compare the average number of hours introverts and extroverts spend going outside, based on the `"Going_outside"` column.

* **Friends and Posting Activity**: Compute the average `"Friends_circle_size"` and `"Post_frequency"` for both introverts and extroverts to see if there are trends in social connectivity and online activity.

* **Open-Ended Exploration**: Conduct your own exploration by forming a research question. For example, you might investigate whether people who report stage fright also tend to spend more time alone, or whether there is a relationship between the size of a person’s friend circle and how often they post on social media. Analyze the data, interpret your results, and summarize your findings in a few sentences.


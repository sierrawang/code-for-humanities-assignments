# **Assignment: What Factors Best Predict Student Exam Scores?**

In this assignment, you will focus on understanding which **student characteristics** are most associated with higher or lower exam scores. You will write code to **visualize trends** and **measure statistical significance** using your Python toolkit.

We downloaded this dataset [from here](https://www.kaggle.com/datasets/firedmosquito831/student-academic-performance-simulation-4000).

---

## **Objective**

You will answer the following research question:

> **“Which factors most correlate with student exam scores?”**

To do this, you will write code that analyzes the relationships between **exam score** and several **categorical variables** in the dataset:

* Gender (Female/Male)
* Tutoring (Yes/No)
* Region (Urban/Rural)
* Parent Education (Primary/Secondary/Tertiary/None)

---

## **Setup**

* Start by importing `pandas`, `matplotlib`, and `numpy` into your script.
* Write your main function.
* Load `data.csv` into a Pandas DataFrame.

---

## **Part 1: Visualizing Exam Score by Category**

Add the following function to your script:

```python
def plot_exam_scores_by_category(df, category_column_name):
    # Your code here
```

This function should:

* Take in your DataFrame and a column name for a categorical variable (like `"Gender"` or `"Region"`).
* For each category (e.g., `"Urban"` and `"Rural"` for region):

  * Collect the list of exam scores.
  * Calculate the **mean exam score**.
  * Calculate the **standard error of the mean**.
    
    **Hint:** You can calculate the standard error using this formula:
    `standard_error = np.std(data_list) / np.sqrt(len(data_list))`
  * Note: In this step, we construct three lists: `labels`, `avg_exam_scores`, and `errors`, which we will use to construct the plot in the next step.
* Use **matplotlib** to create a **bar chart**:

  * X-axis: category labels
  * Y-axis: average exam score
  * Add **error bars** to show the standard error
* Label the axes and title the chart appropriately.
* Test your function on each categorical data column.
* Extension: Add a new column that converts the continuous column `HoursStudied/Week` to be categorical. One idea is to create a column called `StudiedAmount` that is "High" for all students where `HoursStudied/Week` is above the average, and "Low" otherwise. This is just one idea - have fun with it! Once you have converted this column to be categorical, you can then use your `plot_exam_scores_by_category` function to visualize the correlation between studying and exam scores.
* Extension: Add a new column that converts the continuous column `Attendance(%)` to be categorical. Similar to the prior extension, determine the best way to perform this classification based on the data provided, and then use your graphing function to visualize the correlation between attendance and exam scores.

---

## **Part 2: Testing Statistical Significance Between Two Groups**

Write a function with the following signature:

```python
def compare_means(list1, list2):
    # Your code here
```

This function should:

* Take in two lists of exam scores (e.g., students who had tutoring vs. students who did not).
* Use numpy to perform a **two-sample t-test** assuming equal variances.
* Print:

  * The difference in the means
  * The p-value
  * A short statement about whether the result is statistically significant (e.g., p < 0.05)

---

## **Part 3: Use Your Functions to Investigate**

Use the two functions you implemented to explore the impact of each categorical variable:

* Call `plot_exam_scores_by_category()` for each of:

  * `"Gender"`
  * `"Tutoring"`
  * `"Region"`
  * `"Parent Education"`

* For any variable with just **two categories**, split the data into two lists of exam scores and call `compare_means()`.

* Use your results to answer:

  * Which characteristic shows the largest difference in exam scores?
  * Which differences are statistically significant?
  * What might be the most meaningful predictor of performance?

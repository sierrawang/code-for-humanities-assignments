# **Exploring the Heart Disease Dataset**

## **Overview**

In this exercise, you'll work with a real-world dataset on heart disease data, downloaded [from here](https://archive.ics.uci.edu/dataset/45/heart+disease). For this assignment, your dataset file is named: **`heart.csv`**

Here are some key attributes you’ll be working with:

| Column Name | Meaning                                                                  |
| ----------- | ------------------------------------------------------------------------ |
| `age`       | Age in years                                                             |
| `sex`       | 1 = male, 0 = female                                                     |
| `cp`        | Chest pain type (1–4)                                                    |
| `trestbps`  | Resting blood pressure (mm Hg)                                           |
| `chol`      | Serum cholesterol (mg/dl)                                                |
| `fbs`       | Fasting blood sugar > 120 mg/dl (1 = true, 0 = false)                    |
| `restecg`   | ECG results (0 = normal, 1 = abnormal, 2 = left ventricular hypertrophy) |
| `thalach`   | Maximum heart rate achieved                                              |
| `exang`     | Exercise-induced angina (1 = yes, 0 = no)                                |
| `oldpeak`   | ST depression induced by exercise                                        |
| `slope`     | Slope of ST segment (1 = upsloping, 2 = flat, 3 = downsloping)           |
| `ca`        | Number of major vessels (0–3)                                            |
| `thal`      | Thalassemia result (3 = normal, 6 = fixed defect, 7 = reversible defect) |
| `num`       | Heart disease diagnosis (0 = no disease, 1+ = has disease)               |

---

## **Your Task**

Load the dataset using pandas and complete the following:

1. **Add a new column `has_disease`**

   * This should be `True` if `num > 0`, and `False` otherwise.

2. **Print the following comparisons**:

   * Average age of people **with** and **without** heart disease
   * Average maximum heart rate (`thalach`) for **males vs. females**
   * Average cholesterol (`chol`) for people with different **chest pain types (`cp`)**
   * Average resting blood pressure (`trestbps`) for patients **with vs. without** exercise-induced angina (`exang`)
   * Count how many patients have **each type of slope** value (1, 2, 3)
   * Count how many patients have **each thalassemia result** (3, 6, 7)

3. **Use these tools:**

   * `.apply()` or `.iterrows()` for adding new columns
   * `boolean filtering` and `np.mean()` for calculations
   * `print()` for output

4. **Extension:**

   * Create plots to visualize your data analysis. Get creative!


<!-- Data is from https://archive.ics.uci.edu/dataset/45/heart+disease

Attribute documentation:
3 age: age in years
4 sex: sex (1 = male; 0 = female)
9 cp: chest pain type
-- Value 1: typical angina
-- Value 2: atypical angina
-- Value 3: non-anginal pain
-- Value 4: asymptomatic
10 trestbps: resting blood pressure (in mm Hg on admission to the hospital)
12 chol: serum cholestoral in mg/dl
16 fbs: (fasting blood sugar > 120 mg/dl)  (1 = true; 0 = false)
19 restecg: resting electrocardiographic results
-- Value 0: normal
-- Value 1: having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV)
-- Value 2: showing probable or definite left ventricular hypertrophy by Estes' criteria
32 thalach: maximum heart rate achieved
38 exang: exercise induced angina (1 = yes; 0 = no)
40 oldpeak = ST depression induced by exercise relative to rest
41 slope: the slope of the peak exercise ST segment
-- Value 1: upsloping
-- Value 2: flat
-- Value 3: downsloping
44 ca: number of major vessels (0-3) colored by flourosopy
51 thal: 3 = normal; 6 = fixed defect; 7 = reversable defect
58 num: diagnosis of heart disease (angiographic disease status)
-- Value 0: < 50% diameter narrowing
-- Value 1: > 50% diameter narrowing
(in any major vessel: attributes 59 through 68 are vessels)
 -->

# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind

# Function to plot average exam scores with error bars by category
def plot_exam_scores_by_category(df, category_column_name):
    # Create lists to store data for plotting
    labels = []
    avg_exam_scores = []
    errors = []

    # Get the unique categories in the column
    categories = df[category_column_name].unique()

    for category in categories:
        # Filter the rows for the current category
        scores = df[df[category_column_name] == category]["Exam_Score"]
        scores_list = scores.tolist()

        # Calculate mean and standard error
        mean = np.mean(scores_list)
        error = np.std(scores_list) / np.sqrt(len(scores_list))

        # Append to the lists
        labels.append(category)
        avg_exam_scores.append(mean)
        errors.append(error)

    # Create the bar chart
    plt.bar(labels, avg_exam_scores, yerr=errors, color='hotpink')
    plt.xlabel(category_column_name)
    plt.ylabel("Average Exam Score")
    plt.title(f"Exam Score by {category_column_name}")
    plt.show()


# Function to compare the means of two lists and perform a t-test
def compare_means(list1, list2):
    # Calculate mean difference
    mean1 = np.mean(list1)
    mean2 = np.mean(list2)
    diff = mean1 - mean2

    # Perform t-test
    t_stat, p_value = ttest_ind(list1, list2, equal_var=True)

    # Print the results
    print("Mean of group 1:", round(mean1, 2))
    print("Mean of group 2:", round(mean2, 2))
    print("Difference in means:", round(diff, 2))
    print(f"p-value: {p_value:.3f}")

    # Interpretation
    if p_value < 0.05:
        print("Result is statistically significant (p < 0.05).")
    else:
        print("Result is NOT statistically significant (p >= 0.05).")

def main():
    # Load the dataset
    df = pd.read_csv("data.csv")

    # Investigate categorical variables
    categorical_vars = ["Gender", "Tutoring", "Region", "Parent Education"]

    for var in categorical_vars:
        plot_exam_scores_by_category(df, var)

    # Gender: Female vs Male
    female_scores = df[df["Gender"] == "Female"]["Exam_Score"].tolist()
    male_scores = df[df["Gender"] == "Male"]["Exam_Score"].tolist()
    print("\nComparing Gender:")
    compare_means(female_scores, male_scores)

    # Tutoring: Yes vs No
    tutored_scores = df[df["Tutoring"] == "Yes"]["Exam_Score"].tolist()
    not_tutored_scores = df[df["Tutoring"] == "No"]["Exam_Score"].tolist()
    print("\nComparing Tutoring:")
    compare_means(tutored_scores, not_tutored_scores)

    # Region: Urban vs Rural
    urban_scores = df[df["Region"] == "Urban"]["Exam_Score"].tolist()
    rural_scores = df[df["Region"] == "Rural"]["Exam_Score"].tolist()
    print("\nComparing Region:")
    compare_means(urban_scores, rural_scores)

    # Extension: Add a categorical column for study amount
    average_study_time = df["HoursStudied/Week"].mean()
    df["StudiedAmount"] = df["HoursStudied/Week"].apply(lambda x: "High" if x > average_study_time else "Low")
    plot_exam_scores_by_category(df, "StudiedAmount")

    # Extension: Add a categorical column for attendance
    average_attendance = df["Attendance(%)"].mean()
    df["AttendanceLevel"] = df["Attendance(%)"].apply(lambda x: "High" if x > average_attendance else "Low")
    plot_exam_scores_by_category(df, "AttendanceLevel")

def fill_missing(val):
    if pd.isna(val):
        return "none"
    else:
        return val

if __name__ == '__main__':
    main()
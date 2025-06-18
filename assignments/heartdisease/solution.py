import pandas as pd
import numpy as np

def main():
    # Load the dataset
    df = pd.read_csv("heart.csv")

    # 1. Add 'has_disease' column
    df["has_disease"] = df["num"].apply(lambda x: True if x > 0 else False)

    # 2a. Average age: with vs. without heart disease
    age_with_disease = df[df["has_disease"] == True]["age"].tolist()
    age_without_disease = df[df["has_disease"] == False]["age"].tolist()

    print("Average age with heart disease:", round(np.mean(age_with_disease), 2))
    print("Average age without heart disease:", round(np.mean(age_without_disease), 2))
    print()

    # 2b. Average max heart rate (thalach): male vs. female
    male_hr = df[df["sex"] == 1]["thalach"].tolist()
    female_hr = df[df["sex"] == 0]["thalach"].tolist()

    print("Average max heart rate for males:", round(np.mean(male_hr), 2))
    print("Average max heart rate for females:", round(np.mean(female_hr), 2))
    print()

    # 2c. Average cholesterol by chest pain type
    print("Average cholesterol by chest pain type:")
    for cp_type in sorted(df["cp"].unique()):
        cp_chol = df[df["cp"] == cp_type]["chol"].tolist()
        print(f"  Chest pain type {float(cp_type)}: {round(np.mean(cp_chol), 2)}")
    print()

    # 2d. Average resting BP: exang = yes vs. no
    bp_exang = df[df["exang"] == 1]["trestbps"].tolist()
    bp_no_exang = df[df["exang"] == 0]["trestbps"].tolist()

    print("Avg resting BP with exercise-induced angina:", round(np.mean(bp_exang), 2))
    print("Avg resting BP without exercise-induced angina:", round(np.mean(bp_no_exang), 2))
    print()

    # 2e. Count of each slope type
    print("Count of slope types:")
    for slope_val in sorted(df["slope"].unique()):
        count = len(df[df["slope"] == slope_val])
        print(f"  Slope {float(slope_val)}: {count} patients")
    print()

    # 2f. Count of each thal result
    print("Count of thalassemia results:")
    for thal_val in sorted(df["thal"].unique()):
        count = len(df[df["thal"] == thal_val])
        print(f"  Thal {thal_val}: {count} patients")

if __name__ == "__main__":
    main()

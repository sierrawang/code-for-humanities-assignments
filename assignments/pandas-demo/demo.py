import pandas as pd
import csv

NUM_STUDENTS = 9915
NUM_FACULTY = 2345

def main():
    # Load the data
    df = pd.read_csv("stanford.csv")
    df = df[["grad_students", "faculty" ]]
    print(df)
    x = [ "7.0", "6.5"]
    for i in range(len(x)):
        x[i] = float(x[i])

    # Convert the values in the faculty column to be percentages


    # Calculate the student to faculty ratio in each department
    # (handle any missing values as zero)

if __name__ == "__main__":
    main()
import pandas as pd

def main():
    # Load the dataframe
    df = pd.read_csv('student_grades.csv')

    # Print each student's name
    print("Available students:")
    for index, row in df.iterrows():
        print(f"- {row['student_name']}")

    # Add a new line
    print()

    # Prompt the user for the name and assignment 
    student_name = input("Enter a student name: ")
    assignment = input("Which grade are you interested in (homework, midterm, final)? ")
    print()

    # Search for the student and print their grade
    student_row = df[df['student_name'] == student_name]
    if len(student_row) == 1:
        grade = student_row[assignment].iloc[0]
        print(f"{student_name} got an {grade} on the {assignment}.")

if __name__ == '__main__':
    main()

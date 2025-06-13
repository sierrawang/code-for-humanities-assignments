import pandas as pd

def get_percent_survived(df):
    # Loop over all passengers in the df and count the number survived
    num_survived = 0
    for index,row in df.iterrows():
        if row['Survived'] == 1:
            num_survived += 1

    # Print the percent that survived overall
    percent_survived = num_survived / len(df) * 100

    return percent_survived

def main():
    df = pd.read_csv('titanic_data.csv')
    print(f"We have data on {len(df)} passengers on the titanic.")

    # Get the percent of all passengers who survived
    percent_survived = get_percent_survived(df)
    print(f"{percent_survived:.2f}% survived the titanic.")

    # Get the percent of women who survived
    women_df = df[df['Sex'] == 'female']
    percent_women_survived = get_percent_survived(women_df)
    print(f"{percent_women_survived:.2f}% of women survived the titanic.")

if __name__ == '__main__':
    main()
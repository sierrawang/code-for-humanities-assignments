import pandas as pd

def main():
    # Load the csv into a dataframe
    df = pd.read_csv('professors.csv')

    # Print the number of rows in the df
    # print(f"There are {len(df)} professors in this class!")

    # sorted_profs = df.sort_values(by=['hair_length', 'name'], ascending=True)
    # for index,row in sorted_profs.iterrows():
    #     print(f'{row["hair_length"]}, {row["name"]}')

    no_history_or_religion = df[(df['department'] != 'History') & (df['department'] != 'Religious Studies')]
    # notna_series = no_history_or_religion['name'].notna()
    # print(notna_series)

    # no_missing = no_history_or_religion[notna_series]
    print(no_history_or_religion)

    # Get a series reflecting who the history professors are
    # is_history_series = df["department"] == "History"
    # print(is_history_series)

    # # Get the department column
    # department_column = df["department"]
    # print(department_column)
    # print("****************")

    # # Get a dataframe of the history professors
    # history_profs_df = df[df["department"] == "History"]
    # print(history_profs_df)

    # Loop over every row in the dataframe and print out the values
    # for bob in df.iterrows():
    #     bob_index = bob[0]
    #     bob_row = bob[1]
        
    #     print(bob)
    #     # print(f"{bob_index}: {bob_row}")
    #     print('~~~~~~~~~')
    #     print()
    #     # print(f"Professor {bob_row['name']} studies {bob_row['department']} and has {bob_row['hair_length']} hair!")


if __name__ == '__main__':
    main()

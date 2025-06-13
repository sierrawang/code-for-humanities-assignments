import pandas as pd

def main():
    # Load the csv into a dataframe
    df = pd.read_csv('professors.csv')

    # Print the number of rows in the df
    print(f"There are {len(df)} professors in this class!")
	


if __name__ == '__main__':
    main()

import pandas as pd

# Load the specified csv file 
# Return a DataFrame
def load_names_dataframe(file_path="data.csv"):
    return pd.read_csv(file_path)

# Return the number of citizens in the DataFrame
def num_citizens(df):
    return df['Count'].sum()

# Return the number of US citizens born in the specified year 
# with the specified name
def num_year_and_name(name, year, names_df):
    # Filter the DataFrame for the specified name and year
    filtered_df = names_df[(names_df['Name'] == name) & (names_df['Year'] == year)]
    return num_citizens(filtered_df)

# Return the probability of a US citizen being born in the specified year 
# with the specified name
def prob_year_and_name(name, year, names_df):
    return num_year_and_name(name, year, names_df) / num_citizens(names_df)

# Return the probability of a US citizen having the specified name
def prob_name(name, names_df):
    # Filter the DataFrame for the specified name
    filtered_df = names_df[names_df['Name'] == name]
    return num_citizens(filtered_df) / num_citizens(names_df)

# Return the probability of a US citizen being born in the specified year
# given the specified name
def prob_year_given_name(name, year, names_df):
    return prob_year_and_name(name, year, names_df) / prob_name(name, names_df)

def main():
    # Load the names DataFrame
    names_df = load_names_dataframe()

    # Run an interactive loop to get user input
    while True:
        # Get user input
        name = input("Enter a name (or 'q' to quit): ")
        if name.lower() == 'q':
            break
        year = int(input("Enter a year: "))

        # Calculate and print the probabilities
        prob = prob_year_given_name(name, year, names_df)
        print(f"The probability of a US citizen being born in {year} with the name {name} is: {prob:.6f}")
    
if __name__ == "__main__":
    main()
import pandas as pd
import csv

# Return a standardized version of the given name
def standardize_name(name):
    clean_name = ""
    for ch in name:
        if ch.isalpha() or ch == " ":
            clean_name += ch

    # Remove any leading/trailing whitespace
    clean_name = clean_name.strip()

    # Make it lowercase
    clean_name = clean_name.lower()

    return clean_name

# Parse the given date and return just the year, as a string
# For example, given "1720-12-13T00:00:00Z", return "1720"
def get_year(date):
    date = str(date)
    year = date[:4]
    return year

# Return True/False for whether the given name is in the given df
def in_df(name, birth_year, death_year, df):
    matches = df[(df['name'] == name) & (df['birth_year'] == birth_year) & (df['death_year'] == death_year)]
    return len(matches) > 0

# Return a string version of the year
# Make sure that there is no decimal point (e.g. 2020, not 2020.0)
def format_year(year):
    if pd.isna(year):
        return ""
    else:
        year = int(year)
        year = str(year)
        return year

def main():
    # Load the travelers csv into a dataframe
    travelers_df = pd.read_csv('travelersforpython.csv')

    # Add a new column to the travelers dataframe that contains standardized versions of the names
    travelers_df['name'] = travelers_df['travelerNames'].apply(standardize_name)
    travelers_df['birth_year'] = travelers_df['birthDate'].apply(format_year)
    travelers_df['death_year'] = travelers_df['deathDate'].apply(format_year)

    # Load the Wikidata CSV
    wikidata_df = pd.read_csv('query.csv')

    # Add a new column to the wikidata dataframe that contains standardized versions of the names
    wikidata_df['name'] = wikidata_df['personLabel'].apply(standardize_name)
    wikidata_df['birth_year'] = wikidata_df['birthDate'].apply(get_year)
    wikidata_df['death_year'] = wikidata_df['deathDate'].apply(get_year)

    # Define the order of columns
    fieldnames = ['name', 'birth_year', 'death_year']

    # Open the output CSV and write rows using csv.writer
    with open('matched_travelers.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(fieldnames)

        # Loop over every person in the travelers df and check if they are  in the wikidata df
        count = 0
        for index,row in travelers_df.iterrows():
            if in_df(row['name'], row['birth_year'], row['death_year'], wikidata_df):
                writer.writerow([row['name'], row['birth_year'], row['death_year']])
                count += 1
        print(count)

if __name__ == '__main__':
    main()

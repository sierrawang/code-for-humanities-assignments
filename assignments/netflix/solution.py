import pandas as pd
import csv

# Define a function to replace any missing values with "Unknown"
def is_missing(value):
    if pd.isna(value):
        return "Unknown"
    else:
        return value

def main():
    # load the data
    df = pd.read_csv('netflix.csv')  # or whatever your filename is

    # use .apply() with that function
    df['complete_director'] = df['director'].apply(is_missing)
    df['complete_cast'] = df['cast'].apply(is_missing)

    fieldnames = ['title', 'director', 'cast']

    # Step 4: write out to CSV using csv.writer
    output_file = 'tv_shows.csv'
    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        
        # write header
        writer.writerow(fieldnames)
        
        # write data rows
        for index,row in df.iterrows():
            writer.writerow([row['title'], row['complete_director'], row['complete_cast']])

if __name__ == '__main__':
    main()
import pandas as pd


def get_ratio(row, pop_df, column_title):
    date = row['Date']
    year = date[:4]
    population_in_year = pop_df[pop_df['Year'] == int(year)]['Population'].values[0]
    return round(row[column_title] / population_in_year, 4)

def main():
    mta_df = pd.read_csv('mta_ridership.csv')
    nyc_population_df = pd.read_csv('nyc_population.csv')
    mta_df["Year"] = mta_df["Date"].str[:4]
    
    for column in mta_df.columns:
        if column != "Date":
            mta_df[column + '_per_capita'] = mta_df.apply(get_ratio, axis=1, pop_df=nyc_population_df, column_title=column)

    only_per_capita_columns = [col for col in mta_df.columns if col.endswith('_per_capita')]
    mta_per_capita_df = mta_df[['Date'] + only_per_capita_columns]

    mta_per_capita_df.to_csv('mta_per_capita.csv', index=False, encoding='utf-8')
            



if __name__ == '__main__':
    main()
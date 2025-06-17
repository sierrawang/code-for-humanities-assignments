import pandas as pd
import csv

# Load your DataFrame (example: reading from a CSV)
df = pd.read_csv('sentiment_data.csv')

# with open('sentiment_data_sample.csv', 'w') as file:
#     writer = csv.writer(file)
#     writer.writerow(['Index', 'Comment', 'Sentiment'])
#     for index,row in df.iterrows():
#         user_input = input(f'{row["Comment"]} (y/n): ')
#         if user_input == 'y':
#             writer.writerow([index, row['Comment'], row['Sentiment']])




# Take a random sample (e.g., 10% of the data or 100 rows)

sample_df = df.sample(n=30, random_state=42)  # or use n=100 for fixed number of rows

# Write the sampled DataFrame to a new CSV file
sample_df.to_csv('sentiment_data_sample.csv', index=False)

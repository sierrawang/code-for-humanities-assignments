import pandas as pd
from openai import OpenAI
import json


client = OpenAI(api_key="your api key here")  # Replace with your actual OpenAI API key

def get_good_or_bad_news(name_of_incident, impact):
    response = client.responses.create(
        model="gpt-4o",
        input=f"""
        You are an event analyst. Determine if the news is good or bad based on the incident name, impact, and outcome. 
        Incident Name: {name_of_incident}
        Impact: {impact}
        Respond with one word. Either "good" if the incident and impact are considered positive, or "bad" if they are negative.
        """
    )
    
    response_str = response.output_text.strip().lower()
    return response_str



def main():
    df = pd.read_csv('important_dates.csv')
    news_result = []
    for index, row in df.iterrows():
        print(f"Processing row {index + 1}/{len(df)}: {row['Name of Incident']}")
        name_of_incident = row['Name of Incident']
        impact = row['Impact']
        is_good_news = get_good_or_bad_news(name_of_incident, impact)
        news_result.append(is_good_news)
    df['Is Good News'] = news_result
    # filter to only good news
    good_news_df = df[df['Is Good News'] == "good"]
    good_news_df.to_csv('good_news.csv', index=False, encoding='utf-8')


if __name__ == '__main__':
    main()
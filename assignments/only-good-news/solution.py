import pandas as pd
from openai import OpenAI
import json


client = OpenAI(api_key="<your_api_key_here>")  # Replace with your actual OpenAI API key

def get_good_or_bad_news(name_of_incident, impact):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": "You are an event analyst. Determine if the news is good or bad based on the incident name, impact, and outcome. Respond with a json object that has one attribute: is_good_news, which is a boolean value. If the news is good, set is_good_news to true; otherwise, set it to false."
            },
            {
                "role": "user",
                "content": f"Incident: {name_of_incident}\nImpact: {impact}"
            }
        ],
        response_format={"type": "json_object"}
    )
    
    response_str = response.choices[0].message.content
    response_json = json.loads(response_str)
    return response_json.get('is_good_news', False)



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
    good_news_df = df[df['Is Good News'] == True]
    good_news_df.to_csv('good_news.csv', index=False, encoding='utf-8')


if __name__ == '__main__':
    main()
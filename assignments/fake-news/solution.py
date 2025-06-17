import pandas as pd
from openai import OpenAI
import csv

# Initialize the OpenAI client
client = OpenAI(api_key="your api here")  # Replace with your actual OpenAI API key

# Send the incident to GPT and have it classify whether it is "Good news" or "Bad news"
def get_gpt_classification(incident_name, impact):
    response = client.responses.create(
        model="gpt-4o-mini",
        input=f"""
        You are a fake news detector. Given a title and article, your goal is to determine if the news is real or fake. 
        Title: {incident_name}
        Article: {impact}
        Respond with ONE word. Either "real" if you think the news article depicts a real event, or "fake" if you think it is fake news.
        """
    )
    
    return response.output_text.strip()

def main():
    # Load the data
    df = pd.read_csv('news.csv')
    total_real = 100
    total_fake = 100
    false_positive_count = 0
    false_negative_count = 0
    true_positive_count = 0
    true_negative_count = 0


    for idx, row in df.iterrows():
        print(f"Processing row {idx + 1}/{len(df)}: {row['title']}")
        
        # Use GPT to classify the news as true or false
        title = row['title']
        article = row['text']
        gpt_response = get_gpt_classification(title, article)
        
        # Output the result to a new csv file
        df.at[idx, 'Classification'] = gpt_response
        if gpt_response.lower() == "real" and row["is_fake"] == False:
            true_positive_count += 1
        elif gpt_response.lower() == "fake" and row["is_fake"] == True:
            true_negative_count += 1
        elif gpt_response.lower() == "fake" and row["is_fake"] == False:
            false_positive_count += 1
        elif gpt_response.lower() == "real" and row["is_fake"] == True:
            false_negative_count += 1
        else:
            print(gpt_response == "real")
            print(f"Unexpected response: {gpt_response} for row {idx + 1}")

    # Calculate accuracy
    accuracy = (true_positive_count + true_negative_count) / len(df) * 100
    false_positive_rate = false_positive_count / total_fake
    false_negative_rate = false_negative_count / total_real

    print(f"Accuracy: {accuracy:.2f}%")
    print(f"False Positive Rate: {false_positive_rate:.2f}")
    print(f"False Negative Rate: {false_negative_rate:.2f}")


if __name__ == '__main__':
    main()
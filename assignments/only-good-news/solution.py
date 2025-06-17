import pandas as pd
from openai import OpenAI
import csv

# Initialize the OpenAI client
client = OpenAI(api_key="")  # Replace with your actual OpenAI API key

# Send the incident to GPT and have it classify whether it is "Good news" or "Bad news"
def get_gpt_classification(incident_name, impact):
    response = client.responses.create(
        model="gpt-4o-mini",
        input=f"""
        You are an event analyst. Determine if the news is good or bad based on the incident name, impact, and outcome. 
        Incident Name: {incident_name}
        Impact: {impact}
        Respond with one word. Either "good" if the incident and impact are considered positive, or "bad" if they are negative.
        """
    )
    
    return response.output_text

def main():
    # Load the data
    df = pd.read_csv('important_dates.csv')

    column_names = ['Name of Incident', 'Impact', 'Classification']

    with open("classifications.csv", "w") as file:
        # Initialize a writer object
        writer = csv.writer(file)

        # Write the column names
        writer.writerow(column_names)

        # Loop over each row in the dataframe and classify the accident as good or bad
        for index, row in df.iterrows():
            print(f"Processing row {index + 1}/{len(df)}: {row['Name of Incident']}")
            
            # Use GPT to classify the event as good or bad
            name_of_incident = row['Name of Incident']
            impact = row['Impact']
            gpt_response = get_gpt_classification(name_of_incident, impact)
            
            # Output the result to a new csv file
            writer.writerow([name_of_incident, impact, gpt_response])


if __name__ == '__main__':
    main()
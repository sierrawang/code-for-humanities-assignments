import json
import pandas as pd

def load_fruit_dict():
    with open("fruit_counts.json", "r") as file:
        fruit_counts = json.load(file)
        return fruit_counts
    
def load_study_data_df():
    return pd.read_csv("study_data_with_practice.csv")
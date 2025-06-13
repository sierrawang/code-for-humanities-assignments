import pandas as pd

def avg_time_spent_alone(df):
    total = 0
    for index, row in df.iterrows():
        total += row["Time_spent_Alone"]
    return total / len(df)

def main():
    # Load the data
    df = pd.read_csv("personality_dataset.csv")

    # Drop all rows with an empty "Time_spent_Alone"
    has_time_spent_alone = df[df["Time_spent_Alone"].notna()]

    # Get the time spent alone for each personality type
    extroverts_df = has_time_spent_alone[has_time_spent_alone["Personality"] == "Extrovert"]
    extroverts_time_alone = avg_time_spent_alone(extroverts_df)
    print(f"Average alone time for extroverts: {extroverts_time_alone:.2f}")

    introverts_df = has_time_spent_alone[has_time_spent_alone["Personality"] == "Introvert"]
    avg_alone_time_intro = avg_time_spent_alone(introverts_df)
    print(f"Average alone time for introverts: {avg_alone_time_intro:.2f}")

    # Who has the most friends
    N = 3
    top_posters = df.sort_values(by="Friends_circle_size", ascending=False).head(N)
    print(f"\nTop {N} people with the most friends:")
    print(top_posters)

    # Who didn't report going outside?
    missing_outside = df[df["Going_outside"].isna()]
    print(f"\nNumber of people who did not report on going outside: {len(missing_outside)}")

    # Step 6: Drop rows with missing 'Time_spent_Alone' or 'Going_outside'
    cleaned_df = df.dropna(subset=["Time_spent_Alone", "Going_outside"])
    print(f"\nNumber of entries after dropping missing data: {len(cleaned_df)}")

    # Step 7: Social and stage-shy individuals
    social_shy_df = df[(df["Social_event_attendance"] > 3) & (df["Stage_fear"] == "Yes")]
    print(f"\nNumber of people who attend >3 social events and have stage fear: {len(social_shy_df)}")

if __name__ == '__main__':
    main()

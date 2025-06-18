import pandas as pd
import numpy as np

def main():
    # Load datasets
    red_df = pd.read_csv("winequality-red.csv")
    white_df = pd.read_csv("winequality-white.csv")

    # 1. Print number of samples for each wine type
    print("Number of red wine samples:", len(red_df))
    print("Number of white wine samples:", len(white_df))
    print()

    # 2. Average alcohol content by wine type
    red_avg_alcohol = red_df["alcohol"].mean()
    white_avg_alcohol = white_df["alcohol"].mean()
    print(f"Average alcohol content (red): {red_avg_alcohol:.2f}")
    print(f"Average alcohol content (white): {white_avg_alcohol:.2f}")
    print()

    # 3. Mean pH by quality level (red wine only)
    print("Red wine: Mean pH by quality level:")
    red_qualities = red_df['quality'].unique()
    for quality in red_qualities:
        red_ph_by_quality = red_df[red_df['quality'] == quality]["pH"].mean()
        print(f"{quality}: {red_ph_by_quality:.3f}")
    print()

    # 4. Mean sulphates by quality level (red wine only)
    print("Red wine: Mean sulphates by quality level:")
    red_qualities = red_df['quality'].unique()
    for quality in red_qualities:
        red_ph_by_quality = red_df[red_df['quality'] == quality]["sulphates"].mean()
        print(f"{quality}: {red_ph_by_quality:.3f}")
    print()

    # 5. Top 5 wines with highest alcohol (from both datasets)
    red_top5 = red_df.sort_values(by="alcohol", ascending=False)[:5]['alcohol'].to_list()
    white_top5 = white_df.sort_values(by="alcohol", ascending=False)[:5]['alcohol'].to_list()

    print("Top 5 red wines by alcohol content:")
    print(red_top5)
    print()
    print("Top 5 white wines by alcohol content:")
    print(white_top5)
    print()

    # 6. Average quality score for wines with alcohol > 12%
    red_high_alcohol = red_df[red_df["alcohol"] > 12]
    white_high_alcohol = white_df[white_df["alcohol"] > 12]

    print(f"Average quality (red, alcohol > 12%): {red_high_alcohol['quality'].mean():.2f}")
    print(f"Average quality (white, alcohol > 12%): {white_high_alcohol['quality'].mean():.2f}")

if __name__ == "__main__":
    main()

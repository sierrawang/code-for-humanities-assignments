import pandas as pd

# Load the specified csv file 
# Return a DataFrame
def load_titanic_dataframe(file_path="data.csv"):
    return pd.read_csv(file_path)

# Return a dataframe containing only the rows with the given features
def filter_dataframe_by_features(features, df):
    # Make a copy of the dataframe
    df_copy = df.copy()

    # Filter the dataframe based on the features
    for key, value in features.items():
        df_copy = df_copy[df_copy[key] == value]

    return df_copy

# Return the probability of survival for the given features
# features is a dictionary with the following possible keys:
# - 'Pclass': 1, 2, or 3
# - 'Sex': male or female
# - 'Age': a number
# - 'SibSp': number of siblings or spouses aboard
# - 'Parch': number of parents or children aboard
def get_probability_of_survival(features, df):
    # Check if the features are valid
    valid_features = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch']
    for feature in features.keys():
        if feature not in valid_features:
            print(f"Invalid feature: {feature}")
            return None

    # Get the dataframe containing only the rows with the given features
    specified_df = filter_dataframe_by_features(features, df)

    # Get the dataframe containing only the rows with the given features and survived
    survived_feature = { "Survived": 1 }
    survived_df = filter_dataframe_by_features(survived_feature, specified_df)

    # Calculate the probability of survival
    if len(specified_df) == 0:
        return 0
    else:
        probability_of_survival = len(survived_df) / len(specified_df)
        return probability_of_survival

# Return the set of features that result in the highest chance of survival
def get_highest_chance_of_survival():
    pass

def get_pclass(features):
    pclass = input("Enter a Pclass (1, 2, 3, or none): ")
    if pclass in ['1', '2', '3']:
        features['Pclass'] = int(pclass)
    elif pclass.lower() == 'none':
        pass
    else:
        print("Invalid Pclass.")

def get_sex(features):
    sex = input("Enter a gender (male, female, or none): ")
    if sex in ['male', 'female']:
        features['Sex'] = sex
    elif sex.lower() == 'none':
        pass
    else:
        print("Invalid gender.")

if __name__ == "__main__":
    # Load the titanic DataFrame
    titanic_df = load_titanic_dataframe()

    # Run an interactive loop to get user input
    while True:
        # Get user input
        features = {}
        get_pclass(features)
        get_sex(features)

        prob = get_probability_of_survival(features, titanic_df)
        print(f"The probability of survival for the given features is: {prob:.6f}")

        # Check if the user wants to quit
        quit = input("Do you want to quit? (y/n): ")
        if quit.lower() == 'y':
            break
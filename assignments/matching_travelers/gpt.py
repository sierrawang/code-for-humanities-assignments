# match_travelers_simple.py

import pandas as pd

# 1. Load the CSVs
df_travel = pd.read_csv('travelersforpython.csv')
df_wikidata = pd.read_csv('query.csv')

# 2. Preprocess dates
df_travel['birthDate'] = pd.to_datetime(df_travel['birthDate'], errors='coerce')
df_travel['deathDate'] = pd.to_datetime(df_travel['deathDate'], errors='coerce')

df_wikidata['birthDate'] = pd.to_datetime(df_wikidata['birthDate'], errors='coerce')
df_wikidata['deathDate'] = pd.to_datetime(df_wikidata['deathDate'], errors='coerce')

# 3. Preprocess names: strip whitespace, lowercase
df_travel['traveler_clean'] = df_travel['travelerNames'].str.strip().str.lower()
df_wikidata['label_clean'] = df_wikidata['personLabel'].str.strip().str.lower()

# 4. Loop through travelers and check for exact name + date matches
matched_rows = []
for idx, trav in df_travel.iterrows():
    t_name = trav['traveler_clean']
    t_birth = trav['birthDate']
    t_death = trav['deathDate']
    
    for widx, wiki in df_wikidata.iterrows():
        w_name = wiki['label_clean']
        w_birth = wiki['birthDate']
        w_death = wiki['deathDate']
        
        # Check name match
        if t_name != w_name:
            continue
        
        # Check dates (exact match, or both NaT)
        if pd.isna(t_birth) and pd.isna(w_birth):
            birth_match = True
        else:
            birth_match = (not pd.isna(t_birth) and not pd.isna(w_birth) and t_birth == w_birth)
        
        if pd.isna(t_death) and pd.isna(w_death):
            death_match = True
        else:
            death_match = (not pd.isna(t_death) and not pd.isna(w_death) and t_death == w_death)
        
        if birth_match and death_match:
            matched_rows.append({
                'travelerName': trav['travelerNames'],
                'birthDate': t_birth.date() if not pd.isna(t_birth) else '',
                'deathDate': t_death.date() if not pd.isna(t_death) else '',
                'wikidataBirthDate': w_birth.date() if not pd.isna(w_birth) else '',
                'wikidataDeathDate': w_death.date() if not pd.isna(w_death) else '',
                'odnbID': wiki['odnbID']
            })

# 5. Create result DataFrame and write to CSV
df_matches = pd.DataFrame(matched_rows, columns=[
    'travelerName',
    'birthDate',
    'deathDate',
    'wikidataBirthDate',
    'wikidataDeathDate',
    'odnbID'
])
df_matches.to_csv('matched_travelers.csv', index=False)

print(f"Found {len(df_matches)} matched traveler(s). Output written to matched_travelers.csv.")




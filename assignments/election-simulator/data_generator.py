import random
import numpy as np
import csv

# -----------------------------
# 1. Setup: Define Party Lists
# -----------------------------

# List of valid political parties
general_list_of_parties = [
    'Harmony Party',
    'Red Party',
    'Justice and Truth',
    'Adventure Alliance',
    'Animal Friends Party',
    'Go Greens!',
    'Yo-ho-ho Pirate Party'
]

# List of intentionally incorrect or malformed party names (used later for "bad" ballots)
general_list_of_parties_d = [
    'Go Grass!',
    'Advertisement Party',
    'Pink Party',
    'Justice and Teeth',
    'SDP',
    'Party like a Racoon',
    'Pickle Ricks',
    'Princess Party'
]

# Set random seed for reproducibility
random.seed(42)

# Probability distribution for parties — gives higher weight to major parties
prob_weights = np.array([0.20, 0.20, 0.20, 0.19, 0.19, 0.01, 0.01])

# ------------------------------------
# 2. Generate Valid Unranked Ballots
# ------------------------------------

votes = []

# Each ballot selects 3 to 7 parties, no preference order
for i in range(3, 8):  # i = number of parties selected
    for _ in range(random.randint(1000, 1500)):  # Number of ballots per size
        selected = list(np.random.choice(general_list_of_parties, size=i, replace=False, p=prob_weights))
        votes.append([str(party) for party in selected])

# -----------------------------------
# 3. Generate Valid Ranked Ballots
# -----------------------------------

votes_ranked = []

# Each ballot selects 2 to 7 parties and ranks them
for i in range(2, 8):
    for _ in range(random.randint(1000, 1500)):
        selected = list(np.random.choice(general_list_of_parties, size=i, replace=False, p=prob_weights))
        
        ranked_vote = []
        for party in general_list_of_parties:
            if party in selected:
                # Assign rank based on position in selection
                ranked_vote.append(selected.index(party) + 1)
            else:
                # Not selected
                ranked_vote.append(0)
        
        votes_ranked.append(ranked_vote)

# Combine ranked and unranked ballots
votes += votes_ranked
random.shuffle(votes)

# ---------------------------------------------
# 4. Generate Invalid / Corrupted Ballots
# ---------------------------------------------

# 4.1 Ballots with all 8 parties selected randomly (possibly duplicated entries)
names_d = []
for i in range(3, 8):
    for _ in range(random.randint(5, 25)):
        names_d.append([str(party) for party in np.random.choice(general_list_of_parties, size=8, replace=True)])

# 4.2 Ballots with invalid ranking offsets (add 2 to valid ranks)
ranks_d = []
for _ in range(random.randint(20, 40)):
    selected = list(np.random.choice(general_list_of_parties, size=7, replace=False, p=prob_weights))
    ranked = [selected.index(party) + 2 for party in general_list_of_parties]
    ranks_d.append(ranked)

# 4.3 Ballots with all ranks set to zero (fully blank)
for _ in range(random.randint(20, 40)):
    comb = list(np.random.choice(general_list_of_parties, size=random.randint(3, 7), replace=False, p=prob_weights))
    ranked = [0 for _ in general_list_of_parties]
    ranks_d.append(ranked)

# 4.4 Ballots with all zeros and a trailing random integer
for _ in range(random.randint(20, 40)):
    comb = list(np.random.choice(general_list_of_parties, size=random.randint(3, 7), replace=False, p=prob_weights))
    ranked = [0 for _ in general_list_of_parties]
    ranked.append(random.randint(0, 1))  # Append noise
    ranks_d.append(ranked)

# Add malformed ballots to dataset
votes += names_d + ranks_d
random.shuffle(votes)

# -----------------------------
# 5. Export to CSV
# -----------------------------

with open("votes.csv", "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerows(votes)

print("votes.csv file successfully created.")

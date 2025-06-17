## Only Good News

In this assignment, you're provided with a CSV file named `important_dates.csv`, which contains a list of major world events from the 1990s. Your task is to generate a new CSV file that includes a **classification** column for each incident.

To determine whether each event qualifies as good or bad news, you'll use the OpenAI API to analyze the incident in each row.

---

### Steps

#### 1. Create a Classification Function

Write a function called `get_gpt_classification(incident_name, impact)` that:

* Takes in the name of the incident and its impact.
* Uses GPT to classify the event as either `"Good"` or `"Bad"`.

#### 2. Process the CSV

* Load the data using the `pandas` library.
* For each row in the dataset, call your classification function.
* Write the results to a new CSV file named `classifications.csv`.

The output CSV should have the following columns:

* `Name of Incident`
* `Impact`
* `Classification`

---

### Note on Subjectivity

Determining whether something is "good" or "bad" news is subjective. A key part of this assignment is reviewing GPT's classifications and reflecting on whether you agree with them. Consider the following:

* Do you agree with the model's label for each event?
* How does the framing of the incident affect the classification?

Keep in mind that GPT might make binary classifications, even in cases where the topic is nuanced.

---

### Optional Extensions

To explore the topic further or challenge yourself, consider implementing one or more of the following extensions:

* **Trend Analysis**: Create a graph showing the distribution of good versus bad news over time.
* **Three-Way Classification**: Modify the classification system to include a `"Neutral"` option in addition to `"Good"` and `"Bad"`.
* **Scoring System**: Ask GPT to assign a positivity score from 1 to 5 for each event, rather than using a binary label. You might consider normalizing or analyzing the score distribution.
* **Event Summaries**: Have GPT generate a concise one-sentence summary for each event to include in your output.
* **Human Evaluation**: Add a column where a human reviewer can agree or disagree with GPT’s classification, and examine how often there is alignment.
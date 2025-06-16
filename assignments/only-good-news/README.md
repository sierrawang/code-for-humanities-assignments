# Only good news
In this challenge, you are given a CSV that contains rows listing important world events that happened during the 1990's. Your task is to generate a new CSV that contains only the rows that contain good news. In order to determine whether a row contains good news, you will need to use the OpenAI API to analyze the text in each row and determine whether it is positive or negative.

Loop through each row in the CSV and create a new column labeled "Is Good News" that contains a boolean value indicating whether the row contains good news or not. If the row contains good news, set the value to True, otherwise set it to False.

After generating these values, create a new CSV file that contains only the rows that contain good news. The new CSV file should have the same columns as the original CSV file, but only contain the rows that have "Is Good News" set to True.

Disclaimer: Good news is subjective. One interesting aspect of this assignment is reviewing the resulting contents and determining whether you agree with the AI's assessment of good news or not. You may find that some rows you consider good news are marked as bad news, and vice versa, or that the AI is making a binary assessment on a nuanced topic.
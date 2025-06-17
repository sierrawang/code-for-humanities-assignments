## Prompt Engineering for Sentiment Classification

In this assignment, you’ll explore how to use GPT for **sentiment classification**. You're provided with a dataset named `sentiment_data_sample.csv`, which contains user comments and their associated sentiment labels:

* `0` = negative
* `1` = neutral
* `2` = positive

This dataset is a small random sample from a larger dataset originally [available on Kaggle](https://www.kaggle.com/datasets/abdelmalekeladjelet/sentiment-analysis-dataset). Using a subset is a common approach when developing prompts—you iterate on a small sample to improve your prompt before running the final version at scale.

---

### Instructions

#### 1. Load the data

Use the `pandas` library to load the `sentiment_data_sample.csv` file. Inspect the dataset to understand the structure and content of the comments and labels.

#### 2. Design a GPT prompt

Your goal is to write a prompt that enables GPT to classify the sentiment of each comment **in a way that matches the provided sentiment labels** (`0` - negative, `1` - neutral, or `2` - positive).
You may need to experiment with how you phrase the instruction to GPT. Focus on:

* Making the task description clear.
* Asking GPT to output only the sentiment label (not extra commentary).

For each row, send the comment text to GPT and collect its predicted label. Then compare GPT's label to the true label to evaluate how well your prompt is performing.

---

### Optional Extensions

Here are some additional directions:

* **Improve with few-shot examples**: Try providing GPT with a few example labeled comments to see if performance improves.
* **Handle uncertainty**: Ask GPT to output a confidence score alongside its prediction, and use this to flag comments for human review.
* **Visualize the sentiment space**: Use ChatGPT to learn about "text embeddings" and how you could use embeddings to convert each comment into a vector and plot the results. Do comments with similar sentiments cluster together?
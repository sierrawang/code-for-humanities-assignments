# Fake News
With the rise of LLMs, convincing misinformation has become easier to generate than ever. In this assignment, you are given a file news.csv, which contains a list of 200 news articles. 100 are real, and 100 are fake. Your task is to use the OpenAI API to classify each article as either "real" or "fake", then calculate the "False positive rate" and the "false negative rate" of your model. Use the following formulas:
False positive rate = the amount of fake articles classified as real / total number of fake articles

False negative rate = the amount of real articles classified as fake / total number of real articles

Try doing this challenge using a Jupyter notebook. You can make a Jupyter notebook like any other file, just add the extension `.ipynb` to the end of the file name.


# Extensions
To explore the topic further or challenge yourself, consider implementing one or more of the following extensions:

* **Confidence Score** - Ask GPT to provide a confidence score for each classification, and analyze the distribution of these scores.

* **Vary the input contents** - Create columns on the Dataframe that consist of GPT's guess based ONLY on the title, and/or ONLY on the article text. Is there a difference in the false positive and false negative rates when using only the title or only the article text?

* **Prompting** See if you can improve the classification accuracy by changing the prompt you use to classify the articles. 

* **Heatmap** - Using `matplotlib` that visualizes the false positive and false negative rates for each article. (Feel free to use ChatGPT to help you with this, however, try not to over complicate the code needed, and try to understand the code you are using.) Here is documentation on how to use `matplotlib` to make a heatmap: [matplotlib heatmap](https://matplotlib.org/stable/gallery/images_contours_and_fields/image_annotated_heatmap.html).

* **Compare with other models** - Classify the news using two different models, such as `GPT-4o-mini`/ `GPT-4o`/`GPT-4.1`. Compare the false positive and false negative rates of each model. Which model performs best? Plot the models against each other using a bar chart.
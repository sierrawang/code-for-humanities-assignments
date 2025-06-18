## Wine Quality Analysis

This exercise uses two real-world datasets containing physicochemical and quality data on Portuguese "Vinho Verde" wines — both **red** and **white** varieties.

Each wine sample includes 11 numeric features based on lab tests (such as acidity, pH, alcohol content), and one **quality score** rated by expert tasters (on a scale from 0 to 10).

There are:

* **1599 samples of red wine**
* **4898 samples of white wine**

Your goal is to explore and analyze the data.

We downloaded this data [from here](https://archive.ics.uci.edu/dataset/186/wine+quality).
> **P. Cortez, A. Cerdeira, F. Almeida, T. Matos and J. Reis (2009).**
> *Modeling wine preferences by data mining from physicochemical properties*.
> In Decision Support Systems, Elsevier, 47(4):547–553.

---

### Your Tasks

* Import `pandas` and `numpy`
* Define your main function
* Load both `winequality-red.csv` and `winequality-white.csv` into pandas DataFrames.
* Print the number of samples for each wine type.
* Calculate the average `alcohol` content for each wine type.
* Compute the mean `pH` for each `quality` level (for red wine).
* Compute the mean `sulphates` for each `quality` level (for red wine).
* What are the average `quality` scores for wines with alcohol > 12%?

Our output:
```
Number of red wine samples: 1599
Number of white wine samples: 4898

Average alcohol content (red): 10.17
Average alcohol content (white): 10.15

Red wine: Mean pH by quality level:
5.0: 3.296
6.0: 3.296
7.0: 3.272
4.0: 3.365
8.0: 3.287
3.0: 3.380
nan: nan

Red wine: Mean sulphates by quality level:
5.0: 0.634
6.0: 0.693
7.0: 0.765
4.0: 0.642
8.0: 0.771
3.0: 0.618
nan: nan

Top 5 red wines by alcohol content:
[14.9, 14.0, 14.0, 14.0, 14.0]

Top 5 white wines by alcohol content:
[13.9, 12.9, 12.9, 12.8, 12.8]

Average quality (red, alcohol > 12%): 6.51
Average quality (white, alcohol > 12%): 6.86
```

### Exentension (Optional)

* Get creative using `matplotlib` to visualize the data.
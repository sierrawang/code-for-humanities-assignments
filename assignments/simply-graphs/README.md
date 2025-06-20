# Assignment: Plotting Practice with Multi-file Programs

In this assignment, you will practice organizing your code into multiple files. You are given two data files:

* `study_data_with_practice.csv`
* `fruit_counts.json`

You will write three Python files:

## 1. data_loaders.py

This file contains the functions that load the data.

You should write two functions:

* `load_fruit_dict()`: This function reads the `fruit_counts.json` file and returns a dictionary containing the fruit names and their counts.
* `load_study_data_df()`: This function reads the `study_data_with_practice.csv` file into a pandas DataFrame and returns it.

Only data loading should happen in this file.

## 2. plot_helpers.py

This file contains the functions that generate the plots using matplotlib. You will also use colors from a `constants.py` file that is provided.

You should write two functions:

* `make_bar_chart(data, xlabel, ylabel, output_filename)`: This function takes a dictionary of data and creates a bar chart. It should label the axes and save the chart to the file given by `output_filename`.
* `make_scatter_plot(x, y, xlabel, ylabel, output_filename)`: This function takes two lists of numbers and creates a scatter plot. It should label the axes and save the plot to the given filename.

Each function should create a new figure, plot the data, label the axes, and save the image.

## 3. main.py

This is the main file that runs the program. You should import the functions from `data_loaders.py` and `plot_helpers.py`, and use them to make the plots.

Inside your `main()` function, do the following:

* Load the fruit data using `load_fruit_dict()` and use it to create a bar chart by calling `make_bar_chart()`.
* Load the study data using `load_study_data_df()` and use it to create a scatter plot by calling `make_scatter_plot()`.

Then call the `main()` function at the bottom of the file.
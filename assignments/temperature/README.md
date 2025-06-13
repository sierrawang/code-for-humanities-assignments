# Temperature

In this assignment you are given a csv file called temperature.csv that contains 5000 temperature readings between 2012 and 2018 in several major cities around the world.

The csv is structured as follows:

Time Column:
`datetime` - The date and time of the reading

City Columns:
`[city_name]` - The temperature reading in the city at the given time ([city_name] is the name of the city, e.g. `New York`)

We have also provided a function, `setup_df` that preprocess the csv file and returns a pandas DataFrame. Your goal is to make a graph displaying 2 or more cities' temperature readings over time. Recall that you can pass in columns of a DataFrame to the `plt.plot` function to plot them on the same graph.

Hint: No changes need to be made to the `datetime` column to display it on the plot. Matplotlib handles datetime objects (a type of timestamp) automatically.

Look at `expected_plot.png` in this folder to see what the final graph should look like.
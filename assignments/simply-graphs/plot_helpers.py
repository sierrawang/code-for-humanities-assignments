import matplotlib.pyplot as plt
from constants import DEFAULT_BAR_COLOR, DEFAULT_SCATTER_COLOR

# Takes in a dictionary of categories and their corresponding values, 
# makes a bar chart, and saves it to the given output filename
def make_bar_chart(data, xlabel, ylabel, output_filename):
    # Wipe the canvas
    plt.figure()

    # Construct the x, y lists
    x = []
    y = []
    for k,v in data.items():
        x.append(k)
        y.append(v)

    # Create and save the bar chart
    plt.bar(x, y, color=DEFAULT_BAR_COLOR)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.savefig(output_filename)

# Takes in two lists and makes a scatter plot
# and saves it to the given output filename 
def make_scatter_plot(x, y, xlabel, ylabel, output_filename):
    # Wipe the canvas
    plt.figure()

    # Create and save the scatter plot
    plt.scatter(x, y, color=DEFAULT_SCATTER_COLOR)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title("Scatter Plot")
    plt.savefig(output_filename)
import matplotlib.pyplot as plt

def plot_ponts(list):
    """
    This function takes a list of points and plots them on a graph.
    Each point is represented as a tuple (x, y).
    """
    x = [point[0] for point in list]
    y = [point[1] for point in list]
    
    plt.scatter(x, y)
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Scatter Plot of Points')
    plt.grid(True)
    plt.show()

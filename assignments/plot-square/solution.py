import matplotlib.pyplot as plt
import random

def main():
    x_data = []
    y_data = []
    for i in range(1000):
        x_data.append(random.random())
        y_data.append(random.random())

    plt.scatter(x_data, y_data)
    plt.title('Random Scatter Plot')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.show()
    plt.savefig('expected_result.png')



if __name__ == '__main__':
    main()
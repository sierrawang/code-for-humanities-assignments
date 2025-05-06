import random
import math
from helper import plot_ponts

def main():
    # Write your code here!
    points = []
    for i in range(100):
        angle = random.random()* 2*math.pi
        x = math.cos(angle)
        y = math.sin(angle)
        points.append((x, y))
    plot_ponts(points)


if __name__ == '__main__':
    main()
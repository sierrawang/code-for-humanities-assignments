# Plot Circle
Generate random points on the perimeter of a circle. Using the `plot_points` function from helper.py, pass in a list of points.
The list of points should be a list of lists, that looks like this:
```python
points = [[x1, y1], [x2, y2], [x3, y3]]
```
where each point is a list of two numbers. The first number is the x-coordinate and the second number is the y-coordinate.

Note: 
`random.random` generates a random float between 0 and 1.
You can get a point on the perimeter of a circle by taking an angle, and using the following equations:
> x = r * cos(angle)
> y = r * sin(angle)


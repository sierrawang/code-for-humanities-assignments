
def draw_triangle():
    # Get the height of the triangle from the user
    height = int(input("Enter the height of the triangle: "))

    # Loop through each level of the triangle
    for i in range(height):
        # Calculate the number of spaces and stars
        spaces = ' ' * (height - i - 1)
        stars = '*' * (i + 1)
        # Print the current level of the triangle
        print(spaces + stars)

if __name__ == "__main__":
    draw_triangle()
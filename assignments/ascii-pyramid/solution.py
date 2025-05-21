
def draw_ascii_pyramid():
    height = int(input("Enter the height of the pyramid: "))

    # Loop through each level of the pyramid
    for i in range(height):
        # Calculate the number of spaces and stars
        spaces = ' ' * (height - i - 1)
        stars = '*' * (2 * i + 1)
        # Print the current level of the pyramid
        print(spaces + stars)

if __name__ == "__main__":
    draw_ascii_pyramid()
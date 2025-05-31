def main():
    # Get the fahrenheit temperature from the user
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))

    # Use the formula to calculate temperature in Celsius
    celsius = (fahrenheit - 32) * 5.0/9.0

    # Output with appropriate units
    print(f"Temperature: {fahrenheit}F = {celsius}C")

if __name__ == '__main__':
    main()
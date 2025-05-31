def main():
    # Get the input from the user
    month = input("Month (1-12): ")
    day = input("Day (1-31): ")
    year = input("Year (e.g., 2025): ")
    
    # Output the result in two formats
    print(f"MM/DD/YYYY format: {month}/{day}/{year}")
    print(f"DD-MM-YYYY format: {day}-{month}-{year}")

if __name__ == "__main__":
    main()

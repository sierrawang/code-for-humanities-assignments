def main():
    # Prompt the user to construct a list of numbers
    # Make an empty list to store integers
    lst = []
    user_input = input("Enter an integer or press enter to stop: ")  
    while user_input != "":  # While the user doesn't enter nothing...
        lst.append(int(user_input))  
        user_input = input("Enter an integer or press enter to stop: ")  

    # Store the count of even numbers in the list
    count = 0  

    # Loop through the numbers in the list
    for num in lst:  
        # If the current number in the list is even (divisible by 2)
        # Add one to our count!
        if num % 2 == 0:  
            count += 1  

    print(count)

if __name__ == '__main__':
    main()
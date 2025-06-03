def main():    
    counter = int(input("Enter a starting number: "))
    step = int(input("Enter a step to count down by: "))

    while counter > 0:
        # Print the current value of the counter
        print(counter)

        # Update the counter
        counter = counter - step
    
    print("Blast off!!!")

if __name__ == '__main__':
    main()

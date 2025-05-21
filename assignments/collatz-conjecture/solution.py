
def main():
    step = 0
    num = int(input("Enter a number: "))
    while True:
        if num == 1:
            # If the number is 1, we are done!
            print(f"Number of steps: {step}")
            break

        # Increment the step counter
        step += 1
        if num % 2 == 0:
            # If the number is even, divide it by 2
            new_num = int(num / 2)
            print(f"{step}. {num} / 2 = {new_num}")
            num = new_num
        else:
            # If the number is odd, multiply it by 3 and add 1
            new_num = num * 3 + 1
            print(f"{step}. {num} * 3 + 1 = {new_num}")
            num = new_num

if __name__ == "__main__":
    main()
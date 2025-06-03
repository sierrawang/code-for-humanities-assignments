import random

def main():
    print("Khansole Academy")
    
    correct_in_a_row = 0

    while correct_in_a_row < 3:
        # Generate two random numbers
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)

        print(f"What is {num1} + {num2}?")
        user_ans = int(input("Your answer: "))
        true_ans = num1 + num2

        if user_ans == true_ans:
            print("Correct!")
            correct_in_a_row += 1
            print(f"You've gotten {correct_in_a_row} correct in a row.")
        else:
            print("Incorrect.")
            correct_in_a_row = 0
            print(f"The expected answer is {true_ans}")
        print()

    print("Congratulations! You mastered addition.")
    
if __name__ == '__main__':
    main()
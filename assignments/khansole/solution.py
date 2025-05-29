import random

def main():
    print("Khansole Academy")
    random_num_1 = random.randint(10, 99)
    random_num_2 = random.randint(10, 99)
    print(f"What is {random_num_1} + {random_num_2}?")
    user_answer = int(input("Your answer: "))
    correct_answer = random_num_1 + random_num_2
    if user_answer == correct_answer:
        print("Correct!")
    else:
        print("Incorrect.")
        print("The expected answer is", correct_answer)
    
if __name__ == '__main__':
    main()
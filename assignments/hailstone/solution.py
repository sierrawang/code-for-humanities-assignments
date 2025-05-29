"""
Write a program that implements the following process.
Have the user input a positive integer, call it n.
If n is even, divide it by two.
If n is odd, multiply it by three and add one.
Continue this process until n is equal to one.
"""

def main():
    # your code here
    num = int(input("Enter a number: "))

    while num > 1:
        
        if num%2 == 1:
            new_num = round(3*num + 1)
            print(num, "is odd, so I make 3n + 1:", new_num)
            num = new_num
        else:
            new_num = round(num/2)
            print(num, "is even, so I take half:", new_num)
            num = new_num




if __name__ == "__main__":
    main()
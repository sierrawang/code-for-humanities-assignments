def main():
    num = int(input("Enter a number: "))

    while num > 1:
        if num % 2 == 1:
            num = 3 * num + 1
        else:
            num = num / 2
        print(num)

if __name__ == "__main__":
    main()
MILES_PER_STADIA = 0.115

def main():
    miles = float(input("Enter distance in miles: "))
    stadia = miles / MILES_PER_STADIA
    print(f"{miles} miles is {stadia} Greek stadia.")

if __name__ == '__main__':
    main()

import math

K = -8266.64  # Half life constant

def main():
    # Ask the user to enter the percent c14 left in their sample
    pct_left = float(input("% of natural c14: "))
    
    # Calculate the age    
    age = K * math.log(pct_left / 100)
    
    # Print the result    
    print(f"Sample is {age} years old.")

if __name__ == '__main__':
    main()
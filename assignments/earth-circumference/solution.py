
def main():
    angle = float(input("What is the angle of the shadow? "))
    distance = float(input("What is the distance between the obelisks (meters)? "))

    circumference = distance * 360 / angle

    print(f"The circumference of the planet is {circumference} meters.")

if __name__ == "__main__":
    main()
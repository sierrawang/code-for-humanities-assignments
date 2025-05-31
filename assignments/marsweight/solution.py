MARS_WEIGHT_MULTIPLIER = 0.378

def main():
    earth_weight = float(input("Enter a weight on Earth: "))
    mars_weight = MARS_WEIGHT_MULTIPLIER * earth_weight
    print(f"The equivalent on Mars: {mars_weight}")

if __name__ == "__main__":
    main()
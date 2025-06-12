import json

filename = "towers.json"

def main():
    # TODO: Your code goes here!
    with open(filename, 'r') as file:
        data = json.load(file)

    # print out the oldest tower
    oldest_tower = ""
    oldest_tower_age = 0
    youngest_tower = ""
    youngest_tower_age = float('inf')
    tallest_tower = ""
    tallest_tower_height = 0
    shortest_tower = ""
    shortest_tower_height = float('inf')

    for tower in data:
        name = tower['name']
        age = tower['age']
        height = tower['height']

        if age > oldest_tower_age:
            oldest_tower_age = age
            oldest_tower = name

        if age < youngest_tower_age:
            youngest_tower_age = age
            youngest_tower = name

        if height > tallest_tower_height:
            tallest_tower_height = height
            tallest_tower = name

        if height < shortest_tower_height:
            shortest_tower_height = height
            shortest_tower = name
    print(f"The oldest tower is {oldest_tower} with an age of {oldest_tower_age} years.")
    print(f"The youngest tower is {youngest_tower} with an age of {youngest_tower_age} years.")
    print(f"The tallest tower is {tallest_tower} with a height of {tallest_tower_height} meters.")
    print(f"The shortest tower is {shortest_tower} with a height of {shortest_tower_height} meters.")
        

if __name__ == '__main__':
    main()
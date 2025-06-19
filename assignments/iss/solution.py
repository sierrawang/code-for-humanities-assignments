import requests
import time
import json

def main():
    # Fetch the ISS location data from the API


    for i in range(100):
        response = requests.get("https://api.wheretheiss.at/v1/satellites/25544")
        response_json = response.json()
        curr_time = time.time()
        curr_time_str = str(curr_time)
        curr_time_str = curr_time_str.split(".")[0]
        print(f"Current time: {curr_time_str}", i)
        with open(f"./data/{curr_time_str}.json", "w") as file:
            json.dump(response_json, file, indent=4)
        time.sleep(1)



if __name__ == '__main__':
    main()
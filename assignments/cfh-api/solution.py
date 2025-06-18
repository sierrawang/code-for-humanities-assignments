import requests
import csv

def write_csv(csv_text, filename):
    with open(filename, "w", newline='') as csvfile:
        csvfile.write(csv_text) 

def main():
    endpoint = "https://codeforhumanities.stanford.edu/days/metadata.json"
    response = requests.get(endpoint)
    response_json = response.json()
    url_paths = response_json["assn_csv_urls"]
    for url_path in url_paths:
        csv_response = requests.get(url_path)
        csv_text = csv_response.text
        filename = url_path.split("/")[-1]
        write_csv(csv_text, filename)

if __name__ == '__main__':
    main()

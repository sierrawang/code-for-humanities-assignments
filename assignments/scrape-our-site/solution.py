from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://codeforhumanities.stanford.edu"

def main():
    driver = webdriver.Chrome()
    
    driver.get(URL)
    driver.implicitly_wait(1)
    event_titles = driver.find_elements(By.CLASS_NAME, "event-title")
    event_concepts = driver.find_elements(By.CLASS_NAME, "event-concepts")
    event_types = driver.find_elements(By.CLASS_NAME, "event-type")

    for i in range(len(event_titles)):
        print(event_titles[i].text)
        print(event_concepts[i].text)
        print(event_types[i].text)
        print("~~~~~~~~~~~")



if __name__ == "__main__":
    main()
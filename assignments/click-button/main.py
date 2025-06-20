from selenium import webdriver
from selenium.webdriver.common.by import By
import time

URL = "https://www.rapidtables.com/tools/click-counter.html"

def main():
    driver = webdriver.Chrome()
    
    driver.get(URL)
    # TODO: Find the button, and click it 10 times



    # LEAVE THIS CODE. If you don't sleep at the end, it will go to fast for you to see it!
    time.sleep(10)
    driver.quit()



if __name__ == "__main__":
    main()
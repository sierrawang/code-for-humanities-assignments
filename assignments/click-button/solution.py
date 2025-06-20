from selenium import webdriver
from selenium.webdriver.common.by import By
import time

URL = "https://www.rapidtables.com/tools/click-counter.html"

def main():
    driver = webdriver.Chrome()
    
    driver.get(URL)
    driver.implicitly_wait(1)
    add_button = driver.find_element(By.ID, "addbtn")
    for i in range(10):
        add_button.click()

    time.sleep(10)
    driver.quit()



if __name__ == "__main__":
    main()
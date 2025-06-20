from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv


URL = "https://www.jpl.nasa.gov/images/"

# This function scrolls the page until the specified element is in view.
def scroll_to_element(driver, element):
    """Scrolls the page until the specified element is in view."""
    driver.execute_script("arguments[0].scrollIntoView();", element)
    time.sleep(1)  # Wait for the scroll to complete






def main():
    driver = webdriver.Chrome()
    # TODO: write your code below

    driver.quit()

if __name__ == "__main__":
    main()
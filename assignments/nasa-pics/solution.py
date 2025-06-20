from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv


URL = "https://www.jpl.nasa.gov/images/"

def scroll_to_element(driver, element):
    """Scrolls the page until the specified element is in view."""
    driver.execute_script("arguments[0].scrollIntoView();", element)
    time.sleep(1)  # Wait for the scroll to complete






def get_page_info(driver, row_list):
    image_elements = driver.find_elements(By.CLASS_NAME, "BaseImage")
    for img_el in image_elements:
        row_list.append([img_el.get_attribute("src")])




def main():
    driver = webdriver.Chrome()
    rows = []
    driver.get(URL)
    time.sleep(2)
    get_page_info(driver, rows)
    time.sleep(2)
    next_page = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div/div/div/div/div[2]/div[3]/div/button[2]")
    scroll_to_element(driver, next_page)
    next_page.click()
    time.sleep(2)
    get_page_info(driver, rows)
    time.sleep(2)
    with open("all_images.csv", "w") as file:
        writer = csv.writer(file)
        writer.writerow([
            "image_url"
        ])
        writer.writerows(rows)

    driver.quit()

if __name__ == "__main__":
    main()
from selenium import webdriver


def main():

    driver = webdriver.Chrome()

    driver.get("https://www.example.com")
    print(driver.title)
    print(driver.current_url)
    print(driver.page_source)
    driver.quit()


if __name__ == "__main__":
    main()
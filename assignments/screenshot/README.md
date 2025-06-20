### Take a Screenshot

1. Write your `main()` function

2. Import Selenium WebDriver:

   ```python
   from selenium import webdriver
   ```

3. Create a WebDriver instance for a Chrome browser:

   ```python
   driver = webdriver.Chrome()
   ```

4. Use the driver to open the course website: `"https://codeforhumanities.stanford.edu/"`

5. Add a short delay so the page can finish loading.

6. Take a screenshot and save it as `homepage.png`.

7. Quit the driver.
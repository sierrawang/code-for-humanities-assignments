# NASA pics

In this challenge, you will scrape two pages of picture URLs from the NASA website:
https://www.jpl.nasa.gov/images/

Remember, to view the HTML of one of the images on the page you can right click the image and select "Inspect". This will open the developer tools and highlight the HTML for that image.
once you have fetched the URLs from two pages, write them to a .txt file or a .csv file.

We have provided a `scroll_to_element` function, which is necessary to scroll to the next page button (Red with a right pointing arrow toward the bottom of the page). You will need to scroll this button into view before clicking it.




### Hints
Images have the html tag `<img>`. You can use the `find_elements(By.TAG_NAME, "img")` method to get a list of all image elements on the page. You can also look for relevant class names like "BaseImage" to narrow down your search.
Once you have the image elements, you can use the `.get_attribute("src")` method to get the URL of each image.

For getting the button element, you can use several strategies. If you are finding it different to isolate the button, you can use the `find_element(By.XPATH, "<xpath>")` method to find the button by its XPath.

In order to get the "XPath" of the button, right click the element IN THE HTML CODE, then select "Copy" -> "Copy full XPath". This will give you the XPath of the element, which is sort of like a unique address for that element in the HTML document.



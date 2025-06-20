# Scrape Our Site
In this assignment, you will scrape OUR website, to extract all of the assignments, handouts, and lessons.

The goal of the assignment is to print out all of the above data. The output should look something like this (Don't worry about the order of the items):

```
Jupyter Notebook
Jupyter Notebook
Slides
~~~~~~~~~~~
My First Jupyter Notebook
Jupyter Notebook
Assignment
~~~~~~~~~~~
Small but Mighty Python Concepts
lambda functionstimeos library
Slides
~~~~~~~~~~~
...
```

In the above, we are printing the "Name" column of the table first, followed by the "New Concepts" column, then the "Links" column. 

To find out what data to scrape, click through the html of our site. Remember, you can go right to the html of specific elements, by right clicking on the element and selecting "Inspect".

Recall that ChatGPT can be a helpful resource in troubleshooting issues with Selenium.

### Hint
Look for the classnames "event-title", "event-concepts", and "event-type"
Remember, you can use the `find_elements(By.CLASS_NAME, "<classname>")` method to get a list of all elements.
Then, once you have an element, you can use the `.text` attribute to get the text of that element.
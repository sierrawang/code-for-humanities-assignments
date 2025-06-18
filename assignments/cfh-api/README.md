# Code for Humanities "API"
Even the Code for Humanities site has a (very poorly documented) API that you can use to get information about the course assignments.

Use a get request to get the endpoint:
`https://codeforhumanities.stanford.edu/days/metadata.json`
This will return a JSON object with the metadata containing the URLS of CSV files with data about the assignments.
Using that list of URLs, make a get request to each of the URLs to get the CSV data for each assignment, and save it as a file on your computer.

# Extension
Count how many concepts we have completed up to day 7 in the course (look at the "Concepts" column in the CSV files) and print that number to the console.
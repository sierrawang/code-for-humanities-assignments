## Setup

* Convert `travelersforpython.numbers` to a CSV file and place it in this folder.
* Download `query.csv` from [this Wikidata query link](https://query.wikidata.org/index.html#SELECT%20%3Fperson%20%3FpersonLabel%20%3FbirthDate%20%3FdeathDate%20%3FodnbID%20WHERE%20%7B%0A%20%20%3Fperson%20wdt%3AP31%20wd%3AQ5%3B%20%23%20Instance%20of%20human%0A%20%20%20%20%20%20%20%20%20%20wdt%3AP1415%20%3FodnbID.%20%23%20ODNB%20ID%0A%20%20OPTIONAL%20%7B%20%3Fperson%20wdt%3AP569%20%3FbirthDate.%20%7D%20%23%20Date%20of%20birth%0A%20%20OPTIONAL%20%7B%20%3Fperson%20wdt%3AP570%20%3FdeathDate.%20%7D%20%23%20Date%20of%20death%0A%20%20%0A%20%20SERVICE%20wikibase%3Alabel%20%7B%20bd%3AserviceParam%20wikibase%3Alanguage%20%22%5BAUTO_LANGUAGE%5D%2Cen%22.%20%7D%0A%7D) and place it here as well.
* Create a new file called `main.py` in this directory.
* At the top of `main.py`, add:

  ```python
  import pandas as pd
  import csv
  ```
* Define `main()` and call it:

  ```python
  def main():
      pass  # you will fill this in

  if __name__ == '__main__':
      main()
  ```

---

## Milestone 1: Load Data, Standardize Names, and Match on Name

In this milestone you will count the number of travelers in `travelersforpython.csv` with the same name as a person in `query.csv`.

1. Load your data into two DataFrames called `travelers_df` and `wikidata_df`.
2. Write a function `standardize_name(name)` that cleans the given string:

   * Keep only alphabetic characters and spaces.
   * Strip leading/trailing whitespace.
   * Convert to lowercase.
   * Return the cleaned string.
3. Add a new column called `name` to each dataframe using the `.apply(standardize_name)`. For example:

   ```python
   travelers_df['name'] = travelers_df['travelerNames'].apply(standardize_name)
   ```
   Note that the original names column in the `query.csv` is called `personLabel`.
4. Write a function `in_df(name, df)` that returns `True` if any row in `df` has the same `name`, and False otherwise.

   ```python
   def in_df(name, df):
       pass
   ```
5. Add a loop in `main()` and loops through each row in `travelers_df` and count how many names are found in `wikidata_df`, then print the count.
   **Expected result:** 1307

---

## Milestone 2: Include Birth Year & Death Year Matching

Extend your implementation to look make sure that the birth year and death year match across the files. This is tricky because the dates are in different formats in each file, so we will standardize the dates for comparison. Specifically, we will add two columns to each dataframe to hold strictly the birth year and death year as strings for that row.

1. Write a function `format_year(year)`:

   * If value is missing (`pd.isna(year)`), return `""`.
   * Otherwise cast it to `int`, then to `str`, then return the result.
   * We will use this function to standardize the dates in `travelers_df`.
2. Add two columns to `travelers_df`, called `birth_year` and `death_year`. Each column should contain the standardized versions of `birthDate` and `deathDate` respectively. Hint: use `.apply(format_year)` - this is similar to what you did to standardize the name column.
3. Write another function `get_year(date)`:

   * Cast `date` to a string and return the first four characters. For example, if given the input "1720-12-13T00:00:00Z", this function should return "1720".
   * We will use this function to standardize the dates in `wikidata_df`.
4. Add two columns to `wikidata_df`, called `birth_year` and `death_year`. Each column should contain the standardized versions of `birthDate` and `deathDate` respectively. Use your function from the previous step to standardize the dates for this dataframe.
4. Update the `in_df` function to check if name, `birth_year`, and `death_year` all match a row in the given df:

   ```python
   def in_df(name, birth_year, death_year, df):
       pass
   ```
5. Loop again and print the new count.
   **Expected result:** 368

---

## Milestone 3: Write Matches to CSV

Write matches to `matched_travelers.csv`:

1. Create a list called fieldnames that contains three values: `name`, `birth_year`, and `death_year`.
2. Define a `filename` variable for your output CSV file (e.g. `matched_travelers.csv`).
3. Open your file for writing, initialize a csv writer, and write the fieldnames to the file:

   ```python
   with open(filename, 'w') as f:
       writer = csv.writer(f)
       writer.writerow(fieldnames)
       # ...
   ```
2. In your loop, when `in_df(...)` is `True`:

   ```python
   writer.writerow([row['name'], row['birth_year'], row['death_year']])
   ```
3. After the loop, your CSV should list all matching travelers with name and years.

---

## Extension: Improving Matching Logic

So far we've used exact matching on `name`, `birth_year`, and `death_year`.
Next steps:

* Inspect cases that fail to match—are there spelling differences?
* Try different matching logic-is there a better method for identifying matches between the two data files?
* Think about what constitutes a good match and adjust your code accordingly.

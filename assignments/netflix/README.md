**Objective**
Write a Python script that:

* Reads a CSV file of Netflix data using pandas
* Creates a new column `complete_director` with all the same values in the `director` column, except missing directors are replaced with the string "Unknown"
* Creates a new column `complete_cast` with all the same values in the `cast` column, except missing cast are replaced with the string "Unknown"
* Exports a new CSV file containing only the `title`, `complete_cast`, and the `complete_director` columns, using `import csv` and `csv.writer`.

---

**Requirements**

1. **Read the data**

   * Use `pandas.read_csv()` to load a file named `netflix.csv`.
   * You only need to work with the columns `title` and `director`.

2. **Define a function**

   * Create a function `is_missing(value)` that:

     * Returns `"Unknown"` if `value` is missing (use `pd.isna(value)`)
     * Otherwise returns the original `value`

3. **Apply the function**

   * Use `.apply()` to create a new column `complete_director` from `director`
   * Use `.apply()` to create a new column `complete_cast` from `cast`
   * The new column should replace any missing values with `"Unknown"`

4. **Write the output CSV**

   * Use `import csv` and `csv.writer` to write to a file named `result.csv`
   * Loop over the original csv and only copy over rows that have type `TV Show`
   * Include only these columns in the output:

     1. `title`
     2. `director` (which has the content of `complete_director`)
     3. `cast` (which has the content of `complete_cast`)


## Term‑Frequency Over Time

You are given a dataset of 1,712 text files (found in `transcriptions/`), all of which are examples church law in the Middle Ages. Your goal is to explore regional and chronological variations in topics, as well as the distribution of certain rhetorical forms (i.e. what sorts of topics tend to be accompanied by 'authority references', e.g. 'by authority of the Pope' or 'pursuant to such-and-such codified legal text....'). In this assignment, you will begin this exploration by analyzing the frequency of any given term over the decades.

Specifically, you’ll write a Python program that:

* Prompts the user for a search term
* Scans every .txt file in transcriptions/
* Counts how often the term appears (case-insensitive) per file
* Groups counts by decade
* Plots a line graph showing term usage over time

---

### Setup

1. Create a new file called `main.py` in this folder (outside of `transcriptions/`).

2. At the top of `main.py`, add:

   ```python
   import os
   import matplotlib.pyplot as plt
   ```

3. Define your `main()` function and call it:

   ```python
   def main():
       pass  # you will fill this in

   if __name__ == '__main__':
       main()
   ```

---

### Milestone 1: Prompt & Count

1. Inside `main()`, use `input()` to ask the user for a **search term**.
2. Initialize an empty dictionary called `counts_per_decade` that will store the count of the term for each decade
3. Loop through all files in the `transcriptions/` folder using `os.listdir()`.
4. Skip any file whose name contains `"Notes"`.
5. For each remaining file, extract the year from the filename, and then determine the corresponding decade. Suggestions:

   * Split the filename on `_` and take the last part (remove `.txt`)
   * If it ends with an extra character (like `a` or `c`), strip it off
   * Convert it to an integer
   * Compute the decade with `int(year / 10) * 10`
6. Open the file, read its text, and count occurrences of the search term. Suggestions:

    * use `open(filename, encoding='latin_1', errors='ignore')` to read the latin text
    * define a helper function `count_term_in_text(text, term)` that takes in the latin text and the term, and counts the occurrences of the term in the text. In our solution, we use the functions `.lower()`, `.isalpha()`, and `.split()` to clean the text.
7. Update your dictionary by incrementing the count for the decade.

Once this milestone works, print out the `counts_per_decade` dictionary to verify it.

Example output:
```
Enter the term to search for: Concilio
{1360: 69, 1410: 6, 1320: 100, 1340: 68, 1230: 43, 1400: 2, 1280: 143, 1350: 35, 1210: 45, 1290: 79, 1270: 85, 1330: 143, 1310: 184, 1370: 63, 1480: 1, 1260: 54, 1240: 58, 1200: 3, 1440: 1, 1250: 94, 1490: 5, 1460: 2, 1220: 58, 1300: 74, 1380: 9, 1420: 25, 1390: 23, 1430: 7, 1470: 24, 1450: 1, 1180: 2, 1520: 0, 1190: 6}
```

---

### Milestone 2: Plot the Results

1. After processing all files, build two lists:

   * `decades` — sorted list of decades
   * `counts` — corresponding counts in the same order
2. Create a line plot using Matplotlib:

   * Label the x-axis **“Decade”** and the y-axis **“Num Occurrences”**
   * Title the plot: `Occurrences of '<term>' Over Time`, where `<term>` is the user input
   * Optional: Use a marker, line style, and color of your choice for your plot.
3. Display the plot with `plt.show()`.

Run your code, enter a search term, and observe how its frequency changes across decades.

---

### 💡 Extension Ideas (Optional)

* **Normalize**: Divide each term count by the total words in the file to compute frequency per file.
* **Multiple terms**: Extend your code to plot multiple terms on the same graph, so that the user can compare the trends.
* **Get creative!**: Get creative with your data analysis! What research questions regarding this data do find interesting, and how might you be able to visualize the result?

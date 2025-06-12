## Federalist Papers: Who wrote it?!

This assignment uses probability and text analysis to guess which author—**Hamilton** or **Madison**—is more likely to have written an unknown document, based on word frequency.

If you're curious about the **math and historical background** behind this, visit [this link](https://probabilityforcs.firebaseapp.com/book/federalist)!

---

### How it works (High-level Overview)

1. For each known author, you will build a **word probability model** based on their texts.
2. You'll **count how many times each word** appears in the unknown document.
3. Using these counts and the word probabilities from each author, you’ll compute the **log probability** that the document came from each author.
4. The author with the higher probability is the more likely writer.

---

## Your Task

Implement the following functions to complete each missing piece of the program. You’ll be filling in the `TO DO` parts of the code.

---

### `standardize(word)`

**Goal:** Convert a word into a "standardized" form for analysis.

**What to do:**

* Convert the word to **lowercase**.
* **Remove all non-letter characters** (e.g., punctuation, digits, symbols).
* Remove any extra **spaces** or newline characters.

**Example behavior:**

```python
standardize("Democracy!")   → "democracy"
standardize("  LiBeRtY?")   → "liberty"
standardize("123freedom")   → "freedom"
standardize("...THE...")    → "the"
```

**Hint:** Use string methods like `.lower()` and `isalpha()`.

---

### `get_new_words(fileName)`

**Goal:** Count the **total number of words** in the file (after standardizing).

**What to do:**

* Open the file.
* For each line, split it into words.
* For each word, standardize it using the `standardize()` function.
* Count all valid (non-empty) standardized words.

**Return:** An `int` representing the total word count.

---

### `add_word_to_count_map(wordMap, word)`

**Goal:** Update the count for a given word in the dictionary.

**What to do:**

* If the word already exists in the dictionary, increment its count.
* If the word is new, add it to the dictionary with a count of `1`.

---

### `make_word_count_map(fileName)`

**Goal:** Build and return a **dictionary mapping words to their frequency** in the file.

**What to do:**

* Open the file.
* Read each line and split it into words.
* For each word:

  * Standardize it.
  * If the standardized word isn’t empty, use `add_word_to_count_map()` to record it.

**Return:** A dictionary: `{word: count}`

---

Read through the other functions that are in the starter code, including the main function. You do not need to edit this, but reason through what they are doing and how your code is using them.

### Final Check

After filling in the four missing functions, run the program. You should see:

* Word probabilities for `congress`
* Word counts from the unknown file
* Log probabilities for each author
* The difference in log-likelihood - used to decide who the likely author is!

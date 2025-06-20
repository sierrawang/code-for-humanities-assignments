# Historical Figure

In this assignment, you will complete a Python class called `HistoricalFigure` that represents a person from history. This class stores the figure’s name, area of influence, important contributions, and a famous quote.

---

## What You Need to Do

You will complete the file `historical_figure.py`. A class has already been started for you, and you need to fill in the missing pieces.

### Step 1: Complete the `__init__` method

The constructor should store four pieces of information:

* `name`: the full name of the historical figure (a string)
* `field`: their area of influence (like "science", "literature", or "civil rights")
* `quote`: a famous quote (a string)
* `contributions`: start with an empty list; you will add to this later

### Step 2: Fill in the class methods

Complete the following methods:

* `add_contribution(self, new_contribution)`
  This method should add a new contribution (a string) to the `contributions` list.

* `get_summary(self)`
  This method should return a string that looks like:
  `"Ada Lovelace was a key figure in science. Known for: ['Wrote the first algorithm', 'Worked with Charles Babbage']."`

* `share_quote(self)`
  This method should return a string in this format:
  `"Ada Lovelace once said: 'That brain of mine is something more than merely mortal, as time will show.'"`

---

## How to Test Your Work

A file called `test.py` is provided for you. You do not need to change this file.

When you run it, it will:

* Create several historical figures
* Add contributions
* Check if your methods return the correct values

If everything is working, it will print:

```
All tests passed!
```

If something is not working, it will show an error message telling you what to fix.

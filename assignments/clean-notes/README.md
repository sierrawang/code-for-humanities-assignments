## Clean Up a Messy Text File

### Task

Write a Python program that **cleans up a text file** by removing unnecessary whitespace and blank lines. The goal is to extract and print only the meaningful content, neatly formatted. You are given a file named `messy_text.txt` which contains meaningful text along with extra spaces, tabs, and empty lines. Your task is to:

* Read the file line by line.
* Remove all leading/trailing whitespace from each line.
* Ignore lines that are empty after stripping.
* Print each cleaned line.

### 🔍 Example

Given this input file `messy_text.txt`:

```
    
    The Federalist Papers are a collection of 85 articles and essays written by Alexander Hamilton, James Madison, and John Jay.

	These papers were published under the pseudonym "Publius" to promote the ratification of the United States Constitution.


Each essay addresses specific issues related to the Constitution and the need for a strong federal government.
  
  	  The Federalist Papers remain a key resource for understanding the intentions of the Founding Fathers.
```

Your program should print:

```
The Federalist Papers are a collection of 85 articles and essays written by Alexander Hamilton, James Madison, and John Jay.
These papers were published under the pseudonym "Publius" to promote the ratification of the United States Constitution.
Each essay addresses specific issues related to the Constitution and the need for a strong federal government.
The Federalist Papers remain a key resource for understanding the intentions of the Founding Fathers.
```


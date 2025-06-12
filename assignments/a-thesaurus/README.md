# A Thesaurus
In this folder you have a file called `a.json` that contains a dictionary object with the structure:

```
{
    ,,,
     "ACCEPT": [
        "Take",
        "Swallow",
        "Accept"
    ],
    "ACCEPTABILITY": [
        "Acceptability",
        "Acceptableness"
    ],
    "ACCEPTABILITIES": [
        "Acceptability",
        "Acceptableness"
    ],
    "ACCEPTABLE": [
        "Satisfactory",
        "Acceptable"
    ],
    ,,,
}
```

Such that each key is a word where the value is a list of up to 3 Synonyms. Note that all of the words in the dictionary start with the letter "A" (and are all uppercase). 

Your task is to read in the `a.json` file, convert it to JSON, then allow the user to query your program for synonyms of a word that starts with the letter "A". If a word does not exist in the thesaurus, output a message saying that no synonyms were found.
A sample run of your program should look like this:

```
Enter a word to find synonyms: apple
Synonyms for 'APPLE': Malus pumila, Orchard apple tree, Apple
Enter another word to find synonyms (or press Enter to exit): alley
Synonyms for 'ALLEY': Alleyway, Bowling alley, Alley
Enter another word to find synonyms (or press Enter to exit): age
Synonyms for 'AGE': Maturate, Geezerhood, Mature
Enter another word to find synonyms (or press Enter to exit): grape
No synonyms found for 'GRAPE'
Enter another word to find synonyms (or press Enter to exit): 
```


## Optional Extension
If a word is not found in the thesaurus, allow the user to add a new word and its synonyms. Make sure to write the file with the new word and synonyms back to `a.json` so that it is saved for future runs of the program.

```
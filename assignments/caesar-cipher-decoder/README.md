# Caesar Cipher (decoder)
In this program you will attempt to decrypt a message that has been encrypted with a Caesar cipher. You will not be given the shift value. Instead, you will be given the five most common letters in the English language. Then, you must count the frequency of each letter in the encrypted message. Using the character counts, compare the most frequent encrypted letters to the most common letters in the English language.

From those comparisons, find 5 potential shift values, and print out the resultant decryption for each of them.

Important!
In order to get the index of a letter in the alphabet, you can use the `ALPHABET` string provided:
```python
index_of_c = ALPHABET.index('c')
```
Or, you can use Python's built-in `ord` function:
```python
index = ord(letter) - ord('a')
```


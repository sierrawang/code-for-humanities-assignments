## Count the Word "Like"

### Task

Write a Python program that **counts how many times each student says the word "like"** in a storytelling log.

You're given a file called `weekend_stories.txt`, where each line contains a student's name followed by a colon and their description of what they did over the weekend. Your task is to:

* Read the file line by line.
* For each student, count how many times the word `"like"` appears in their story.
* Print the count in a formatted message.

> The word `"like"` may appear with commas or periods (e.g., `"like,"` or `"like."`), so be sure your check accounts for that!

### Expected Output

Given the following `weekend_stories.txt` file:

```
Alice: So, like, I went to the Dish on Saturday morning, and it was, like, so beautiful. I, like, ran the whole trail and, like, felt amazing...
Bob: I went surfing in Santa Cruz, and it was, like, totally awesome...
Charlie: I went to, like, a concert in SF, and it was, like, the best, like, night ever...
Dana: I went to see Stanford play Cal in water polo, and it was, like, such an intense game...
```

Your program should output:

```
Alice said 'like' 8 times.
Bob said 'like' 8 times.
Charlie said 'like' 10 times.
Dana said 'like' 7 times.
```
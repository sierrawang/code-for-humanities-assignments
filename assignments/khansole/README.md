# Khansole Academy
In Code in Place we are all about building technology to help folks learn. Now it is your turn. Implement Khansole Academy—a program that helps other people learn addition! Write a program that randomly generates a simple addition problem for the user, reads in the answer from the user, and then checks to see if they got it right or wrong.



More specifically, your program should be able to generate simple addition problems that involve adding two 2-digit integers (i.e., the numbers 10 through 99). The user should be asked for an answer to the generated problem. Your program should determine if the answer was correct or not, and give the user an appropriate message to let them know.

A sample run of the program is shown below (user input comes right after "Your answer: "):
```
Khansole Academy
What is 51 + 79?
Your answer: 120
Incorrect.
The expected answer is 130
```

Here's another sample run, where the user gets the question correct:
```
Khansole Academy
What is 55 + 11?
Your answer: 66
Correct!
```

When you have decided that your program works as intended, hit Check Correct.


## Optional Extension

Note: To avoid the assignment being marked incorrect because you did an extension, leave the base assignment solution in this project. To do your extension, make your own project under "Code > Your Own". If you get something cool working, share it on the forum!!

If you're up for it, we can make Khansole Academy an even better learning tool. Be creative! We recommend you start with the "three in a row" extension first, then come up with your own :-).

Three in a row

In the previous milestone you wrote code to randomly generate one addition problem at a time and tell the user if they got it right or not. In this milestone, you should randomly generate addition problems until the user has gotten 3 problems correct in a row. (Note: the number of problems the user needs to get correctly in a row to complete the program is just one example of a good place to specify a constant in your program).

You should be able to use a lot of your code from the previous milestone to help out here!

A sample run of the program is shown below (user input is in blue).

```
Khansole Academy
What is 51 + 79? 
Your answer: 120 
Incorrect. 
The expected answer is 130 

What is 33 + 19? 
Your answer: 42 
Incorrect. 
The expected answer is 52 

What is 55 + 11? 
Your answer: 66 
Correct! 
You've gotten 1 correct in a row. 

What is 84 + 25? 
Your answer: 109 
Correct! 
You've gotten 2 correct in a row. 

What is 26 + 58? 
Your answer: 74 
Incorrect. 
The expected answer is 84 

What is 98 + 85? 
Your answer: 183 
Correct! 
You've gotten 1 correct in a row. 

What is 79 + 66? 
Your answer: 145 
Correct! 
You've gotten 2 correct in a row. 

What is 97 + 20? 
Your answer: 117 
Correct! 
You've gotten 3 correct in a row. 

Congratulations! You mastered addition.
```
Douglas Hofstadter’s Pulitzer-prize-winning book Gödel, Escher, Bach contains many interesting mathematical puzzles, many of which can be expressed in the form of computer programs. In Chapter XII, Hofstadter mentions a wonderful problem:
Pick some positive integer and call it n.
If n is even, divide it by two.
If n is odd, multiply it by three and add one.
Continue this process until n is equal to one.

```
Enter a number: 15
15 is odd, so I make 3n + 1: 46 
46 is even, so I take half: 23
23 is odd, so I make 3n + 1: 70
70 is even, so I take half: 35 
35 is odd, so I make 3n + 1: 106 
106 is even, so I take half: 53 
53 is odd, so I make 3n + 1: 160 
160 is even, so I take half: 80
80 is even, so I take half: 40 
40 is even, so I take half: 20 
20 is even, so I take half: 10 
10 is even, so I take half: 5
5 is odd, so I make 3n + 1: 16 
16 is even, so I take half: 8 
8 is even, so I take half: 4
4 is even, so I take half: 2
2 is even, so I take half: 1
```

As you can see from this example, the numbers go up and down, but eventually—at
least for all numbers that have ever been tried—comes down to end in 1. In some
respects, this process is reminiscent of the formation of hailstones, which get carried
upward by the winds over and over again before they finally descend to the ground.
Because of this analogy, this sequence of numbers is usually called the Hailstone
sequence, although it goes by many other names as well.

You can check if a number is even or odd using the % operator. The % operator takes the left side and divides by the right and evaluates to the integers remaining. For example 5 % 2 would return 1 since 5 divides into 2 twice, with 1 left over (remaining). Read more in the Advanced Arithmetic Chapter of the Python Reader.

Here is an example where we check if a user entered an odd number:
```
my_num = int(input("Enter a num: "))
# What is the remainder when my_num is divided by 2?
# If the remainder is 1, then the number was odd.
remainder = my_num % 2
if remainder == 1:
    print("Your number is odd")
else:
    print("Your number is even")
```

Write a console program that reads in a number from the user and then displays the Hailstone sequence for that number, just as in Hofstadter’s book, followed by a line showing the number of steps taken to reach 1.

To get the autograder to pass, you will need to print out each value as an integer. However, when you use division by 2, python will change your numbers to floats. You can fix that by casting your values back to an integer:
```
three_float = 3.0
three_int = int(three_float)
```

The fascinating thing about this problem is that no one has yet been able to prove that it always stops. This problem (often refered to in math as the Collatz Conjecture) is one of the most famous unsolved problems in math. The number of steps in the process can certainly get very large. How many steps, for example, does your program take when n is 27? 
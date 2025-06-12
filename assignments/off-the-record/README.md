## Extract “On the Record” Interview Content

### Task

Write a Python program that **extracts only the "on the record" parts of an interview transcript**.

You're given a transcript file named `interview_transcript.txt`, which contains sections labeled either:

* `ON THE RECORD` — lines that can be publicly quoted
* `OFF THE RECORD` — lines meant to be excluded from public viewing

Your job is to:

* Read the file line by line.
* Identify and print **only** the lines that fall **within ON THE RECORD sections**.
* Skip any lines that appear in OFF THE RECORD sections.

> Note: The markers `ON THE RECORD` and `OFF THE RECORD` appear on their own lines and may repeat throughout the file.

### Expected Output

Given this input file:

```
ON THE RECORD
Interviewer: Thank you for joining us today. How do you feel about the current state of the dining halls at Stanford?

President Levin: I think the dining halls are doing a fantastic job. The variety and quality of food have improved significantly.

OFF THE RECORD
President Levin: Between you and me, I think the new chef at Wilbur is a bit overrated. But don't quote me on that!

ON THE RECORD
Interviewer: That's great to hear! Are there any new initiatives planned for the dining services?

President Levin: Yes, we're planning to introduce more sustainable food options and expand our plant-based offerings.

OFF THE RECORD
President Levin: Honestly, I wish we could just get rid of those long lines at lunchtime. It's a nightmare!

ON THE RECORD
Interviewer: Thank you for your time. We look forward to seeing these changes implemented.
```

Your program should print:

```
Interviewer: Thank you for joining us today. How do you feel about the current state of the dining halls at Stanford?
President Levin: I think the dining halls are doing a fantastic job. The variety and quality of food have improved significantly.
Interviewer: That's great to hear! Are there any new initiatives planned for the dining services?
President Levin: Yes, we're planning to introduce more sustainable food options and expand our plant-based offerings.
Interviewer: Thank you for your time. We look forward to seeing these changes implemented.
```

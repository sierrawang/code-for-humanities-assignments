In this program you will be implementing a digital phonebook application. 
The user should have 3 possible actions:
1. Add a new contact with a name and phone number.
2. Search for a contact by name and print the phone number.
3. List all contacts in the phonebook.
Which they should select by entering the numbers "1", "2", or "3" respectively.

The program should continue to prompt the user for an action until they enter an option that is different from all of the above (or enter an empty string).
A potential output of the program could look like this:

```
To add a contact, type '1'
To look up a contact, type '2'
To see all contacts, type '3'
Enter your choice (1, 2, or 3): 1
Enter the contact's name: TJ
Enter the contact's phone number: 555-555-1000
Contact TJ added with phone number 555-555-1000.
Enter your choice (1, 2, or 3): 1
Enter the contact's name: Sierra
Enter the contact's phone number: 555-415-9999
Contact Sierra added with phone number 555-415-9999.
Enter your choice (1, 2, or 3): 2
Enter the contact's name to look up: TJ
TJ's phone number is 555-555-1000.
Enter your choice (1, 2, or 3): 3
Contacts in the phonebook:
TJ: 555-555-1000
Sierra: 555-415-9999
Enter your choice (1, 2, or 3): 
Closing phonebook.
```
def main():
    # Initialize an empty phonebook
    phonebook = {}

    # Prompt the user
    print("To add a contact, type '1'")
    print("To look up a contact, type '2'")
    print("To see all contacts, type '3'")
    choice = input("Enter your choice (1, 2, or 3): ")


    # Loop until the user does not enter a 1, 2, or 3
    while True:
        if choice == '1':
            # Add a new contact!
            name = input("Enter the contact's name: ")
            phone_number = input("Enter the contact's phone number: ")
            phonebook[name] = phone_number
            print(f"Contact {name} added with phone number {phone_number}.")
        elif choice == '2':
            # Perform a lookup!
            name = input("Enter the contact's name to look up: ")
            if name in phonebook:
                print(f"{name}'s phone number is {phonebook[name]}.")
            else:
                print(f"Contact {name} was not found.")
        elif choice == '3':
            # List out the contacts
            print("Contacts in the phonebook:")
            for name in phonebook.keys():
                print(f"{name}: {phonebook[name]}")
        else:
            # The user has ended the program.
            print("Closing phonebook.")
            break

        choice = input("Enter your choice (1, 2, or 3): ")


if __name__ == '__main__':
    main()

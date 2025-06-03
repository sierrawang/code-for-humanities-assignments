from ai import call_gpt

def main():
    # Initialize the user response to be nothing
    user_response = ""

    while user_response != "no":
        # Get the next user query
        query = input("Query: ")

        # Get a response from GPT
        response = call_gpt(query)

        # Display the response to the user
        print(f"Response: {response}")
        
        # Ask the user whether they would like to continue
        user_response = input("Would you like to continue? (yes/no) ")
        print()

if __name__ == '__main__':
    main()
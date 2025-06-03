from youtube_helper import get_youtube_link

def main():
    # Get the user's input
    user_response = input("What would you like to search on youtube? ")

    # Construct a link for the user
    link = get_youtube_link(user_response)

    # Output the result to the user
    print(f"Here is your youtube link: {link}")

if __name__ == "__main__":
    main()
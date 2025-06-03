from ai import call_gpt
from youtube_helper import get_youtube_link

def main():
    # Get the user's input
    genre = input("Enter a music genre: ")
    mood = input("Enter your mood: ")
    decade = input("Enter a decade for your song to be from: ")
    print("Finding a song for you...")
    print()

    # Use GPT to choose a song
    gpt_response = call_gpt(f"Name a song with the genre {genre} and mood {mood} from the decade {decade}. Return only the song name and artist.")
    link = get_youtube_link(gpt_response)

    # Output the result to the user
    print(f"Try listening to: {gpt_response}")
    print(f"Youtube link: {link}")

if __name__ == "__main__":
    main()
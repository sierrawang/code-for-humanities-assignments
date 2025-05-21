from ai import call_gpt
from youtube import search_youtube

def main():
    # Get the user's input
    genre = input("Enter a music genre: ")
    mood = input("Enter your mood: ")
    decade = input("Enter a decade for your song to be from: ")
    print("Finding a song for you...")
    print()

    # Use GPT to choose a song
    song = call_gpt(f"Name a song with the genre {genre} and mood {mood} from the decade {decade}. Return only the song name and artist.")
    link = search_youtube(song)
    print(f"Try listening to: {song}")
    print(f"Youtube link: {link}")

if __name__ == "__main__":
    main()
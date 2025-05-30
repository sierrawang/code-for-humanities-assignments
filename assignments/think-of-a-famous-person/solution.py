from ai import call_gpt
import random

n_questions = 20
correct_response = "Great job! 🌱"

def main():
    person = get_person()
    print("I am thinking of a person.")
    print("Can you guess what person it is?")

def get_person():
    person = [
        "George Washington", "Napoleon Bonaparte", "Ada Lovelace", "Alexander the Great", "William Shakespeare",
        "Cleopatra VII", "Marie Curie", "Frida Kahlo", "Harriet Tubman", "John Stuart Mill", "Taylor Swift",
        "Caitlin Clark", "Serena Williams", "Babe Ruth", "Katherine Johnson", "Margaret Thatcher", "Julius Caeser",
        "Lionel Messi", "Galileo Galilei", "Jane Goodall", "Vincent van Gogh", "Albert Einstein", "Nicolaus Copernicus"
    ]
    return random.choice(person)



def get_prompt(question, person):
    return f"""You are a helpful assistant playing a game of 20 questions where the user is trying to think of an animal. 
You will be given a yes or no question.
If the users question shows they have the answer (for example if they ask, "is it a {person}") then they have won and you must respond with the exact string "{correct_response}".
Otherwise, answer the question in a way that is honest for the animal and try to just answer in "yes" or "no" unless your answer needs a qualifier.
If the user ever directly asks for a hint, you can give one to them.

The : {person}.
The question: {question}.
    """

if __name__ == "__main__":
    main()
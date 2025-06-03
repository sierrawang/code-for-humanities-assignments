from famous_people import FAMOUS_PEOPLE
from ai import call_gpt
import random

CORRECT_MESSAGE = "Correct!"

def get_person():
    return random.choice(FAMOUS_PEOPLE)

def main():
    person = get_person()
    print("I am thinking of a person.")
    print("Can you guess what person it is?")

    gpt_response = ""
    while gpt_response != CORRECT_MESSAGE:
        # Prompt the user to ask a question
        question = input("Ask me a yes or no question: ")

        # Construct a prompt
        prompt = f"""You are a helpful assistant playing a game of 20 questions where the user is trying to think of a person. 
You will be given a yes or no question.
If the users question shows they have the answer (for example if they ask, "is it {person}") then they have won and you must respond with the exact string "{CORRECT_MESSAGE}".
Otherwise, answer the question in a way that is honest for the person and try to just answer in "yes" or "no" unless your answer needs a qualifier.
If the user ever directly asks for a hint, you can give one to them.

The person: {person}.
The question: {question}.
    """
        
        # Get a response from GPT
        gpt_response = call_gpt(prompt)

        # Output the response to the user
        print(gpt_response)

if __name__ == "__main__":
    main()
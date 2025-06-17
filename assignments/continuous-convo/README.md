## Build a Chatbot with GPT

In this assignment, you'll build a simple chatbot that uses OpenAI's API to hold a back-and-forth conversation with a user. The chatbot will remember everything said in the conversation and use that memory to generate appropriate responses.

By the end of the assignment, you will have a functional command-line chatbot that feels responsive, interactive, and context-aware.

---

### Instructions

#### 0. Setup

* Import the openai libary
* Define your main function

#### 1. Write a `get_next_message` function

Implement a function called `get_next_message(conversation)` that:

* Takes in the full conversation so far (as a list of message dictionaries),
* Sends the conversation to the GPT API,
* Returns the next message from the assistant.

Make sure to extract and return only the generated text (not the full response object).

#### 3. Implement the conversation loop

In your `main()` function:

* Create an empty list called `conversation` to store the full history.
* Ask the user for their first message and add it to the list with the role `"user"`.
* Use a loop to:

  * Send the full conversation to GPT using `get_next_message`
  * Print GPT’s reply
  * Add the GPT reply (role: `"assistant"`) and the user's next input (role: `"user"`) to the conversation
* Stop the loop when the user submits an empty input.

---

### Output Example

```
You: hi
AI: Hello! How can I assist you today?
You: im wondering what i just said
AI: You said "hi." It seems like a friendly greeting! Is there something specific you'd like to discuss or ask about?
You:
```

---

### Optional Extensions

* **Conversation Logging**: Save the full conversation to a text file so the user can refer back to it later.
* **Developer Prompt Customization**: Add an initial `"developer"` message to define your chatbot's personality (e.g., "You are a wise owl").
* **Token Counting**: Track how many tokens each message uses. You may want to truncate or trim older messages when the conversation gets long.
* **Multiple Chat Modes**: Allow the user to choose between chatbot "modes" like helpful assistant, trivia master, or sarcastic friend.

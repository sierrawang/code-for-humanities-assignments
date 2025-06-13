# Infinite Story

# See the full assignment description here:
http://nifty.stanford.edu/2025/piech-infinite-story/infinite_story_assn_handout.pdf

## Overview

You are exploring a world. Almost every scene is normal, but if the hero explores enough, they
will slowly start to uncover the mysterious parts…

In this assignment, you will write a choose-your-own-adventure adventure game that harnesses
the power of generative AI. You will get to apply the knowledge you have learned about
dictionaries and combine that with making requests to ChatGPT to ultimately help guide your
user through a mystical adventure. In the end, you will think about the ethical implications
underlying the use of generative AI in storytelling applications.

When the user starts the program it will look like this:
```
You are standing at the end of a road before a small brick building. A small stream flows out of the building and down a gully to the south. A road runs up a small hill to the west.
1. Take the road up the hill
2. Walk up to the stream
3. Knock on the door
What do you choose?
```

The user can then choose what action to take next. Here they chose 1, to take the road up the
hill:
```
You are standing at the end of a road before a small brick building. A small stream flows out of the building and down a gully to the south. A road runs up a small hill to the west.
1. Take the road up the hill
2. Walk up to the stream
3. Knock on the door
What do you choose? 1

As you walk up the hill, the landscape opens up before you. You can see a vast valley with lush greenery and winding rivers below. The sun is setting in the distance, casting a warm glow over the scene.
1. Descend into the valley
2. Continue exploring the hilltop
3. Follow the path towards the village in the distance
4. Return to the small brick building
What do you choose? 
```

Up to this point, it seems like a standard storytelling app. The magic happens when the user gets
to a scene that hasn't been written yet. Instead of crashing, or preventing the user from
continuing, the app will make a request to ChatGPT to generate the next scene. The story
continues!


## Milestone 1: Loading the Story
A key limitation for any story of this nature is that you will eventually hit a dead end. Program
`warmup.py` to find the "dead ends" in a story. Dead ends are scene keys that are referenced in the
story, but are not defined.

In order to complete this warmup we need to first understand how story data is stored. The data
for a story is saved as a nested dictionary. We've created two story dictionaries for you,
`original_big.json` and `original_small.json`. These files are stored in a folder called data:

First, load in a story dictionary. Since each story is in json format you can load it with the
following line of code which should be at the start of your `main` function:

```python
story_data = ""
with open('data/original_small.json') as file:
    story_data = json.load(file)
```

You will routinely access this dictionary throughout your program. You should only load the file
once.

Before proceeding, take some time to understand how the data in story_data is organized. Here is
an excerpt of the story_data dictionary


```json
{
    "plot": "You are exploring a world. Almost every scene is normal, but if the hero explores
    enough of the normal parts (eg more than 10 scenes), they will slowly start to uncover the
    mysterious parts. Most of the tone is simply setting a beautiful and uplifting landscape
    filled with wonder.",
    "scenes": {
        "start": {
            "text": "You are standing at the end of a road before a small brick building. A small
            stream flows out of the building and down a gully to the south. A road runs up a small hill to
            the west.",
            "scene_summary": "Start of the story. Standing in front of a brick building.",
            "choices": [
                {
                "text": "Take the road up the hill",
                "scene_key": "overlooking_valley"
                },
                {
                "text": "Walk up to the stream",
                "scene_key": "next_to_gully"
                },
                {
                "text": "Knock on the door",
                "scene_key": "knocking_on_small_brick_building"
                }
            ]
        },
        "knocking_on_small_brick_building": {
            "text": "You knock on the door, but no one answers. You hear a faint sound of a dog
            barking from inside.",
            "scene_summary": "Nobody answers.",
            "choices": [
                {
                "text": "Go back to the start",
                "scene_key": "start"
                }
            ]
        },
    ... # more scenes, hidden for space
}
```

Wow! A truly nested dictionary. Don't be intimidated by it. Instead, understand it step by step.

Story: Every story is a dictionary with two keys: a key "plot" that is associated with a string
description of the overall story line, and a key "scenes" that is associated with a dictionary
containing all the data of the scenes in the story (see Scenes below).

Scenes: A dictionary with all the scene data. In the scenes dictionary scene keys are associated
with all the data for that given scene. Each scene has a "text" description, a "scene_summary"
and a list of choices that the user can take from the scene (see Choices below). Here is
scene_data associated with the scene key "knocking_on_small_brick_building". It only has one
choice: 

```json
    {
        "text": "You knock on the door, but no one answers. You hear a faint sound of a dog barking
        from inside.",
        "scene_summary": "Nobody answers.",
        "choices": [
            {
            "text": "Go back to the start",
            "scene_key": "start"
            }
        ]
    }
```


Choice: A choice has both the "text" of the choice and the "scene_key" that the hero will go to if
they take this choice.

Now that you have the story_data loaded, it is time to program `warmup.py` to find "dead ends":
    • Loop over all the scenes in the story.
    • For each scene, loop over all the choices for that scene.
    • Each choice has a value associated with the key "scene_key".
    • If the scene_key is not a key in story_data["scenes"], then it is a dead end. Print out
    scene_key

For example if you ran `warmup.py` with the story constant set to "original_small.json" file it
should print out the following keys:
next_to_gully
descend_into_valley
watching_sunset
continue_exploring_hilltop
return_to_small_brick_building

We print out `descent_into_valley` because it is referenced by a choice, but it is not in the
scenes dictionary (it is a dead end). We do not print out `knocking_on_small_brick_building`
as it is a key in the scenes dictionary. Recall that for this milestone you should write your code in
`warmup.py`. Test your code on both original_small and original_big. The order of dead ends does
not matter. 

You can also try these optional challenges. Can you print out these values using story_data:
• The "plot" of the story?
• The "text" description of the scene with key "start"?
• The "scene_key" you would go to if you took the first choice from the "start" scene (the
choice that has text "Take the road up the hill")?

## Milestone 2: Printing a Scene to the Console 
Write a function to print a single scene to the console. It should only take one parameter, the
dictionary associated with that scene. Write your code in `infinite_story.py`. In this new
program you should load the story_data json in the same way as in Milestone 1. You can test
your code on either the big or small story data. We recommend that at this point you start
working with `original_big`

Your function should print out the "text" for the scene as well as the "text" for each choice
associated with the "choices" key in the scene data. Choices should be numbered for the user,
starting at 1. For example, if you called the function with the data for the "start" scene, it should
print out the following:

```
You are standing at the end of a road before a small brick building. A small stream flows out of
the building and down a gully to the south. A road runs up a small hill to the west.
1. Take the road up the hill
2. Walk up to the stream
3. Knock on the door
```


Recall that what the scene dictionrary looks like. (See the example above.)

Observe that every scene has a description ("text") as well as a list of next scene options that the
user can choose from ("choices"). Notice that choices is a list and that each element in the list is
a dictionary of its own. The "text" key in each inner dictionary is the text description for the
choice.

Your function should work for any scene, not just the start. Note, that you do not need to use the
"scene_summary" key, that will come in handy later.

## Milestone 3: Getting a Valid Choice from the User
Write a function to get a valid choice from the user. This function should also only take in one
parameter, the data dictionary of a scene. It should return the choice the user made.

After you print a scene to the console, including the choices, you will need to get a valid choice
from the user. In this milestone you will write the function that gets that information from the
user.

Ask the user what they choose, with input prompt "What do you choose? ". Their response
needs to be one of the integers that corresponds to a printed choice for the scene. Until the choice
is valid, print out "Please enter a valid choice: " and then re-prompt the user to enter a
valid choice. When you get a valid choice, return the choice made.

Here is an example, where we call the get valid choice function for the "start" scene. Note that
the scene has already been printed using the function from the previous milestone. User input is
in blue italics. The user enters two invalid choices, before they eventually enter a valid choice, `1`,
which corresponds to the text "Take the road up the hill"

```
You are standing at the end of a road before a small brick building. A small stream flows out of
the building and down a gully to the south. A road runs up a small hill to the west.
1. Take the road up the hill
2. Walk up to the stream
3. Knock on the door
What do you choose? cat
Please enter a valid choice: 5
Please enter a valid choice: 1
```

Pro Tip: Python lists are 0-indexed, but our choices are indexed starting at 1! How might you
take care of this?

Now that you have functionality to print out a scene, and get a valid choice for a scene, it is time
to stitch our story app together! In main(), your job is to infinitely run scenes by transitioning
from one scene to the next based on what the user inputs.

Pro Tip: You should have a variable which keeps track of the current scene key. The first scene
always has the scene key "start".

In an infinite loop you should:
1. get the scene data for the current scene
2. print the current scene
3. get a valid choice from the user
4. update the current scene key

Suggested: To make it easier for the user to read, print out an extra (blank) line to the console
before you print out a scene.

Woohoo! Look at your infinite story coming together! If you play for long enough, you will
eventually reach a scene_key which is not in your story. Your program will likely crash with an
error that says KeyError and complains that a scene key is not in your scenes dictionary. So
what do we do if we don't have a scene description?! We will resolve this issue in the next
milestone! :)


## Milestone 4: Handling Infinity

When we get to a scene key where we don't have scene data (i.e. the key does not exist in our
story_data dictionary, a dead end), we are not going to crash. Instead, we are going to call upon
ChatGPT for help in generating a new scene, including appropriate choices! Then, we will
continue our program with the newly created scene. For this milestone, define a function that
creates a new scene when the scene key doesn't exist in your story_data dictionary. Specifically
you should:
1. Print "[Suspenseful music plays as the story continues...]"
2. Construct a prompt to ask Chat GPT to generate the next scene
3. Add the scene into your story_data, so that if the story brings the hero back to the same
scene key, you display the same information.


The prompt should be formatted like this:
```python
f""""Return the next scene of a story for key  {scene key}. An example scene
should be formatted in json like this: {example scene}. The main plot line of
the story is {plot}."""
```

`scene_key` is the key of the scene to be generated. The plot should be the value associated with
"plot" in story_data. The example scene should be the start scene's data turned into a string. You
can cast a dictionary to a string, just like you can cast an integer to a string, using a command
like str(start_scene_data). It is important to give ChatGPT an example json so that it knows
what format you are expecting scenes to be in.

So how do we communicate with ChatGPT to generate our next scene when we do not already
have the data in our dictionary? To do this, we will first need to understand a new key concept:
APIs.

APIs (Application Programming Interfaces) allow software applications to communicate and
interact with each other. They define the methods and data formats that applications can use to
request and exchange information, allowing computer scientists to integrate various services,
such as ChatGPT, seamlessly into their own projects without a lot of added complexity. Think of
them as functions on a remote computer that you can call over the internet. They are a super
powerful tool!

See example_request.py for a full example of making an API "call" to OpenAI.
```python
chat_completion = CLIENT.chat.completions.create(
 messages=[{
 "role": "user",
 "content": """What is the capital of all countries in east africa?
 Reply in json where keys are countries""",
 }],
 model="gpt-3.5-turbo", # the GPT model to use
 response_format={"type": "json_object"} # we want our response in json format,
)
```


This is an example of an API "call", where we are sending a prompt to OpenAI's chat API
(client) to generate a response based on the prompt "What is the capital of all countries in east
africa? Reply in json where keys are countries". It also specifies that the input message is from
the user ("role": "user"), indicates the GPT model to be used ("gpt-3.5-turbo"), and specifies that
the response should be formatted as json (response_format={"type": "json_object"}).
In order for the call to work we need to first initialise the API client. Notice the line in your
program:
```python
CLIENT = NotOpenAI(api_key="yourapikey")
```
You are going to need to replace "yourapikey" with your own API Key. To get your API key see
the NotOpenAI handout. 
The chat_completion that you get back from the API call is a rather complicated object. To get
just the json response you can use the following two lines:
```python
# get the content of the response
response_str = chat_completion.choices[0].message.content
# turn the string into a dictionary using loads
new_scene_data = json.loads(response_str)
```

If ChatGPT has done its job, new_scene_data will now be a new dictionary for a scene,
complete with text, summary and choices. You can now add this new scene to your story_data
dictionary.

Then you can add that scene to your story_data dictionary, and keep the story going!

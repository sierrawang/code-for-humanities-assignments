# Infinite Story

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
story_data = json.load(open('data/original_small.json'))
```

You will routinely access this dictionary throughout your program. You should only load the file
once.

Before proceeding, take some time to understand how the data in story_data is organized. Here is
an excerpt of the story_data dictionary


```
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
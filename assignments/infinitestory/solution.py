import json
from openai import OpenAI


CLIENT = OpenAI()
STORY_NAME = "original_big"
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400



# This function loads the story from the JSON file
def open_story_file():
    with open(f"data/{STORY_NAME}.json", 'r') as file:
        story = json.load(file)
    return story


def print_scene_and_get_choice(scene_key, story):
    if scene_key in story["scenes"]:
        scene = story["scenes"][scene_key]
    else:
        scene = get_new_scene(scene_key, story)
        story["scenes"][scene_key] = scene

    choices = scene.get("choices", [])
    print(scene["text"])
    for i, choice in enumerate(scene["choices"]):
        print(f"{i + 1}. {choice['text']}")
    choice_index = int(input("What do you choose? ")) - 1
    return choices[choice_index]


def get_new_scene(scene_key, story):
    print("[Suspenseful music plays in the background]")
    chat_completion = CLIENT.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": f"""Return the next scene of a story for key {scene_key}. An example scene should be formatted in json like this: {story["scenes"]["start"]}. The main plot line of the story is {story["plot"]}."""
            }
        ],
        model="gpt-4o", # the GPT model to use
        response_format={"type": "json_object"} # we want our response in json format,
    )
    response_str = chat_completion.choices[0].message.content
    response = json.loads(response_str)
    return response



def main():
    print("Infinite Story")
    # TODO: your code here
    story = open_story_file()
    # print(story["plot"])
    choice = print_scene_and_get_choice("start", story)
    
    while True:
        print()
        next_scene_key = choice["scene_key"]
        choice = print_scene_and_get_choice(next_scene_key, story)




if __name__ == "__main__":
    main()

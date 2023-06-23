

import os
import openai

# openai.api_type = "azure"
# openai.api_version = "2023-05-15"
# openai.api_base = os.getenv("OPENAI_API_BASE")  # Your Azure OpenAI resource's endpoint value.

with open("api.txt", "r") as f:
    key = f.read()
openai.api_key = key


def send_request_gpt(content, system_role="You are a helpful assistant.", assistant=None):
    messages = [
        {"role": "system", "content": system_role},
        {"role": "user", "content": content}
    ]
    if assistant is not None:
        messages.append({"role": "assistant", "content": assistant})
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k",
        messages=messages
    )
    print(completion)
    print(completion.choices[0].message.content)
    return completion.choices[0].message.content

def send_request_dvc(content, assistant=None):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="I am a highly intelligent question answering bot. If you ask me a question that is rooted in truth, I will give you the answer. If you ask me a question that is nonsense, trickery, or has no clear answer, I will respond with \"Unknown\". Q:" +
               content,
        temperature=0,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=["\n"]
    )
    print(response)

def ask_poem(name, assistant=None):
    send_request_gpt(
        f"what is the original chinese content of 诗经 {name}, answer the poem only without title",
        system_role="You are a Chinese student being ask of existing information, your answer must be as correct as possible, no imaginary or creation and only answer what is asked, no additional content.",
    )


def translate_poem(name, assistant=None):
    send_request_gpt(
        f"translate the poem \'{name}\' to english, context only without title",
        assistant=assistant
    )

def image_scene(chinese, translate):
    context_origin = f"here is an ancient chinese poem: \n" + chinese
    context_translate = f"here is its translation: \n" + translate
    context_imagine = "use simple K-12 word to describe a scene for drawing relate to it around 30 words"
    return send_request_gpt(
        context_origin + "\n" + context_translate + "\n" + context_imagine,
        system_role="You are a creative and imaginary chinese artist",
    )

chinese = "桃之夭夭、灼灼其華。之子于歸、宜其家室。桃之夭夭、有蕡其實。之子于歸、宜其室家。桃之夭夭、其葉蓁蓁。之子于歸、宜其家人"
english = "The peach tree is young and elegant; Brilliant are its flowers. This young lady is going to her future home, And will order well her chamber and house. The peach tree is young and elegant; Abundant will be its fruits. This young lady is going to her future home, And will order well her chamber and house. The peach tree is young and elegant; Luxuriant are its leaves. This young lady is going to her future home, And will order well her family."

imaginary = image_scene(chinese, english)
imaginary = "shijng  a drawing of" + imaginary

print(imaginary)

# translate_poem("关睢", assistant=poem)z
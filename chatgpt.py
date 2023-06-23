# 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

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

imaginary = image_scene("關關雎鳩、在河之洲。窈宨淑女、君子好逑。參差荇菜、左右流之。窈宨淑女、寤寐求之。求之不得、寤寐思服。悠哉悠哉、輾轉反側。參差荇菜、左右采之。窈宨淑女、琴瑟友之。參差荇菜、左右芼之。窈宨淑女、 鍾鼓樂之。",
            "Guan-guan go the ospreys, On the islet in the river. The modest, retiring, virtuous, young lady, For our prince a good mate she." +
            "Here long, there short, is the duckweed, To the left, to the right, borne about by the current. The modest, retiring, virtuous, young lady, Waking and sleeping, he sought her." +
            "He sought her and found her not , And waking and sleeping he thought about her . Long he thought ; oh ! long and anxiously ; On his side , on his back , he turned , and back again ." +
            "Here long, there short, is the duckweed; On the left, on the right, we gather it.The modest, retiring, virtuous, young lady; With lutes, small and large, let us give her friendly welcome.")
imaginary = "shijng  a drawing of" + imaginary

print(imaginary)

# translate_poem("关睢", assistant=poem)z
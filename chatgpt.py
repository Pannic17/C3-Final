#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

import os
import openai
# openai.api_type = "azure"
# openai.api_version = "2023-05-15"
# openai.api_base = os.getenv("OPENAI_API_BASE")  # Your Azure OpenAI resource's endpoint value.

with open("api.txt", "r") as f:
    key = f.read()

openai.api_key = key

completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello!"}
  ]
)

print(completion.choices[0].message)

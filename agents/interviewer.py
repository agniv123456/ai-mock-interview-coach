#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from openai import OpenAI

client = OpenAI()

def ask_question(context):
    with open("prompts/interviewer.txt", "r") as f:
        system_prompt = f.read()

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": context}
    ]

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages
    )

    return response.choices[0].message.content


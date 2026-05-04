#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from openai import OpenAI

client = OpenAI()

def generate_feedback(history):
    with open("prompts/coach.txt", "r") as f:
        system_prompt = f.read()

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": str(history)}
        ]
    )

    return response.choices[0].message.content


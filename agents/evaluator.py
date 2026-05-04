#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from openai import OpenAI
import json

client = OpenAI()

def evaluate_answer(question, answer):
    with open("prompts/evaluator.txt", "r") as f:
        system_prompt = f.read()

    user_input = f"""
Question: {question}
Answer: {answer}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input}
        ]
    )

    text = response.choices[0].message.content

    try:
        return json.loads(text)
    except:
        print("JSON Error:", text)
        return {}


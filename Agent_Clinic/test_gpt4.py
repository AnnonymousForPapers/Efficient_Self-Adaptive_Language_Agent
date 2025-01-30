# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 02:10:57 2025

@author: xiaoyenche
"""

import openai
api_key = "sk-sbOm_ObkD09Tju5p5kNH_g6gw8FeDMzOffCXi9IXZET3BlbkFJZoPYD-k1svBv5DALaV_7dhFzn0-NlksFkAGlmjdycA"
openai.api_key = api_key

completion = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "Write a haiku about recursion in programming."
        }
    ]
)

print(completion.choices[0].message)
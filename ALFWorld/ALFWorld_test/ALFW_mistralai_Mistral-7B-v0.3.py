# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 13:25:01 2024

@author: xiaoyenche

disable use cach for limited memory space
"""

# import os
# import openai

# # openai.api_key = os.environ["OPENAI_API_KEY"]
# openai.api_key = "sk-proj-AG8M7U9zlBI5W5F9FCRfT3BlbkFJcEYuaroajIdau953QIK2"

# def llm(prompt, stop=["\n"]):
#     # response = openai.Completion.create(
#     response = openai.Completion.create(
#       model="gpt-3.5-turbo-instruct",
#       prompt=prompt,
#       temperature=0,
#       max_tokens=100,
#       top_p=1,
#       frequency_penalty=0.0,
#       presence_penalty=0.0,
#       stop=stop
#     )
#     # return response["choices"][0]["text"]
#     return response.choices[0].text

from transformers import AutoTokenizer, AutoModelForCausalLM
# import torch

model_name = "mistralai/Mistral-7B-v0.3"
print("\n" + "Model name: " + model_name + "\n")

access_token = "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"

tokenizer = AutoTokenizer.from_pretrained(model_name, token=access_token)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    device_map="auto",
    token=access_token
)

#%% ReAct 

import yaml
import alfworld
import alfworld.agents.environment
with open('base_config.yaml') as reader:
    config = yaml.safe_load(reader)

split = "eval_out_of_distribution"

env = getattr(alfworld.agents.environment, config["env"]["type"])(config, train_eval=split)
env = env.init_env(batch_size=1)

def process_ob(ob):
    if ob.startswith('You arrive at loc '):
        ob = ob[ob.find('. ')+2:]
    return ob

import json
folder = './prompts/'
prompt_file = 'alfworld_3prompts.json'
with open(folder + prompt_file, 'r') as f:
    d = json.load(f)
    
import sys

def alfworld_run(prompt, to_print=True, ob=''):
    init_prompt = prompt + ob + '\n>'
    prompt = ''
    if to_print:
        print(ob)
        sys.stdout.flush()
    for i in range(1, 50):
        # action = llm(init_prompt + prompt, stop=['\n']).strip()
        
        """Change here"""
        inputs = tokenizer(
        [
            init_prompt + prompt
        ], return_tensors = "pt").to("cuda")

        outputs = model.generate(**inputs, max_new_tokens = 400, use_cache = True, do_sample=False, top_p=1, repetition_penalty=0.0001,)
        action_1 = tokenizer.batch_decode(outputs)[0]
        if i == 1:
            print("\n\n-----1st LLM output start-----\n")
            print(action_1)
            print("\n-----1st LLM output end-----\n\n")
        # print("\n-----NLP output-----\n")
        # 1
        # initializing stop string
        action_1 = action_1.replace(r"\n", "\n")
        stop=init_prompt + prompt + " "
        # slicing off after length computation    
        if stop in action_1:
            action_2 = action_1.split(stop)[1]
            # print("\n-----True 1-----\n")
        else:
            action_2 = action_1
            # print("\n-----False 1-----\n")
        # 2
        # initializing stop string
        stop="\n"
        # slicing off after length computation       
        if stop in action_2:
            action_3 = action_2.split(stop)[0]
            # print("\n-----True 2-----\n")
        else:
            action_3 = action_2
            # print("\n-----False 2-----\n")
        action = action_3
        # print(action)
        # print("\n-----NLP output end-----\n\n")
        """Changes end"""
        
        # print("\n\n ******** \n action: " + str(action))
        observation, reward, done, info = env.step([action])
        observation, reward, done = process_ob(observation[0]), info['won'][0], done[0]
        if action.startswith('think:'):
            observation = 'OK.'
        if to_print:
            print(f'Act {i}: {action}\nObs {i}: {observation}')
            sys.stdout.flush()
        prompt += f' {action}\n{observation}\n>'
        if done:
            return reward
    return 0

prefixes = {
    'pick_and_place': 'put',
    'pick_clean_then_place': 'clean',
    'pick_heat_then_place': 'heat',
    'pick_cool_then_place': 'cool',
    'look_at_obj': 'examine',
    'pick_two_obj': 'puttwo'
}
cnts = [0] * 6
rs = [0] * 6

for _ in range(134):
    ob, info = env.reset()
    ob = '\n'.join(ob[0].split('\n\n')[1:])
    # print("\n\n ******** \n ob: " + str(ob) + "\n **************** \n end ob \n\n")
    name = '/'.join(info['extra.gamefile'][0].split('/')[-3:-1])
    print(name)
    for i, (k, v) in enumerate(prefixes.items()):
        if name.startswith(k):
            prompt = 'Interact with a household to solve a task. Here are two examples.\n' + d[f'react_{v}_1'] + d[f'react_{v}_0'] + '\nHere is the task.\n'
            print(k, v)
            r = alfworld_run(prompt, ob=ob)
            rs[i] += r
            cnts[i] += 1
            break
    print(_+1, 'r', r, 'rs', rs, 'cnts', cnts, 'sum(rs)/sum(cnts)', sum(rs) / sum(cnts))
    print('------------\n')
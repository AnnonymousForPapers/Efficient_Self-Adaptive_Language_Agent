# -*- coding: utf-8 -*-
"""
ref:
    https://winder.ai/calculating-token-counts-llm-context-windows-practical-guide/
    https://cookbook.openai.com/examples/how_to_count_tokens_with_tiktoken
    https://discuss.huggingface.co/t/tokenizer-decoding-using-bert-roberta-xlnet-gpt2/1128
"""

#%%
import json
folder = './prompts/'
prompt_file = 'alfworld_3prompts.json'
with open(folder + prompt_file, 'r') as f:
    d = json.load(f)

prefixes = {
    'pick_and_place': 'put',
    'pick_clean_then_place': 'clean',
    'pick_heat_then_place': 'heat',
    'pick_cool_then_place': 'cool',
    'look_at_obj': 'examine',
    'pick_two_obj': 'puttwo'
}
from transformers import AutoTokenizer, AutoModelForCausalLM

model_names = ['google/gemma-2-9b',
               'google/gemma-2-9b-it',
               'mistralai/Mistral-7B-v0.3',
               'mistralai/Mistral-7B-Instruct-v0.3',
               'meta-llama/Llama-2-7b-hf',
               'microsoft/Phi-3-medium-128k-instruct',
               'deepseek-ai/deepseek-llm-7b-base',
               'HuggingFaceH4/zephyr-7b-alpha']

access_token = ""

for j, m in enumerate(model_names):
    if j != 5:
        continue
    tokenizer = AutoTokenizer.from_pretrained(m, token=access_token)
    model = AutoModelForCausalLM.from_pretrained(
        m,
        device_map="auto",
        token=access_token
    )
    print("\nModel name: " + m + ", Max. context len.: " + str(model.config.max_position_embeddings))
    for i, (k, v) in enumerate(prefixes.items()):
        prompt = 'Interact with a household to solve a task. Here are two examples.\n' + d[f'react_{v}_1'] + d[f'react_{v}_0'] + '\nHere is the task.\n'
        result = tokenizer(prompt)
        input_ids = result['input_ids']
        # print("Token ids:" + str(input_ids))
        # print("Decode:" + str(tokenizer.decode(input_ids)))
        # print("Tokens:" + str(tokenizer.convert_ids_to_tokens(input_ids)))
        print("Model name: " + m + ", Task type: " + v + ", Context length:" + str(len(tokenizer.convert_ids_to_tokens(input_ids))))
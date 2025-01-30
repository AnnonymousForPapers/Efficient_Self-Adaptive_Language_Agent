# pip install accelerate
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

access_token = ""

tokenizer = AutoTokenizer.from_pretrained("google/gemma-2-9b-it")
model = AutoModelForCausalLM.from_pretrained(
    "google/gemma-2-9b-it",
    device_map="auto",
    torch_dtype=torch.bfloat16,
    token=access_token,
)

# messages = [
#     {"role": "user", "content": "Write me a poem about Machine Learning."},
# ]

# chat = [
#     {"role": "user", "content": "Hello, how are you?"},
# ]

# prompt = tokenizer.apply_chat_template(chat, tokenize=False, add_generation_prompt=True)

# print("prompt starts#########################")
# print(prompt)
# print("prompt ends#########################")
# inputs = tokenizer.encode(prompt, add_special_tokens=False, return_tensors="pt")
# print("input starts#########################")
# print(inputs)
# print("input ends#########################")
# outputs = model.generate(input_ids=inputs.to(model.device), max_new_tokens=150)
# print("output starts#########################")
# print(tokenizer.decode(outputs[0]))
# print("output ends#########################")
# print("processed output starts#########################")
# answer = tokenizer.decode(outputs[0, len(inputs):])
# import re
# answer = re.sub("\s+", " ", answer)
# print("processed ends#########################")

# input_ids = tokenizer.apply_chat_template(messages, return_tensors="pt", return_dict=True).to("cuda")

# outputs = model.generate(**input_ids, max_new_tokens=256, do_sample=False)
# print(tokenizer.decode(outputs[0]))

#%% In ProntoQA formatted changed

prompt = "Hello, how are you?"

messages = [
{"role": "user", "content": prompt},
]
prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
inputs = tokenizer.encode(prompt, add_special_tokens=False, return_tensors="pt")
# greedy decoding if num_beams=1 and do_sample=False
outputs = model.generate(input_ids=inputs.to(model.device), max_length=200, use_cache = True, num_beams=1, do_sample=False)# , top_p=1, repetition_penalty=0.0001,)
response = tokenizer.decode(outputs[0], skip_special_tokens=True)
print("Response")
print(response)
print("\n\n")

stop = "\nmodel\n"
# stop = "Answer"
# slicing off the prompt 
if stop in response:
    response_sliced = response.split(stop)[1]
    print("\n-----True 1-----\n")
else:
    response_sliced = response
    print("\n-----False 1-----\n")
    
print("Sliced response")
print(response_sliced)
print("\n\n")

import re
answer = re.sub("\s+", " ", response_sliced)
print("Answer")
print(answer)
print("\n\n")
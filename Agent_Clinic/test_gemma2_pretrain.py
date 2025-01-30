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

input_text = "Write me a poem about Machine Learning."
input_ids = tokenizer(input_text, return_tensors="pt").to("cuda")

outputs = model.generate(**input_ids, max_new_tokens=200, use_cache = True, do_sample=False)
# outputs = model.generate(**inputs, max_new_tokens = 256, use_cache = True, do_sample=False, top_p=1, repetition_penalty=0.0001,)

print("output starts#########################")
print(tokenizer.decode(outputs[0]))
print("output ends#########################")
print("processed output starts#########################")
answer = tokenizer.decode(outputs[0, len(inputs):])
import re
answer = re.sub("\s+", " ", answer)
print("processed ends#########################")
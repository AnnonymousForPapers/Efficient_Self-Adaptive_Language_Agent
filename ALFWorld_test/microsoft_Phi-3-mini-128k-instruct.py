from transformers import AutoTokenizer, AutoModelForCausalLM

model_name = "microsoft/Phi-3-mini-128k-instruct"
print("\n" + "Model name: " + model_name + "\n")

access_token = ""

tokenizer = AutoTokenizer.from_pretrained(model_name, token=access_token)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    device_map="auto",
    torch_dtype="auto",
    trust_remote_code=True,
    token=access_token
)
initial_prompt = "Interact with a household to solve a task. Here are two examples.\nYou are in the middle of a room. Looking quickly around you, you see a cabinet 4, a cabinet 3, a cabinet 2, a cabinet 1, a coffeemachine 1, a countertop 1, a diningtable 3, a diningtable 2, a diningtable 1, a drawer 1, a fridge 1, a garbagecan 1, a microwave 1, a sidetable 1, a sinkbasin 1, a stoveburner 4, a stoveburner 3, a stoveburner 2, a stoveburner 1, and a toaster 1.\nYour task is to: clean some apple and put it in sidetable.\n> think: To solve the task, I need to find and take an apple, then clean it with sinkbasin, then put it in sidetable.\nOK.\n> think: First I need to find an apple. An apple is more likely to appear in fridges (1), diningtable (1-3), sidetable (1), countertop (1), sinkbasin (1), garbagecan (1). I can check one by one, starting with fridge 1.\nOK.\n> go to fridge 1\nThe fridge 1 is closed.\n> open fridge 1\nYou open the fridge 1. The fridge 1 is open. In it, you see a lettuce 2, a mug 2, a potato 2, and a tomato 1.\n> go to diningtable 1\nOn the diningtable 1, you see nothing.\n> go to diningtable 2\nOn the diningtable 2, you see a pineapple 1.\n> go to diningtable 3\nOn the diningtable 3, you see a bowl 2, a bowl 1, a bread 2, and a bread 1.\n> go to sidetable 1\nOn the sidetable 1, you see a cup 1, a lettuce 1, a peppershaker 3, a potato 1, and a saltshaker 1.\n> go to countertop 1\nOn the countertop 1, you see a butterknife 1, a dishsponge 1, and a soapbottle 1.\n> go to sinkbasin 1\nOn the sinkbasin 1, you see a cup 2, a egg 1, a mug 1, and a potato 3.\n> go to garbagecan 1\nOn the garbagecan 1, you see a apple 3, and a egg 3.\n> think: Now I find an apple (3). Next, I need to take it.\nOK.\n> take apple 3 from garbagecan 1\nYou pick up the apple 3 from the garbagecan 1.\n> think: Now I take an apple (3). Next, I need to go to sinkbasin (1) and clean it.\nOK.\n> go to sinkbasin 1\nOn the sinkbasin 1, you see a cup 2, a egg 1, a mug 1, and a potato 3.\n> clean apple 3 with sinkbasin 1\nYou clean the apple 3 using the sinkbasin 1.\n> think: Now I clean an apple (3). Next, I need to put it in/on sidetable 1.\nOK.\n> go to sidetable 1\nOn the sidetable 1, you see a cup 1, a lettuce 1, a peppershaker 3, a potato 1, and a saltshaker 1.\n> put apple 3 in/on sidetable 1\nYou put the apple 3 in/on the sidetable 1.\nYou are in the middle of a room. Looking quickly around you, you see a cabinet 13, a cabinet 12, a cabinet 11, a cabinet 10, a cabinet 9, a cabinet 8, a cabinet 7, a cabinet 6, a cabinet 5, a cabinet 4, a cabinet 3, a cabinet 2, a cabinet 1, a coffeemachine 1, a countertop 1, a diningtable 1, a drawer 1, a fridge 1, a garbagecan 1, a microwave 1, a shelf 3, a shelf 2, a shelf 1, a sinkbasin 1, a stoveburner 4, a stoveburner 3, a stoveburner 2, a stoveburner 1, and a toaster 1.\nYour task is to: put a clean lettuce in diningtable.\n> think: To solve the task, I need to find and take a lettuce, then clean it with sinkbasin, then put it in diningtable. \nOK.\n> think: First I need to find a lettuce. A lettuce is more likely to appear in fridge (1), diningtable (1), sinkbasin (1), stoveburner (1-3), cabinet (1-13). I can check one by one, starting with fridge 1.\nOK.\n> go to fridge 1\nThe fridge 1 is closed.\n> open fridge 1\nYou open the fridge 1. The fridge 1 is open. In it, you see a cup 3, a egg 2, a potato 3, and a potato 2.\n> go to diningtable 1\nOn the diningtable 1, you see a apple 1, a bread 1, a butterknife 2, a cup 2, a fork 2, a knife 2, a knife 1, a ladle 1, a lettuce 1, a mug 2, a mug 1, a pan 2, a peppershaker 1, a spatula 3, a tomato 2, and a tomato 1.\n> think: Now I find a lettuce (1). Next, I need to take it.\nOK.\n> take lettuce 1 from diningtable 1\nYou pick up the lettuce 1 from the diningtable 1.\n> think: Now I take a lettuce (1). Next, I need to go to sinkbasin (1) and clean it.\nOK.\n> go to sinkbasin 1\nOn the sinkbasin 1, you see a apple 2, a ladle 2, a spoon 1, and a tomato 3.\n> clean lettuce 1 with sinkbasin 1\nYou clean the lettuce 1 using the sinkbasin 1.\n> think: Now I clean a lettuce (1). Next, I need to put it in/on diningtable 1.\nOK.\n> go to diningtable 1\nOn the diningtable 1, you see a apple 1, a bread 1, a butterknife 2, a cup 2, a fork 2, a knife 2, a knife 1, a ladle 1, a mug 2, a mug 1, a pan 2, a peppershaker 1, a spatula 3, a tomato 2, and a tomato 1.\n> put lettuce 1 in/on diningtable 1\nYou put the lettuce 1 in/on the diningtable 1.\n\nHere is the task.\n"
task_prompt = "You are in the middle of a room. Looking quickly around you, you see a cabinet 6, a cabinet 5, a cabinet 4, a cabinet 3, a cabinet 2, a cabinet 1, a coffeemachine 1, a countertop 3, a countertop 2, a countertop 1, a drawer 3, a drawer 2, a drawer 1, a fridge 1, a garbagecan 1, a microwave 1, a shelf 3, a shelf 2, a shelf 1, a sinkbasin 1, a stoveburner 4, a stoveburner 3, a stoveburner 2, a stoveburner 1, and a toaster 1.\nYour task is to: put a clean knife in countertop.\n>"
prompt = ''

inputs = tokenizer(
        [
            initial_prompt + task_prompt + prompt
        ], return_tensors = "pt").to("cuda")
outputs = model.generate(**inputs, max_new_tokens = 400, use_cache = True, do_sample=False, top_p=1, repetition_penalty=0.0001,)
action_1 = tokenizer.batch_decode(outputs)[0]
print(action_1)

# 1
# initializing stop string
action_1 = action_1.replace(r"\n", "\n")
stop=initial_prompt + task_prompt + prompt + " "
# slicing off after length computation
if stop in action_1:
  action_2 = action_1.split(stop)[1]
  print("\n-----True 1-----\n")
else:
  action_2 = action_1
  print("\n-----False 1-----\n")
# 2
# initializing stop string
stop="\n"
# slicing off after length computation
if stop in action_2:
  action_3 = action_2.split(stop)[0]
  print("\n-----True 2-----\n")
else:
  action_3 = action_2
  print("\n-----False 2-----\n")
action = action_3
print(action)
print("\n-----NLP output end-----\n\n")

observation = 'OK.'
prompt += f' {action}\n{observation}\n>'
print(prompt)

inputs = tokenizer(
        [
            initial_prompt + task_prompt + prompt
        ], return_tensors = "pt").to("cuda")
outputs = model.generate(**inputs, max_new_tokens = 400, use_cache = True, do_sample=False, top_p=1,)
action_1 = tokenizer.batch_decode(outputs)[0]
print(action_1)

# 1
# initializing stop string
action_1 = action_1.replace(r"\n", "\n")
stop=initial_prompt + task_prompt + prompt + " "
# slicing off after length computation
if stop in action_1:
  action_2 = action_1.split(stop)[1]
  print("\n-----True 1-----\n")
else:
  action_2 = action_1
  print("\n-----False 1-----\n")
# 2
# initializing stop string
stop="\n"
# slicing off after length computation
if stop in action_2:
  action_3 = action_2.split(stop)[0]
  print("\n-----True 2-----\n")
else:
  action_3 = action_2
  print("\n-----False 2-----\n")
action = action_3
print(action)
print("\n-----NLP output end-----\n\n")
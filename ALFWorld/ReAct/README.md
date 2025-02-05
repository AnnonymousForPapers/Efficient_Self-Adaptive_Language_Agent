# ReAct prompting in the ALFWorld environment using gemma2-9b-it
We implemented the (ReAct prompting)[#ReAct] in the "ALFW_google_gemma-2-9b-it.py" file for comparison of SALA and ESALA. 

## Installation
Before running the code, please install torch, the transformers dataset by following [their instruction](https://huggingface.co/docs/transformers/installation), and then install the ALFWorld environment by following their [Install Source instruction](https://github.com/alfworld/alfworld#install-source).

After installing the PDDL files and the game files in the [Install Source instruction](https://github.com/alfworld/alfworld#install-source), Please enter
```
export ALFWORLD_DATA=<storage_path>
```
in the terminal everytime before running the code to make the tasks order the same. The <storage_path> is the path that you stores the ALFWorld repository.

## Contents
We used [the exemplar](#Exemplar) from the [ReAct prompting paper](#ReAct) to prompt the gemma2-9b-it.

In order to run the python file, we need to enter the Hugging Face access token on the right side of "access_token = ". We can get the Hugging Face access token by following the instruction in [their tutorial](https://huggingface.co/docs/hub/security-tokens).

To run the python file, please use
```
ALFW_google_gemma-2-9b-it.py
```
in the terminal.

## Control the start of the task number
In order to start the task on different task number, please change the number on the right of 
```
env_start_num = 
```
at line 128 in either "Append_RFLX_noExplicit.py", "Append_RFLX_noExplicit_rmvRflx0.py", or "Append_RFLX_noExplicit_rmvRflx1.py". The number should be the task number you want to start with.

## Outputs
After a task is completed, the statistics will be appended below the last observation as:
```
{task_number} r {task_status} rs {success_counts_per_task_type} cnts {total_counts_per_task_type} sum(rs)/sum(cnts) {success_rate}
```
, where {task_number} is an integer that represents the number of the task starting from 1, {task_status} is 0 if the task fails or True if the task completes, {success_counts_per_task_type} shows the counts of the successful tasks for each task types, {total_counts_per_task_type} shows the counts of the tasks for each task types, and {success_rate} is the result of sum(rs)/sum(cnts), which is the ratio of {success_counts_per_task_type} divided by {total_counts_per_task_type}. 

The counts of {success_counts_per_task_type} and {total_counts_per_task_type} are stored in a list with 6 elements. Each element corresponds to one task type and the task types in each list are in the order of **['put', 'clean', 'heat', 'cool', 'examine', 'puttwo']**, where 
- 'put' represents the **Pick and Place** task
- 'clean' represents the **Clean and Place** task
- 'heat' represents the **Heat and Place** task
- 'cool' represents the **Cool and Place** task
- 'examine' represents the **Examine in Light** task
- 'puttwo' represents the **Pick Two and Place** task.

## The initial prompt without the test environment information of each agent is listed below:
### ReAct
  ```
  Interact with a household to solve a task. Here are two examples.
  You are in the middle of a room. Looking quickly around you, you see a cabinet 4, a cabinet 3, a cabinet 2, a cabinet 1, a coffeemachine 1, a countertop 1, a diningtable 3, a diningtable 2, a diningtable 1, a drawer 1, a fridge 1, a garbagecan 1, a microwave 1, a sidetable 1, a sinkbasin 1, a stoveburner 4, a stoveburner 3, a stoveburner 2, a stoveburner 1, and a toaster 1.
  Your task is to: clean some apple and put it in sidetable.
  > think: To solve the task, I need to find and take an apple, then clean it with sinkbasin, then put it in sidetable.
  OK.
  > think: First I need to find an apple. An apple is more likely to appear in fridges (1), diningtable (1-3), sidetable (1), countertop (1), sinkbasin (1), garbagecan (1). I can check one by one, starting with fridge 1.
  OK.
  > go to fridge 1
  The fridge 1 is closed.
  > open fridge 1
  You open the fridge 1. The fridge 1 is open. In it, you see a lettuce 2, a mug 2, a potato 2, and a tomato 1.
  > go to diningtable 1
  On the diningtable 1, you see nothing.
  > go to diningtable 2
  On the diningtable 2, you see a pineapple 1.
  > go to diningtable 3
  On the diningtable 3, you see a bowl 2, a bowl 1, a bread 2, and a bread 1.
  > go to sidetable 1
  On the sidetable 1, you see a cup 1, a lettuce 1, a peppershaker 3, a potato 1, and a saltshaker 1.
  > go to countertop 1
  On the countertop 1, you see a butterknife 1, a dishsponge 1, and a soapbottle 1.
  > go to sinkbasin 1
  On the sinkbasin 1, you see a cup 2, a egg 1, a mug 1, and a potato 3.
  > go to garbagecan 1
  On the garbagecan 1, you see a apple 3, and a egg 3.
  > think: Now I find an apple (3). Next, I need to take it.
  OK.
  > take apple 3 from garbagecan 1
  You pick up the apple 3 from the garbagecan 1.
  > think: Now I take an apple (3). Next, I need to go to sinkbasin (1) and clean it.
  OK.
  > go to sinkbasin 1
  On the sinkbasin 1, you see a cup 2, a egg 1, a mug 1, and a potato 3.
  > clean apple 3 with sinkbasin 1
  You clean the apple 3 using the sinkbasin 1.
  > think: Now I clean an apple (3). Next, I need to put it in/on sidetable 1.
  OK.
  > go to sidetable 1
  On the sidetable 1, you see a cup 1, a lettuce 1, a peppershaker 3, a potato 1, and a saltshaker 1.
  > put apple 3 in/on sidetable 1
  You put the apple 3 in/on the sidetable 1.
  You are in the middle of a room. Looking quickly around you, you see a cabinet 13, a cabinet 12, a cabinet 11, a cabinet 10, a cabinet 9, a cabinet 8, a cabinet 7, a cabinet 6, a cabinet 5, a cabinet 4, a cabinet 3, a cabinet 2, a cabinet 1, a coffeemachine 1, a countertop 1, a diningtable 1, a drawer 1, a fridge 1, a garbagecan 1, a microwave 1, a shelf 3, a shelf 2, a shelf 1, a sinkbasin 1, a stoveburner 4, a stoveburner 3, a stoveburner 2, a stoveburner 1, and a toaster 1.
  Your task is to: put a clean lettuce in diningtable.
  > think: To solve the task, I need to find and take a lettuce, then clean it with sinkbasin, then put it in diningtable. 
  OK.
  > think: First I need to find a lettuce. A lettuce is more likely to appear in fridge (1), diningtable (1), sinkbasin (1), stoveburner (1-3), cabinet (1-13). I can check one by one, starting with fridge 1.
  OK.
  > go to fridge 1
  The fridge 1 is closed.
  > open fridge 1
  You open the fridge 1. The fridge 1 is open. In it, you see a cup 3, a egg 2, a potato 3, and a potato 2.
  > go to diningtable 1
  On the diningtable 1, you see a apple 1, a bread 1, a butterknife 2, a cup 2, a fork 2, a knife 2, a knife 1, a ladle 1, a lettuce 1, a mug 2, a mug 1, a pan 2, a peppershaker 1, a spatula 3, a tomato 2, and a tomato 1.
  > think: Now I find a lettuce (1). Next, I need to take it.
  OK.
  > take lettuce 1 from diningtable 1
  You pick up the lettuce 1 from the diningtable 1.
  > think: Now I take a lettuce (1). Next, I need to go to sinkbasin (1) and clean it.
  OK.
  > go to sinkbasin 1
  On the sinkbasin 1, you see a apple 2, a ladle 2, a spoon 1, and a tomato 3.
  > clean lettuce 1 with sinkbasin 1
  You clean the lettuce 1 using the sinkbasin 1.
  > think: Now I clean a lettuce (1). Next, I need to put it in/on diningtable 1.
  OK.
  > go to diningtable 1
  On the diningtable 1, you see a apple 1, a bread 1, a butterknife 2, a cup 2, a fork 2, a knife 2, a knife 1, a ladle 1, a mug 2, a mug 1, a pan 2, a peppershaker 1, a spatula 3, a tomato 2, and a tomato 1.
  > put lettuce 1 in/on diningtable 1
  You put the lettuce 1 in/on the diningtable 1.
  
  Here is the task.
  ```
## References
### ReAct
```
@inproceedings{yao2023react,
  title = {{ReAct}: Synergizing Reasoning and Acting in Language Models},
  author = {Yao, Shunyu and Zhao, Jeffrey and Yu, Dian and Du, Nan and Shafran, Izhak and Narasimhan, Karthik and Cao, Yuan},
  booktitle = {International Conference on Learning Representations (ICLR) },
  year = {2023},
  html = {https://arxiv.org/abs/2210.03629},
}
```
## Gemma 2
```
@misc{gemmateam2024gemma2improvingopen,
      title={Gemma 2: Improving Open Language Models at a Practical Size}, 
      author={Gemma Team and Morgane Riviere and Shreya Pathak and Pier Giuseppe Sessa and Cassidy Hardin and Surya Bhupatiraju and Léonard Hussenot and Thomas Mesnard and Bobak Shahriari and Alexandre Ramé and Johan Ferret and Peter Liu and Pouya Tafti and Abe Friesen and Michelle Casbon and Sabela Ramos and Ravin Kumar and Charline Le Lan and Sammy Jerome and Anton Tsitsulin and Nino Vieillard and Piotr Stanczyk and Sertan Girgin and Nikola Momchev and Matt Hoffman and Shantanu Thakoor and Jean-Bastien Grill and Behnam Neyshabur and Olivier Bachem and Alanna Walton and Aliaksei Severyn and Alicia Parrish and Aliya Ahmad and Allen Hutchison and Alvin Abdagic and Amanda Carl and Amy Shen and Andy Brock and Andy Coenen and Anthony Laforge and Antonia Paterson and Ben Bastian and Bilal Piot and Bo Wu and Brandon Royal and Charlie Chen and Chintu Kumar and Chris Perry and Chris Welty and Christopher A. Choquette-Choo and Danila Sinopalnikov and David Weinberger and Dimple Vijaykumar and Dominika Rogozińska and Dustin Herbison and Elisa Bandy and Emma Wang and Eric Noland and Erica Moreira and Evan Senter and Evgenii Eltyshev and Francesco Visin and Gabriel Rasskin and Gary Wei and Glenn Cameron and Gus Martins and Hadi Hashemi and Hanna Klimczak-Plucińska and Harleen Batra and Harsh Dhand and Ivan Nardini and Jacinda Mein and Jack Zhou and James Svensson and Jeff Stanway and Jetha Chan and Jin Peng Zhou and Joana Carrasqueira and Joana Iljazi and Jocelyn Becker and Joe Fernandez and Joost van Amersfoort and Josh Gordon and Josh Lipschultz and Josh Newlan and Ju-yeong Ji and Kareem Mohamed and Kartikeya Badola and Kat Black and Katie Millican and Keelin McDonell and Kelvin Nguyen and Kiranbir Sodhia and Kish Greene and Lars Lowe Sjoesund and Lauren Usui and Laurent Sifre and Lena Heuermann and Leticia Lago and Lilly McNealus and Livio Baldini Soares and Logan Kilpatrick and Lucas Dixon and Luciano Martins and Machel Reid and Manvinder Singh and Mark Iverson and Martin Görner and Mat Velloso and Mateo Wirth and Matt Davidow and Matt Miller and Matthew Rahtz and Matthew Watson and Meg Risdal and Mehran Kazemi and Michael Moynihan and Ming Zhang and Minsuk Kahng and Minwoo Park and Mofi Rahman and Mohit Khatwani and Natalie Dao and Nenshad Bardoliwalla and Nesh Devanathan and Neta Dumai and Nilay Chauhan and Oscar Wahltinez and Pankil Botarda and Parker Barnes and Paul Barham and Paul Michel and Pengchong Jin and Petko Georgiev and Phil Culliton and Pradeep Kuppala and Ramona Comanescu and Ramona Merhej and Reena Jana and Reza Ardeshir Rokni and Rishabh Agarwal and Ryan Mullins and Samaneh Saadat and Sara Mc Carthy and Sarah Cogan and Sarah Perrin and Sébastien M. R. Arnold and Sebastian Krause and Shengyang Dai and Shruti Garg and Shruti Sheth and Sue Ronstrom and Susan Chan and Timothy Jordan and Ting Yu and Tom Eccles and Tom Hennigan and Tomas Kocisky and Tulsee Doshi and Vihan Jain and Vikas Yadav and Vilobh Meshram and Vishal Dharmadhikari and Warren Barkley and Wei Wei and Wenming Ye and Woohyun Han and Woosuk Kwon and Xiang Xu and Zhe Shen and Zhitao Gong and Zichuan Wei and Victor Cotruta and Phoebe Kirk and Anand Rao and Minh Giang and Ludovic Peran and Tris Warkentin and Eli Collins and Joelle Barral and Zoubin Ghahramani and Raia Hadsell and D. Sculley and Jeanine Banks and Anca Dragan and Slav Petrov and Oriol Vinyals and Jeff Dean and Demis Hassabis and Koray Kavukcuoglu and Clement Farabet and Elena Buchatskaya and Sebastian Borgeaud and Noah Fiedel and Armand Joulin and Kathleen Kenealy and Robert Dadashi and Alek Andreev},
      year={2024},
      eprint={2408.00118},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2408.00118}, 
}
```
## ALFWorld
```
@inproceedings{ALFWorld20,
  title ={{ALFWorld: Aligning Text and Embodied
           Environments for Interactive Learning}},
  author={Mohit Shridhar and Xingdi Yuan and
          Marc-Alexandre C\^ot\'e and Yonatan Bisk and
          Adam Trischler and Matthew Hausknecht},
  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},
  year = {2021},
  url = {https://arxiv.org/abs/2010.03768}
}
```
## ALFRED
```
@inproceedings{ALFRED20,
  title ={{ALFRED: A Benchmark for Interpreting Grounded
           Instructions for Everyday Tasks}},
  author={Mohit Shridhar and Jesse Thomason and Daniel Gordon and Yonatan Bisk and
          Winson Han and Roozbeh Mottaghi and Luke Zettlemoyer and Dieter Fox},
  booktitle = {The IEEE Conference on Computer Vision and Pattern Recognition (CVPR)},
  year = {2020},
  url  = {https://arxiv.org/abs/1912.01734}
}
```
## TextWorld
```
@inproceedings{cote2018textworld,
  title={Textworld: A learning environment for text-based games},
  author={C{\^o}t{\'e}, Marc-Alexandre and K{\'a}d{\'a}r, {\'A}kos and Yuan, Xingdi and Kybartas, Ben and Barnes, Tavian and Fine, Emery and Moore, James and Hausknecht, Matthew and El Asri, Layla and Adada, Mahmoud and others},
  booktitle={Workshop on Computer Games},
  pages={41--75},
  year={2018},
  organization={Springer}
}
```


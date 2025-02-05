# Implementation of SALA in the AgentClinic environment
We implemented the proposed SALA in the "adaptation_gemma2_9b_it_agentclinic.py" and implement the vanilla prompting method from [the AgentClinic GitHub](https://github.com/samuelschmidgall/agentclinic) with gemma2-9b-it in "gemma2_9b_it_agentclinic.py". 

## Installation
Before running the code, please follow [the instruction from the AgentClinic GitHub](https://github.com/samuelschmidgall/agentclinic).

## Contents
To run the "adaptation_gemma2_9b_it_agentclinic.py" python file, please use
```
python adaptation_gemma2_9b_it_agentclinic.py --huggingface_api_key "" --inf_type "llm" --num_scenarios 15 --total_inferences 20
```
To run the "gemma2_9b_it_agentclinic.py" python file, please use
```
python gemma2_9b_it_agentclinic.py --huggingface_api_key "" --inf_type "llm" --num_scenarios 15 --total_inferences 20
```
, where the Hugging Face access token should be enter inside the "" on the right side of
```
--huggingface_api_key ""
```
We can get the Hugging Face access token by following the instruction in [their tutorial](https://huggingface.co/docs/hub/security-tokens).

## Outputs
After a task is completed, the statistics will be appended below the last observation as:
```
Correct answer: {Correct_diagnosis}
Scene {task_number}, The diagnosis was  {correctness} {correct_diagnosis_rate}
```
, where {task_number} is an integer that represents the number of the task starting from 1, {Correct_diagnosis} is the diagnosis the agent should give, {correctness} shows CORRECT if the diagnosis is correct and INCORRECT if the diagnosis is incorrect, and {correct_diagnosis_rate} is the ratio of the counts of the correct diagnosis divided by the counts of the total tasks. 

## References
### Gemma 2
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
### AgentClinic
```
@misc{schmidgall2024agentclinic,
      title={AgentClinic: a multimodal agent benchmark to evaluate AI in simulated clinical environments}, 
      author={Samuel Schmidgall and Rojin Ziaei and Carl Harris and Eduardo Reis and Jeffrey Jopling and Michael Moor},
      year={2024},
      eprint={2405.07960},
      archivePrefix={arXiv},
      primaryClass={cs.HC}
}
```

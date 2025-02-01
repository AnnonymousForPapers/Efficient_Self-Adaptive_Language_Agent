# Codes related to the ALFWorld environment
## Contents
The codes related to the test of different language models in the ALFWorld environment using ReAct prompting are in the [ALFWorld_test folder](ALFWorld_test/README.md).

The codes related to the test of the proposed Self-Adaptive Language Agent (SALA) and Efficient Self-Adaptive Language Agent (ESALA) in the ALFWorld environment are in the [Adaptation folder](Adaptation/README.md).

The codes related to the test of the gemma2-9b-it in the ALFWorld environment using ReAct prompting are in the [ReAct folder](ReAct/README.md).

The codes related to the statistics of the gemma2-9b-it in the ALFWorld environment using ReAct prompting, SALA, and ESALA are in the [Records folder](Records/README.md).

## References
### References related to ReAct prompting
**ReAct**
```
@inproceedings{yao2023react,
  title = {{ReAct}: Synergizing Reasoning and Acting in Language Models},
  author = {Yao, Shunyu and Zhao, Jeffrey and Yu, Dian and Du, Nan and Shafran, Izhak and Narasimhan, Karthik and Cao, Yuan},
  booktitle = {International Conference on Learning Representations (ICLR) },
  year = {2023},
  html = {https://arxiv.org/abs/2210.03629},
}
```
### References related to the ALEWorld environment
**ALFWorld**
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
**ALFRED**
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
**TextWorld**
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
### References related to the language models we used
**Gemma 2**
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
**Mistral**
```
@misc{jiang2024mixtralexperts,
      title={Mixtral of Experts}, 
      author={Albert Q. Jiang and Alexandre Sablayrolles and Antoine Roux and Arthur Mensch and Blanche Savary and Chris Bamford and Devendra Singh Chaplot and Diego de las Casas and Emma Bou Hanna and Florian Bressand and Gianna Lengyel and Guillaume Bour and Guillaume Lample and Lélio Renard Lavaud and Lucile Saulnier and Marie-Anne Lachaux and Pierre Stock and Sandeep Subramanian and Sophia Yang and Szymon Antoniak and Teven Le Scao and Théophile Gervet and Thibaut Lavril and Thomas Wang and Timothée Lacroix and William El Sayed},
      year={2024},
      eprint={2401.04088},
      archivePrefix={arXiv},
      primaryClass={cs.LG},
      url={https://arxiv.org/abs/2401.04088}, 
}
```
**Llama**
```
@misc{touvron2023llama2openfoundation,
      title={Llama 2: Open Foundation and Fine-Tuned Chat Models}, 
      author={Hugo Touvron and Louis Martin and Kevin Stone and Peter Albert and Amjad Almahairi and Yasmine Babaei and Nikolay Bashlykov and Soumya Batra and Prajjwal Bhargava and Shruti Bhosale and Dan Bikel and Lukas Blecher and Cristian Canton Ferrer and Moya Chen and Guillem Cucurull and David Esiobu and Jude Fernandes and Jeremy Fu and Wenyin Fu and Brian Fuller and Cynthia Gao and Vedanuj Goswami and Naman Goyal and Anthony Hartshorn and Saghar Hosseini and Rui Hou and Hakan Inan and Marcin Kardas and Viktor Kerkez and Madian Khabsa and Isabel Kloumann and Artem Korenev and Punit Singh Koura and Marie-Anne Lachaux and Thibaut Lavril and Jenya Lee and Diana Liskovich and Yinghai Lu and Yuning Mao and Xavier Martinet and Todor Mihaylov and Pushkar Mishra and Igor Molybog and Yixin Nie and Andrew Poulton and Jeremy Reizenstein and Rashi Rungta and Kalyan Saladi and Alan Schelten and Ruan Silva and Eric Michael Smith and Ranjan Subramanian and Xiaoqing Ellen Tan and Binh Tang and Ross Taylor and Adina Williams and Jian Xiang Kuan and Puxin Xu and Zheng Yan and Iliyan Zarov and Yuchen Zhang and Angela Fan and Melanie Kambadur and Sharan Narang and Aurelien Rodriguez and Robert Stojnic and Sergey Edunov and Thomas Scialom},
      year={2023},
      eprint={2307.09288},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2307.09288}, 
}
```
**Phi-3**
```
@misc{abdin2024phi3technicalreporthighly,
      title={Phi-3 Technical Report: A Highly Capable Language Model Locally on Your Phone}, 
      author={Marah Abdin and Jyoti Aneja and Hany Awadalla and Ahmed Awadallah and Ammar Ahmad Awan and Nguyen Bach and Amit Bahree and Arash Bakhtiari and Jianmin Bao and Harkirat Behl and Alon Benhaim and Misha Bilenko and Johan Bjorck and Sébastien Bubeck and Martin Cai and Qin Cai and Vishrav Chaudhary and Dong Chen and Dongdong Chen and Weizhu Chen and Yen-Chun Chen and Yi-Ling Chen and Hao Cheng and Parul Chopra and Xiyang Dai and Matthew Dixon and Ronen Eldan and Victor Fragoso and Jianfeng Gao and Mei Gao and Min Gao and Amit Garg and Allie Del Giorno and Abhishek Goswami and Suriya Gunasekar and Emman Haider and Junheng Hao and Russell J. Hewett and Wenxiang Hu and Jamie Huynh and Dan Iter and Sam Ade Jacobs and Mojan Javaheripi and Xin Jin and Nikos Karampatziakis and Piero Kauffmann and Mahoud Khademi and Dongwoo Kim and Young Jin Kim and Lev Kurilenko and James R. Lee and Yin Tat Lee and Yuanzhi Li and Yunsheng Li and Chen Liang and Lars Liden and Xihui Lin and Zeqi Lin and Ce Liu and Liyuan Liu and Mengchen Liu and Weishung Liu and Xiaodong Liu and Chong Luo and Piyush Madan and Ali Mahmoudzadeh and David Majercak and Matt Mazzola and Caio César Teodoro Mendes and Arindam Mitra and Hardik Modi and Anh Nguyen and Brandon Norick and Barun Patra and Daniel Perez-Becker and Thomas Portet and Reid Pryzant and Heyang Qin and Marko Radmilac and Liliang Ren and Gustavo de Rosa and Corby Rosset and Sambudha Roy and Olatunji Ruwase and Olli Saarikivi and Amin Saied and Adil Salim and Michael Santacroce and Shital Shah and Ning Shang and Hiteshi Sharma and Yelong Shen and Swadheen Shukla and Xia Song and Masahiro Tanaka and Andrea Tupini and Praneetha Vaddamanu and Chunyu Wang and Guanhua Wang and Lijuan Wang and Shuohang Wang and Xin Wang and Yu Wang and Rachel Ward and Wen Wen and Philipp Witte and Haiping Wu and Xiaoxia Wu and Michael Wyatt and Bin Xiao and Can Xu and Jiahang Xu and Weijian Xu and Jilong Xue and Sonali Yadav and Fan Yang and Jianwei Yang and Yifan Yang and Ziyi Yang and Donghan Yu and Lu Yuan and Chenruidong Zhang and Cyril Zhang and Jianwen Zhang and Li Lyna Zhang and Yi Zhang and Yue Zhang and Yunan Zhang and Xiren Zhou},
      year={2024},
      eprint={2404.14219},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2404.14219}, 
}
```
**DeepSeek**
```
@article{deepseek-llm,
  author = {DeepSeek-AI},
  title = {DeepSeek LLM: Scaling Open-Source Language Models with Longtermism},
  journal = {arXiv preprint arXiv:2401.02954},
  year = {2024},
  url = {https://github.com/deepseek-ai/DeepSeek-LLM}
}
```
**Zephyr**
```
@misc{tunstall2023zephyr,
      title={Zephyr: Direct Distillation of LM Alignment}, 
      author={Lewis Tunstall and Edward Beeching and Nathan Lambert and Nazneen Rajani and Kashif Rasul and Younes Belkada and Shengyi Huang and Leandro von Werra and Clémentine Fourrier and Nathan Habib and Nathan Sarrazin and Omar Sanseviero and Alexander M. Rush and Thomas Wolf},
      year={2023},
      eprint={2310.16944},
      archivePrefix={arXiv},
      primaryClass={cs.LG}
}
```

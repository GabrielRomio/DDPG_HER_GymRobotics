========================================

EN

Reinforcement Learning (RL) is the area of artificial intelligence where agents learn to make optimized decisions by interacting with an environment. Unlike traditional approaches, in RL, the agent explores the environment, learning from rewards and penalties over time until it masters the given task.

One of the most popular algorithms in reinforcement learning is DDPG (Deep Deterministic Policy Gradient). It is an off-policy algorithm based on actor-critic architecture, where the actor is responsible for learning the policy (actions) and the critic evaluates the policy based on the expected return. It is suitable for continuous and high-dimensional environments, common in robotic applications. The HER (Hindsight Experience Replay) technique is often combined with DDPG to enhance learning in tasks where the search space is vast and goals are rarely achieved. HER allows the agent to learn from past experiences or failures even when the initial objective was not reached.

The OpenAI Gym and Gymnasium-Robotics environments provide robust platforms for RL agent simulation and training. Gym offers a wide range of standardized environments, while Gymnasium-Robotics focuses on robotic manipulation tasks, simulating realistic scenarios for the development of algorithms aimed at industrial robots. By combining these environments with MuJoCo, a physics simulator primarily used for modeling and simulation, a near-realistic environment is achieved for industrial robot applications.

Therefore, combining DDPG with HER in these simulated environments allows for training robots to perform complex tasks and precise object manipulation. By training models in simulated environments, this learning can be transferred to physical robots, resulting in more adaptable industrial systems capable of handling unpredictable variables and making real-time adjustments. This is particularly useful in industries requiring precision, such as automotive and manufacturing, where robots need to quickly adapt to different scenarios without manual reprogramming. These advances can enhance industrial processes, reducing costs and increasing productivity in dynamic and complex environments.

This work presents an example of training based on the conditions mentioned above. A 98% success rate was achieved with training over 35,000,000 interactions across 12 simultaneous environments. The training was conducted using a Ryzen 5 5800 CPU over 6.5 hours.
A demonstration can be found at: https://www.youtube.com/shorts/KCNRaKu_uFA

Developed by Gabriel Romio

========================================

PT-BR

O Aprendizado por Reforço (RL) é a área da inteligência artificial em que agentes aprendem a tomar decisões otimizadas interagindo com um ambiente. Diferente de abordagens tradicionais, em RL o agente explora o ambiente, aprendendo com recompensas e penalidades ao longo do tempo, até dominar a tarefa em questão.

Um dos algoritmos mais populares em aprendizado por reforço é o DDPG (Deep Deterministic Policy Gradient). Ele é um algoritmo "off-policy" baseado em atores-críticos, onde o ator é responsável por aprender a política (ações) e o crítico avalia a política baseada no retorno esperado. É indicado para ambientes contínuos e de alta dimensão, comuns em aplicações robóticas. A técnica HER (Hindsight Experience Replay) é frequentemente combinada com o DDPG para melhorar o aprendizado em tarefas onde o espaço de busca é vasto e os objetivos são raramente alcançados. Assim, o HER possibilita que o agente aprenda com experiências passadas ou falhas mesmo quando o objetivo inicial não foi atingido.

Os ambientes OpenAI Gym e Gymnasium-Robotics fornecem plataformas robustas para a simulação e treinamento de agentes de RL. O Gym oferece uma ampla gama de ambientes padronizados, enquanto o Gymnasium-Robotics é focado em tarefas de manipulação robótica, simulando cenários realistas para o desenvolvimento de algoritmos voltados a robôs industriais. Combinando esses ambientes com o MuJoCo, um simulador de física usado principalmente para modelagem e simulação, obtém-se um ambiente próximo da realidade à que um robô industrial estará submetido.

Assim, a combinação de DDPG com HER nesses ambientes simulados permite treinar robôs para realizar tarefas complexas e manipulação precisa de objetos. Ao treinar modelos em ambientes simulados, pode-se transferir esse aprendizado para robôs físicos, resultando em sistemas industriais mais adaptáveis, capazes de lidar com variáveis imprevisíveis e realizar ajustes em tempo real. Isso é particularmente útil em indústrias que exigem precisão, como automotiva e manufatura, onde robôs precisam adaptar-se rapidamente a diferentes cenários sem a necessidade de reprogramação manual. Esses avanços podem aperfeiçoar processos industriais, reduzindo custos e aumentando a produtividade em ambientes dinâmicos e complexos.

Este trabalho apresenta um exemplo de treinamento com base nas condições citadas acima. Obteve-se 98% de aproveitamento com um treinamento ao longo de 35.000.000 de interações em 12 ambientes simultâneos. O treinamento se deu utilizando como hardware uma CPU Ryzen 5 5800, ao longo de 6,5 horas.
Uma demonstração pode ser vista em: https://www.youtube.com/shorts/KCNRaKu_uFA

Desenvolvido por Gabriel Romio

========================================

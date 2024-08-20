import gymnasium as gym
import numpy as np
from stable_baselines3 import DDPG, HerReplayBuffer
from stable_baselines3.common.vec_env import DummyVecEnv, SubprocVecEnv
from stable_baselines3.common.env_util import make_vec_env
from stable_baselines3.common.utils import set_random_seed

#Create a new environment
def make_env(env_id: str, rank: int, seed: int = 0):
    def _init():
        env = gym.make(env_id, render_mode="rgb_array")
        env.reset(seed=seed + rank)
        return env
    set_random_seed(seed)
    return _init

if __name__ == "__main__":
    env_id = "FetchPickAndPlace-v2"
    num_cpu = 12  #Number of processes to use

    #Create the vectorized environment
    vec_env = SubprocVecEnv([make_env(env_id, i) for i in range(num_cpu)])
    
    #Start the trein
    #model = DDPG(policy="MultiInputPolicy", env=vec_env, replay_buffer_class=HerReplayBuffer, verbose=1)
    model = DDPG( #Train a model with DDPG
        "MultiInputPolicy",
        vec_env,
        verbose=1,
        replay_buffer_class=HerReplayBuffer, #Adds HER to training
        learning_starts=1000,
    )
    #Load and continue the training of a model
    #model = DDPG.load("DDPG_FetchPickAndPlace", env=vec_env) #Loads an already trained model
    #model.learn(total_timesteps=15000_000, progress_bar=True) #Continue model training
    model.save("DDPG_FetchPickAndPlace") #Save the model

    #Shows the trained model in an enviroment
    vec_env = model.get_env()
    obs = vec_env.reset()
    while 1:
        action, _states = model.predict(obs, deterministic=True)
        obs, rewards, dones, info = vec_env.step(action)
        vec_env.render("human")


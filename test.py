import gym
from TD3 import TD3

def test():
    env_name = "BipedalWalker-v2"
    random_seed = 0
    n_episodes = 3
    max_timesteps = 2000
    render = True
    
    filename = "TD3_{}_{}".format(env_name, random_seed)
    filename += '_solved'
    directory = "./preTrained/{}/ONE".format(env_name)
    
    env = gym.make(env_name)
    state_dim = env.observation_space.shape[0]
    action_dim = env.action_space.shape[0]
    max_action = float(env.action_space.high[0])
    
    policy = TD3(state_dim, action_dim, max_action)
    
    policy.load_actor(directory, filename)
    
    for ep in range(1, n_episodes+1):
        ep_reward = 0
        state = env.reset()
        for t in range(max_timesteps):
            action = policy.select_action(state)
            state, reward, done, _ = env.step(action)
            ep_reward += reward
            if render:
                env.render()
            if done:
                print(t)
                break
            
        print('Episode: {}\tReward: {}'.format(ep, int(ep_reward)))
        ep_reward = 0
        env.close()        
                
if __name__ == '__main__':
    test()
    
    
    
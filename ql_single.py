import os
import sys
from datetime import datetime
import traci
from sumo_rl import SumoEnvironment
from sumo_rl.agents import QLAgent
from sumo_rl.exploration import EpsilonGreedy

if 'SUMO_HOME' in os.environ:
    tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
    sys.path.append(tools)
else:
    sys.exit("Please declare the environment variable 'SUMO_HOME'")


if __name__ == '__main__':
    learning_rate = 0.1
    discount_factor = 0.99
    max_eps = 0.05
    min_eps = 0.005
    decay_rate = 0.995
    episode = 1
    experiment_time = str(datetime.now()).split('_')[0]
    output = 'output.csv'

    environment = SumoEnvironment(net_file='Kilis_static.net.xml',
                                route_file='episode_routes.rou.xml',
                                out_csv_name=output,use_gui=True,
                                num_seconds=76000,min_green=8,max_green=50)
    
    for eps in range(1,episode+1):
        beginning_state = environment.reset()
        agent = {ts: QLAgent(starting_state=environment.encode(beginning_state[ts],ts),
                            state_space=environment.observation_space,
                            action_space=environment.action_space,
                            alpha=learning_rate,
                            gamma=discount_factor,
                            exploration_strategy=EpsilonGreedy(initial_epsilon=max_eps, min_epsilon=min_eps, decay=decay_rate)) for ts in environment.ts_ids}
        
        done = {'__all__': False}
        while not done['__all__']:
            actions = {ts: agent[ts].act() for ts in agent.keys()}

            state, reward, done, _ = environment.step(action=actions)
            for agent_id in agent.keys():
                    agent[agent_id].learn(next_state=environment.encode(state[agent_id], agent_id), reward=reward[agent_id])
        environment.save_csv(output,eps)
        environment.close()

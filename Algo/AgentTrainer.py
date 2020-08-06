from tensorflow.keras.optimizers import Adam
from algo.DDQNAgent import DDQNAgent
from algo.ExpirienceReplay import ExpirienceReplay
from HexEnv import HexEnv
import numpy as np


class AgentTrainer():

    BATCH_SIZE = 32

    def __init__(self, agent, environment):
        self.agent = agent
        self.environment = environment

    def _take_action(self, action):
        next_observation, reward, terminated = self.environment.step(action)
        # next_observation = next_observation if not terminated else None //todo: PROBLEM
        reward = np.random.normal(reward, 1) #todo: reward change
        return next_observation, reward, terminated

    def _print_epoch_values(self, episode, total_epoch_reward, average_loss):
        print("**********************************")
        print(f"Episode: {episode} - Reward: {total_epoch_reward} - Average Loss: {average_loss:.3f}")

    def train(self, num_of_episodes=1000):
        total_time_steps = 0

        for episode in range(0, num_of_episodes):

            # Reset the environment
            observation = self.environment.reset()

            # Initialize variables
            average_loss_per_episode = []
            average_loss = 0
            total_epoch_reward = 0

            terminated = False

            while not terminated:

                # Run Action
                action = self.agent.act(observation)

                # Take action
                next_observation, reward, terminated = self._take_action(action)
                self.agent.store(observation, action, reward, next_observation, terminated)

                loss = self.agent.train(AgentTrainer.BATCH_SIZE)
                average_loss += loss

                self.agent.align_epsilon(total_time_steps)
                total_time_steps += 1

                if terminated:
                    average_loss /= total_epoch_reward
                    average_loss_per_episode.append(average_loss)
                    self._print_epoch_values(episode, total_epoch_reward, average_loss)

                # Real Reward is always 1 for Cart-Pole environment
                total_epoch_reward += reward
                observation = next_observation


if __name__ == '__main__':
    environment = HexEnv.create_new(8, True, True, None, verbose=False)
    optimizer = Adam()
    experience_replay = ExpirienceReplay(50000)
    agent = DDQNAgent(experience_replay, state_shape=(8, 8), actions_size= 8*8, batch_size=32, optimizer = optimizer)
    agent_trainer = AgentTrainer(agent, environment)
    agent_trainer.train()
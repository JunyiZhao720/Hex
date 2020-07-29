import numpy as np

class AgentTrainer():
    def __init__(self, agent, enviroment):
        self.agent = agent
        self.enviroment = enviroment

    def _take_action(self, action):
        next_state, reward, terminated, _ = self.enviroment.step(action)
        next_state = next_state if not terminated else None
        reward = np.random.normal(1.0, REWARD_STD)
        return next_state, reward, terminated

    def _print_epoch_values(self, episode, total_epoch_reward, average_loss):
        print("**********************************")
        print(f"Episode: {episode} - Reward: {total_epoch_reward} - Average Loss: {average_loss:.3f}")

    def train(self, num_of_episodes=1000):
        total_timesteps = 0

        for episode in range(0, num_of_episodes):

            # Reset the enviroment
            state = self.enviroment.reset()

            # Initialize variables
            average_loss_per_episode = []
            average_loss = 0
            total_epoch_reward = 0

            terminated = False

            while not terminated:

                # Run Action
                action = agent.act(state)

                # Take action
                next_state, reward, terminated = self._take_action(action)
                agent.store(state, action, reward, next_state, terminated)

                loss = agent.train(BATCH_SIZE)
                average_loss += loss

                state = next_state
                agent.align_epsilon(total_timesteps)
                total_timesteps += 1

                if terminated:
                    average_loss /= total_epoch_reward
                    average_loss_per_episode.append(average_loss)
                    self._print_epoch_values(episode, total_epoch_reward, average_loss)

                # Real Reward is always 1 for Cart-Pole enviroment
                total_epoch_reward += 1
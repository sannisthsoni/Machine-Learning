# !/usr/bin/python
#From https://www.youtube.com/watch?v=mGYU5t8MO7s

import gym
import universe

env = gym.make('flashgames.CoasterRacer-v0')
observation_n = env.reset()

while True:
    action_n = [[('KeyEvent','ArrowUp',True)] for ob in observation_n]
    obervation_n, reward_n, done_n, info = env.step(action_n)
    env.render()


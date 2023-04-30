# -*- coding: utf-8 -*-
"""
Created on Thu Aug 4 22:01:48 2022

@author: Cristoforo Grasso
"""

#https://github.com/DMells/DiceGame/blob/main/dicegame.ipynb

import numpy as np
from dice_game import DiceGame
from abc import ABC, abstractmethod


"""
This code defines an abstract base class called DiceGameAgent that inherits from the ABC class, 
which stands for Abstract Base Class. The DiceGameAgent class has one constructor method __init__ that takes 
one argument game, and one abstract method play that takes one argument state.
The purpose of an abstract base class is to define a common interface that its subclasses must implement.
In this case, any subclass of DiceGameAgent must implement a play method that takes a state argument. 
The play method is left unimplemented in the DiceGameAgent 
class using the pass statement, indicating that it is up to the subclasses to implement this method.

"""


class DiceGameAgent(ABC):
    def __init__(self, game):
        self.game = game
    
    @abstractmethod
    def play(self, state):
        pass




class MyAgent(DiceGameAgent):
    def __init__(self, game):
        """
        The initial constructor for the MyAgent class.
        Upon intialisation calculates self.Values, the dictionary containing all 
        possible states as keys and the best expected reward & optimal policy as values
        
        param/attribute game: the dice game object

        attribute theta: the convergence threshold
        attribute V: the state:[expected_reward, optimal policy] dictionary
        """
        super().__init__(game)
        self.num_actions = len(self.game.actions)
        self.Values = self.solve()

    
    def expected_rewards(self, Values, state):
        """
        Given a current state, iterates over every possible action and every possible next state to
        calculate the Bellman update (the expected reward associated with choosing that action).
        
        The expected reward is the sum of the reward of the current state plus the expected reward of
        the next state,
        
        param V: the (either converged or unconverged) dictionary of states: [expected rewards, optimal policy]
        param state: the current state of the game
        
        returns A: an dictionary of actions containing the expected rewards of taking that action
        
        """
        Actions = {a:0 for a in self.game.actions}

        # For each possible action
        for a in Actions.keys():
            
            # Get the possible next_states, game_over, reward and probabilities of the next state occurring
            next_states, game_over, reward, probabilities = self.game.get_next_states(a, state)
            
            # For each next_state and associated probability of that action & given state
            for next_state, probability in zip(next_states, probabilities): 
                # If there is a next_state
                if not game_over:
                    # Calculate Bellman Update
                    Actions[a] += probability * (reward+Values[next_state][0])
                else:
                    # next_state = None
                    Actions[a] += probability * reward
        return Actions


    def solve(self, theta = 0.1):
        """
        The core function to perform value iteration.
        
        Loops until the difference between the expected reward for each iteration and the 
        previous run-through for that state is less than self.theta i.e. convergence.
        
        returns V : the converged dictionary of states:[expected maximum reward, optimal policy]
        """
        
        # Initialise dictionary with each state as keys and values [expected reward, optimal policy]
        Values = {i: [0, None] for i in self.game.states}
        
        # Loop until delta < self.theta
        while True:
            delta = 0
    
            # For each state
            for s in self.game.states:
                # Get the list of reward values pertaining to each action given that state
                A = self.expected_rewards(Values, s)
                
                # Take the highest expected reward value 
                best_action_value = max(A.values())
                
                # Update delta with either delta or the absolute difference between the 
                # new maximum value for that state and the previous maximum value for that state
                delta = max(delta, np.abs(best_action_value - Values[s][0]))
                
                # Update the maximum value and optimal policy for that state   
                Values[s] = [best_action_value,max(A, key = A.get)]
                
            # If the change is less than self.theta, end the loop
            if delta < theta:
                break
        return Values

        
    def play(self, state):
        """
        For the given state, obtains the optimal policy
        
        param state : the current state of the game
        
        returns self.Values[state][1] : the optimal action associated with that state
        """

        return self.Values[state][1]


game = DiceGame()
agent = MyAgent(game)
policy  = agent.solve()


state = game.reset()


import statistics

data = []
for v in policy.values():
    print(v[0])
    data.append(float(v[0]))
    average = statistics.mean(data)

print(f"\n{average}")
        
# There should be exactly 56 states
assert(len(policy.items()) == 56)

# The optimal move when you roll three 1s is to stick
assert(policy[(1, 1, 1)][1] == (0, 1, 2))

# The optimal move when you roll three 4s is to reroll all 3
assert(policy[(4, 4, 4)][1] == ())

print("All three tests pass.")

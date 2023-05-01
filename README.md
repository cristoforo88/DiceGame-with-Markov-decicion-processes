# DiceGame with Markov Decicion Processes

Dice Game with Value Iteration Algorithm
This repository contains a Python implementation of the value iteration algorithm for a simple dice game. The goal of the game is to roll a six-sided die and reach the final state with the highest possible score. The game consists of 10 states, where each state represents the score obtained so far. The game ends when the final state (score of 10) is reached.

**Markov decision process (MDP) using value iteration**

Initialize array V arbitrarily (e.g., V 
s
​
 =0 for all s∈S 
+
 )
Repeat
Set Δ=0
For each s∈S do
Set v=V(s)
V(s)= 
a∈A
max
​
  
s 
′
 ∈S
∑
​
 p(s 
′
 ∣s,a)[r(s,a,s 
′
 )+γV(s 
′
 )]
Set Δ=max(Δ,∣v−V(s)∣)
Until Δ<ϵ (a small positive number)
Output a deterministic policy, π, such that
π(s)=argmax 
a∈A
​
  
s 
′
 ∈S
∑
​
 p(s 
′
 ∣s,a)[r(s,a,s 
′
 )+γV(s 
′
 )]

In this expression, $V$ represents the value function, $s$ represents a state, $a$ represents an action, $p(s'|s,a)$ represents the probability of transitioning to state $s'$ from state $s$ with action $a$, $r(s,a,s')$ represents the reward obtained by transitioning from state $s$ to state $s'$ with action $a$, $\gamma$ represents the discount factor, $\epsilon$ represents a small positive number, and $\pi$ represents the policy.



**Getting Started**

To run the program, you will need to have Python 3 installed on your system. You can download Python from the official website: https://www.python.org/downloads/

Clone the repository to your local machine using the following command:

 ```
git clone https://github.com/your-username/dice-game-value-iteration.git
 ```

Once you have cloned the repository, navigate to the project directory:

 ```
cd dice-game-value-iteration
 ```
 
Install the required Python packages by running the following command:

 ```
pip install -r requirements.txt
 ```

This will install the necessary packages for running the program.

**Usage**

To run the program, simply execute the following command:


python main.py
This will run the value iteration algorithm and output the optimal policy for the dice game. The output will show the optimal action to take in each state, along with the corresponding expected reward.

**References**

This implementation is based on the value iteration algorithm for Markov decision processes (MDPs). For more information on MDPs and value iteration, see the following resources:

Sutton, R. S., & Barto, A. G. (2018). Reinforcement learning: An introduction. MIT press.

Puterman, M. L. (1994). Markov decision processes: discrete stochastic dynamic programming. John Wiley & Sons.


**License**


**Acknowledgments**





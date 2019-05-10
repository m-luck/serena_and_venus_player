# def L2dist(POINT, a, b, c):
import random
import numpy as np
import sys

states = {
    "(C,C)": (30,70), 
    "(C,N)": (80,20),
    "(N,C)": (90,10),
    "(N,N)": (20,80)
    }

# states = {
#     "(C,C)": (50,50), 
#     "(C,N)": (10,90), 
#     "(N,C)": (20,80), 
#     "(N,N)": (80,20)
#     }

total_value = [0.0,0.0]
current_value = [0.0,0.0]
trial_counter = [0,0]
alpha = 1
beta = 0

def ourChoice():
    outcome = np.random.choice(
    ['C', 'N'], 
    1,
    p=[alpha, beta]
    )[0]
    return outcome

def rationalAgentChoice():
    outcome = np.random.choice(
    ['C', 'N'], 
    1,
    p=[0.6, 0.4]
    )[0]
    return outcome

def run_trial():
    agent_choice = ourChoice()
    other_choice = rationalAgentChoice()
    full_outcome = "({AGENT},{OTHER})".format(AGENT=agent_choice, OTHER=other_choice)
    value = states[full_outcome][0] 
    if agent_choice == "C": 
        total_value[0] += value
        trial_counter[0] += 1
        current_value[0] = total_value[0]/trial_counter[0]
    else:
        total_value[1] += value
        trial_counter[1] += 1
        current_value[1] = total_value[1]/trial_counter[1]
    return total_value, current_value, trial_counter

def run(NTRIALS):
    for i in range(0,NTRIALS):
        total_value, current_value, trial_counter = run_trial()
    return current_value, total_value, trial_counter

NTRIALS = int(sys.argv[1])
res = 0
old_res = -1
while res > old_res and alpha > 0:
    values, total, trials = run(NTRIALS)
    if float(values[0]) - float(values[1]) > 1:
        print(values)
        print("C") 
    elif float(values[1]) - float(values[0]) > 1:
        print(values)
        print("N")
    else:
        print(values)
        print("C or N are alright")
    alphaC = alpha * float(values[0])
    betaN = beta * float(values[1])
    print(alphaC,"+" ,betaN,"=",alphaC + betaN)
    print(total, trials)
    old_res = res
    res = alphaC + betaN
    alpha -= 0.1 
    beta += 0.1
    print("AB:",alpha, beta)
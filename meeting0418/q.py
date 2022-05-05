import math
import random

ALPHA = 0.1 # learning rate
GAMMA = 0.9
EPSILON = 0.8 # randomize value
LEVEL = 3
GOAL_POSITION = 14
THRESHOLD = 100

def select_a(previous_position, q_value):
    """
    Select activity
    """
    if random.random() < EPSILON:
        if random.randint(0, 1) == 0:
            return 2 * previous_position + 1
    else:
        if q_value[2 * previous_position + 1] > q_value[2 * previous_position + 2]:
            return 2 * previous_position + 1
    return 2 * previous_position + 2

def update_q(position, q_value):
    """
    Calculate updated Q Value
    """
    if position < 2 ** LEVEL - 1:
        # if not in last level
        qmax = max(
            q_value[2 * position + 1],
            q_value[2 * position + 2])
        return q_value[position] + int(
            ALPHA * (GAMMA * qmax - q_value[position]))

    # if in last level
    if position == GOAL_POSITION:
        return q_value[position] + int(
            ALPHA * (1000 - q_value[position]))
    #elif position == 11:
    #    return q_value[position] + int(
    #        ALPHA * (500 - q_value[position]))
    return q_value[position]

def solve(seed, time):
    random.seed(seed)
    q_value = [
        random.randint(0, 100) for i in
            range(2 ** (LEVEL + 1) - 1)
    ]

    convergence_time = 0
    eq_count = 0
    print(q_value)
    for i in range(time):
        previous_q_value = q_value
        position = 0  # initial state
        for j in range(3):
            position = select_a(position, q_value)
            q_value[position] = update_q(position, q_value)
        print(q_value)

        if q_value == previous_q_value:
            if convergence_time == 0:
                convergence_time = i
            eq_count += 1
            if eq_count > THRESHOLD:
                print(convergence_time)
                break
        else:
            eq_count = 0
            convergence_time = 0

if __name__ == "__main__":
    solve(32767, 1000)
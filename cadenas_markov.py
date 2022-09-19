import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
p_init = np.array([0.1, 0.8, 0.1])
p_transition_example = np.array(
    [[0.6,  0.2, 0.2],
    [0.05, 0.9, 0.05],
    [0.1,  0.2, 0.7]])

p_state_t = [p_init]
for i in range(200):
    p_state_t.append(p_state_t[-1] @ p_transition_example)

state_distributions = pd.DataFrame(p_state_t)
print(state_distributions)

print(plt.plot(state_distributions))
import matplotlib.pyplot as plt
import numpy as np
import yaml

from src.simulation import Simulation

# Load config
with open("config/parameters.yaml", "r") as f:
    config = yaml.safe_load(f)

# Run simulation
sim = Simulation(config)
sim.run()

# Plot opinion variance over time
variances = [np.var(step) for step in sim.history]

plt.plot(variances)
plt.xlabel("Time step")
plt.ylabel("Opinion variance")
plt.title("Consensus formation")
plt.show()

# Print final opinions
final_opinions = sim.history[-1]
print("Final opinions:")
print(final_opinions)

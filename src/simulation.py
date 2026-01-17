import random
import numpy as np

class Simulation:
  def __init__(self, config):
    self.config = config,
    self.agents = {},
    self.network = None,
    self.history = []
    
    random.seed(config["simulation"]["random_seed"])
    np.random.seed(config["simulation"]["random_seed"])
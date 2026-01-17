import random
import numpy as np
import networkx as nx

from src.agent import Agent
class Simulation:
  def __init__(self, config):
    self.config = config,
    self.agents = {},
    self.network = None,
    self.history = []
    
    random.seed(config["simulation"]["random_seed"])
    np.random.seed(config["simulation"]["random_seed"])
    
    self._initialize_agents()
    self._initialize_network()
    
  def _initialize_agents(self):
    agent_config = self.config["agents"]  
    num_agents = self.config["network"]["num_agents"]
      
    for i in range(num_agents):
      opinion = random.uniform(
        agent_config["opinion"]["min"],
        agent_config["opinion"]["max"]
      )
      confidence = random.uniform(
        agent_config["confidence"]["min"],
        agent_config["confidence"]["max"]
      )
      open_mindedness = random.uniform(
        agent_config["open_mindedness"]["min"],
        agent_config["open_mindedness"]["max"]
      )
      stubbornness = random.uniform(
        agent_config["stubbornness"]["min"],
        agent_config["stubbornness"]["max"]
      )
        
      self.agents[i] = Agent(i, opinion, confidence, open_mindedness, stubbornness)
      
  def _initialize_network(self):
    network_config = self.config["network"]
    self.network = nx.watts_strogatz_graph(
      network_config["num_agents"],
      network_config["average_degree"],
      network_config["rewiring_probability"]
    )
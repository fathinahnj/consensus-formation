import random
import numpy as np
import networkx as nx

from src.agent import Agent
class Simulation:
  def __init__(self, config):
    self.config = config
    self.agents = {}
    self.network = None
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
    
  def step(self):
    update_config = self.config["update_rule"]
    noise_config = self.config["emotional_noise"]
    
    for i, j in self.network.edges():
      agent_i = self.agents[i]
      agent_j = self.agents[j]
      
      if agent_i.can_interact(agent_j, update_config["bounded_confidence"]):
        noise = 0.0
        if noise_config["enabled"]:
          noise = np.random.normal(0, noise_config["sigma"])
          
        agent_i.update_opinion(
          agent_j.opinion,
          update_config["learning_rate"],
          noise
        ) 
        
  def record_state(self):
    opinions = [agent.opinion for agent in self.agents.values()]
    self.history.append(opinions)
    
  def global_variance(self):
    """
    To calculate the global variance of opinions in the network (consensus / polarization measure)
    Returns:
        : variance of opinions (float)
    """
    opinions = [agent.opinion for agent in self.agents.values()]
    return np.var(opinions)  
  
  def run(self):
    max_steps = self.config["simulation"]["max_steps"]
    threshold = self.config["simulation"]["convergence_threshold"]
    
    for step in range(max_steps):
      self.step()
      self.record_state()
      
      if self.global_variance() < threshold:
        print(f"Converged at step {step}.")
        break
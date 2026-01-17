class Agent: 
  def __init__(self, agent_id, opinion, confidence, open_mindedness, stubbornness):
    self.id = agent_id,
    self.opinion = opinion,
    self.confidence = confidence, # for dynamic threshold
    self.open_mindedness = open_mindedness,
    self.stubbornness = stubbornness
    
    
  def can_interact(self, other, confidence_threshold):
    '''
    Docstring for can_interact
    
    :param self: agent
    :param other: other agent
    :param confidence_threshold: implementation of bounded confidence rule (Deffuant / Hegselmann–Krause)
    :return: boolean indicating if interaction is possible (if opinion is not too different)       
    '''
    return abs(self.opinion - other.opinion) <= confidence_threshold
    
  def update_opinion(self, other_opinion, learning_rate, noise=0.0):
    '''
    Docstring for update_opinion
    
    :param self: agent
    :param other_opinion: opinion of the other agent
    :param learning_rate: rate at which the agent learns from others' opinions
    :param noise: set to 0.0 by default, other influence on opinion change (emotion, deliberation disturbance, etc.)
    :return: change in opinion
    '''
    delta = learning_rate * (other_opinion - self.opinion) # base change in opinion
    delta *= self.open_mindedness           # faster change for open-minded agents
    delta *= (1 - self.stubbornness)        # slower change for stubborn agents
    
    self.opinion += delta + noise
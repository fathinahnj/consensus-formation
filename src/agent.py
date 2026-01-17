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
    
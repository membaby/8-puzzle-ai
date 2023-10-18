from algorithms.utils import get_neighbors
from collections import deque
from collections import ChainMap

class BFS:
    def __init__(self, initial_state, goal_state):
        self.goal_state = goal_state
        self.frontier = deque([initial_state])
        self.explored = set()
        self.frontier_U_explored = set()
        self.parent_map={initial_state:initial_state} #dictionary
        

    def run_algorithm(self) ->bool :
        while len(self.frontier)!=0:
            curr= self.frontier.popleft()
            self.explored.add(curr)
            self.frontier_U_explored.add(curr)

            if curr== self.goal_state:
                return True,self.parent_map
            
            for neighbor in get_neighbors(curr):
                 if neighbor not in self.frontier_U_explored:
                     self.frontier.append(neighbor)
                     self.frontier_U_explored.add(neighbor)
                     self.parent_map[neighbor]=curr
        return False



        
from time import clock
from collections import deque
from State import State

goalTest = [[0,1,2],[3,4,5],[6,7,8]]

class Solver:

	
	def __init__(self,initialState):
		self.initialState = initialState
		self.explored = set()
		self.depth = 0
		


	def solve(self):
		before = clock()
		frontier = deque([self.initialState])
		self.explored.add(self.initialState.id)
		while frontier:
			frontier = deque(sorted(list(frontier), key=lambda state: state.getFManhattan()))
			state = frontier.popleft()
			if (state.board == goalTest):
				self.finalState = state
				self.runningTime = clock() - before
				return True
			for neighbor in state.neighbors():
				if not ((neighbor.id in self.explored)):
					self.explored.add(neighbor.id)
					frontier.append(neighbor)
					if neighbor.depth > self.depth:
						self.depth = neighbor.depth
		self.runningTime = clock() - before
		return False


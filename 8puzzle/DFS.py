from time import clock
from State import State
from Solver import Solver

goalTest = [[0,1,2],[3,4,5],[6,7,8]]

class DFS(Solver):

	def solve(self):
		before = clock()
		frontier = [self.initialState]
		self.explored.add(self.initialState.id)
		while frontier:
			state = frontier.pop()
			state.getFManhattan()
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



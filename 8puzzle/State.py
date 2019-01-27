from math import sqrt
from math import pow
class State:
	
	def __init__(self,board,direction,parent=None):
		self.board = board;
		self.id = ''.join(map(str, board))
		self.parent = parent
		if (self.parent != None):
			self.g = parent.f
			self.depth = parent.depth + 1
			self.direction = direction
		else:
			self.g = 0
			self.depth = 0
			self.direction = ''



	def getFManhattan(self):
		h = 0
		for current_x in range(0,3):
			for current_y in range(0,3):
				if self.board[current_x][current_y] != 0:
					goal_x , goal_y = divmod(self.board[current_x][current_y],3)
					h += abs(current_x - goal_x) + abs(current_y - goal_y)
		self.f = h + self.g
		return self.f

	def getFEuclidean(self):
		h = 0
		for current_x in range(0,3):
			for current_y in range(0,3):
				if self.board[current_x][current_y] != 0:
					goal_x , goal_y = divmod(self.board[current_x][current_y],3)
					h += sqrt(pow(current_x - goal_x,2) + pow(current_y - goal_y,2))
		self.f = h + self.g
		return self.f


	def getPath(self):
		state, path = self, []
		while state:
			path.append(state)
			state = state.parent
		return list(reversed(path))


	def copy(self):
		newBoard = []
		for i in range(0,3):
			row = []
			for j in range(0,3):
				row.append(self.board[i][j])
			newBoard.append(row)
		return newBoard


	def position(self,number):
		for i in range(0,3):
			for j in range(0,3):
				if self.board[i][j] == number:
					return [i,j]
		return [0,0]

	def neighbors(self):
		i,j = map(int,self.position(0))
		nb = []

		#left
		if(j > 0):
			left = self.copy()
			left[i][j],left[i][j-1]= left[i][j-1],left[i][j]
			nb.append(State(left,'left',self))

		#up
		if(i > 0):
			up = self.copy()
			up[i][j],up[i-1][j]= up[i-1][j],up[i][j]
			nb.append(State(up,'up',self))


		#right
		if(j < 2):
			right = self.copy()
			right[i][j],right[i][j+1]= right[i][j+1],right[i][j]
			nb.append(State(right,'right',self))


		#down
		if(i < 2):
			down = self.copy()
			down[i][j],down[i+1][j]= down[i+1][j],down[i][j]
			nb.append(State(down,'down',self))

		return nb

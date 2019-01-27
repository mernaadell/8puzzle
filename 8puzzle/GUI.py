from Tkinter import *
from Solver import Solver
from State import State
from Euclidean import Euclidean
from DFS import DFS
from BFS import BFS


class GUI:
	
	def __init__(self,board):
		self.mainFrame = Tk()
		self.mainFrame.title("8 Puzzle")
		Grid.rowconfigure(self.mainFrame, 0, weight=1)
		Grid.columnconfigure(self.mainFrame, 0, weight=1)
		self.boardFrame = Frame(self.mainFrame,bg = "white")
		self.board = board
		self.labels = [[0 for x in range(3)] for y in range(3)]
		for i in range(0,3):
			Grid.rowconfigure(self.boardFrame, i, weight=1)
			for j in range(0,3):
				Grid.columnconfigure(self.boardFrame, j, weight=1)
				if not (i == 0 and j == 0):
					self.labels[i][j] = Label(self.boardFrame,text=str(i*3+j),font=('Times 26 bold'),height = 4 , width = 13,bg='#444488',fg='white')
		self.BottomFrame = Frame(self.mainFrame,bg = "white")
		self.labelsFrame = Frame(self.BottomFrame,bg = "white")
		self.ButtonsFrame = Frame(self.BottomFrame,bg = "gray")
		Grid.rowconfigure(self.BottomFrame, 0, weight=1)
		Grid.columnconfigure(self.BottomFrame, 0, weight=1)
		
		self.loadingLabel = Label(self.labelsFrame,text='Choose searching technic:',bg='white',fg='#888888')
		self.loadingLabel.pack()	
	
		self.labelsFrame.grid(row=0,column=0,sticky="nsew")
		self.ButtonsFrame.grid(row=1,column=0,sticky="nsew")

		self.buttons = []
		for i in range(0,4):
			button = Button(self.ButtonsFrame,bg='white',fg='#444488',font=('Times 18 bold'))
			self.buttons.append(button) 
			self.buttons[i].pack(side=LEFT,expand=YES,fill=BOTH)

		initialState = State(self.board,'',None)

		self.buttons[0].config(text=' DFS ',command =lambda: self.solveButtonAction(DFS(initialState)))
		self.buttons[1].config(text=' BFS ',command =lambda: self.solveButtonAction(BFS(initialState)))
		self.buttons[2].config(text='A* (Euclidean)',command =lambda: self.solveButtonAction(Euclidean(initialState)))
		self.buttons[3].config(text='A* (Manhattan)',command =lambda: self.solveButtonAction(Solver(initialState)))



	def display(self):
		for i in range(0,3):
			for j in range(0,3):
				if (self.board[i][j] != 0):
					x,y = divmod(self.board[i][j],3)
					self.labels[x][y].grid(row=i,column=j,sticky="nsew")



	def solveButtonAction(self,solver):
		self.loadingLabel.config(text = 'Loading...')
		self.solver = solver
		self.solver.solve()
		self.solutionPath = self.solver.finalState.getPath()
		self.noOfSteps = len(self.solutionPath)-1
		self.currentStep = 0
		

		output = open("output.txt", "w")
		for state in self.solutionPath:
			output.write(state.direction+',')
		output.write('\n\ncost of the path: {}'.format(solver.finalState.f))
		output.write(str(len(self.solver.explored)))
		output.write('\nsearch depth: {}'.format(solver.depth))
		output.write('\nrunning time: {}'.format(solver.runningTime)) 

		for i in range(0,4):
			self.buttons[i].destroy()
		self.loadingLabel.destroy()

		costLabel = Label(self.labelsFrame,text='cost of the path: {}'.format(solver.finalState.f),bg='white',fg='#888888')
		depthLabel = Label(self.labelsFrame,text='    search depth: {}'.format(solver.depth),bg='white',fg='#888888')
		timeLabel = Label(self.labelsFrame,text='     running time: {}'.format(solver.runningTime) + ' seconds',bg='white',fg='#888888')

		self.stepsLabel = Label(self.labelsFrame,text='STEP: {}/{}'.format(self.currentStep,self.noOfSteps),bg='white',fg='#444488')

		costLabel.pack(side=LEFT)
		depthLabel.pack(side=LEFT)
		timeLabel.pack(side=LEFT)
		self.stepsLabel.pack(side=RIGHT)	
		
		self.nextButton = Button(self.ButtonsFrame,bg='white',fg='#444488',text=' Next >>',font=('Times 18 bold'),command =lambda:self.nextButtonAction())
		self.previousButton = Button(self.ButtonsFrame,bg='white',fg='#444488',text='<< Previous ',font=('Times 18 bold'),state=DISABLED,command =lambda:self.previousButtonAction())
		self.endButton = Button(self.ButtonsFrame,bg='white',fg='#444488',text=' END ',font=('Times 18 bold'),command =lambda:self.endButtonAction())
		self.beginButton = Button(self.ButtonsFrame,bg='white',fg='#444488',text=' BEGINNING ',font=('Times 18 bold'),state=DISABLED,command =lambda:self.beginButtonAction())
		self.nextButton.pack(side=RIGHT)
		self.previousButton.pack(side=RIGHT)	
		self.beginButton.pack(side=LEFT)
		self.endButton.pack(side=LEFT)


	def nextButtonAction(self):
			self.currentStep += 1
			self.stepsLabel.config(text = 'STEP: {}/{}'.format(self.currentStep,self.noOfSteps))
			if self.currentStep == self.noOfSteps:
				self.nextButton.config(state=DISABLED)
				self.endButton.config(state=DISABLED)
			self.board = self.solutionPath[self.currentStep].board
			self.display()
			if self.currentStep > 0:
				 self.beginButton.config(state="normal")
				 self.previousButton.config(state="normal")

	def previousButtonAction(self):
			self.currentStep -= 1
			self.stepsLabel.config(text = 'STEP: {}/{}'.format(self.currentStep,self.noOfSteps))
			if self.currentStep == 0:
				self.previousButton.config(state=DISABLED)
				self.beginButton.config(state=DISABLED)
			self.board = self.solutionPath[self.currentStep].board
			self.display()
			if self.currentStep < self.noOfSteps:
				 self.endButton.config(state="normal")
				 self.nextButton.config(state="normal")

	def beginButtonAction(self):
			self.currentStep = 0
			self.stepsLabel.config(text = 'STEP: {}/{}'.format(self.currentStep,self.noOfSteps))
			self.board = self.solutionPath[self.currentStep].board
			self.display()
			self.beginButton.config(state=DISABLED)
			self.previousButton.config(state=DISABLED)
			self.endButton.config(state="normal")
			self.nextButton.config(state="normal")

	def endButtonAction(self):
			self.currentStep = self.noOfSteps
			self.stepsLabel.config(text = 'STEP: {}/{}'.format(self.currentStep,self.noOfSteps))
			self.board = self.solutionPath[self.currentStep].board
			self.display()
			self.endButton.config(state=DISABLED)
			self.nextButton.config(state=DISABLED)
			self.beginButton.config(state="normal")
			self.previousButton.config(state="normal")

	def run(self):
		self.display()
		self.boardFrame.grid(row=0,column=0,sticky="nsew")
		self.BottomFrame.grid(row=1,column=0,sticky="nsew")
		self.mainFrame.mainloop()

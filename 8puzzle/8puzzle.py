from Tkinter import*
from Solver import Solver
from State import State


def display(board,label):
	for i in range(0,3):
		for j in range(0,3):
				if (board[i][j] != 0):
					x,y = divmod(board[i][j],3)
					label[x][y].grid(row=i,column=j,sticky="nsew")
	


#start gui
tk = Tk()
tk.title("8 Puzzle")
Grid.rowconfigure(tk, 0, weight=1)
Grid.columnconfigure(tk, 0, weight=1)


#Board
boardFrame = Frame(tk,bg = "white")

board = [[1,2,5],[3,4,0],[6,7,8]]
initialState = State(board,'',None)
solver = Solver(initialState)

label = [[0 for x in range(3)] for y in range(3)]
for i in range(0,3):
	Grid.rowconfigure(boardFrame, i, weight=1)
	for j in range(0,3):
		Grid.columnconfigure(boardFrame, j, weight=1)
		if not (i == 0 and j == 0):
			label[i][j] = Label(boardFrame,text=str(i*3+j),font=('Times 26 bold'),height = 4 , width = 8,bg='#444488',fg='white')
display(board,label)

#BUTTONS
ButtonsFrame = Frame(tk,bg = "white")
buttons = []
for i in range(0,4):
	button = Button(ButtonsFrame,bg='white',fg='#444488')
	buttons.append(button) 
	buttons[i].pack(side=LEFT,expand=YES,fill=BOTH)	

def solveButtonAction(buttons):
	solver.solve()
	for i in range(0,4):
		buttons[i].destroy()
	#gui
	labelsFrame = Frame(ButtonsFrame,bg = "white")
	ButtonsFrame2 = Frame(ButtonsFrame,bg = "gray")

	Grid.rowconfigure(ButtonsFrame, 0, weight=1)
	Grid.columnconfigure(ButtonsFrame, 0, weight=1)
	
	costLabel = Label(labelsFrame,text='cost of the path: {}'.format(solver.finalState.f),bg='white',fg='#888888')
	depthLabel = Label(labelsFrame,text='    search depth: {}'.format(solver.depth),bg='white',fg='#888888')
	timeLabel = Label(labelsFrame,text='     running time: {}'.format(solver.runningTime) + ' seconds',bg='white',fg='#888888')
	
	costLabel.pack(side=LEFT)
	depthLabel.pack(side=LEFT)
	timeLabel.pack(side=LEFT)	
	
	nextButton = Button(ButtonsFrame2,bg='white',fg='#444488',text=' Next >>',font=('Times 18 bold'))
	previousButton = Button(ButtonsFrame2,bg='white',fg='#444488',text='<< Previous ',font=('Times 18 bold'))
	lastButton = Button(ButtonsFrame2,bg='white',fg='#444488',text=' last ',font=('Times 18 bold'))
	startButton = Button(ButtonsFrame2,bg='white',fg='#444488',text=' start ',font=('Times 18 bold'))
	nextButton.pack(side=RIGHT)
	previousButton.pack(side=RIGHT)	
	startButton.pack(side=LEFT)
	lastButton.pack(side=LEFT)

	labelsFrame.grid(row=0,column=0,sticky="nsew")
	ButtonsFrame2.grid(row=1,column=0,sticky="nsew")
	


buttons[0].config(text=' DFS ',command =lambda: solveButtonAction(buttons))
buttons[1].config(text=' BFS ',command =lambda: solveButtonAction(buttons))
buttons[2].config(text='A* (Euclidean)',command =lambda: solveButtonAction(buttons))
buttons[3].config(text='A* (Manhattan)',command =lambda: solveButtonAction(buttons))		


boardFrame.grid(row=0,column=0,sticky="nsew")
ButtonsFrame.grid(row=1,column=0,sticky="nsew")

tk.mainloop()

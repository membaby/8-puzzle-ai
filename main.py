from rich import print
from rich.table import Table
from solvers import Solver
from tkinter import * 
# from gui import Table

def print_puzzle(state, prev_state, title):
    table = Table(title=title)
    table.add_column("Parent", justify="center", style="cyan", no_wrap=True)
    table.add_column("Child", justify="center", style="magenta", no_wrap=True)
    for i in range(3):
        table.add_row(' '.join([str(x) for x in state[i]]), ' '.join([str(x) for x in prev_state[i]]))
    print(table)


def print_states(list_of_state):
    for i in range(0, len(list_of_state)):
        state = list_of_state[i]
        print(state[0], state[1], state[2])
        print(state[3], state[4], state[5])
        print(state[6], state[7], state[8])
        print("_____")
        print()


if __name__ == '__main__':
    # Stage 1: Algorithm Selection
    print('.:[ 8-Puzzle Solver ]:.')
    print('[ ] Please select an algorithm:')
    print('     [-] Uninformed Search Methods:')
    print('         [1] Depth-First Search')
    print('         [2] Breadth-First Search')
    print('     [-] Informed Search Methods:')
    print('         [3] A* Search - Manhattan Distance')
    print('         [4] A* Search - Euclidean Distance')

    while True:
        user_choice_algorithm = input('Your Choice: ')
        if user_choice_algorithm in ['1', '2', '3', '4']: break
        print('[!] Invalid choice.')

    # Stage 2: Initial State
    initial_state = ''
    print('[ ] Enter 8-Puzzle Initial State:')
    for i in range(3):
        row = input().replace(' ', '')

        # Invalid Input - Error Handler
        if len(row) != 3:
            print("I can't solve puzzles larger than 3x3.")
            exit()
        elif not all([x.isnumeric() for x in row]):
            print("I can't solve puzzles containing non-numeric values.")
            exit()

        initial_state += row
    initial_state += str(initial_state.index('0'))
    # initial_state example: 1234567808

    # Stage 3: Solvers
    goal_state = '0123456780'
    solver = Solver()
    solution, steps, cost_of_path, nodes_expanded, search_depth, running_time = solver.solve(user_choice_algorithm, initial_state, goal_state)
    # solution, running_time, list_of_states = solver.solve(user_choice_algorithm, initial_state, goal_state)
    # print('Solution:', solution)
    # print('Time:', running_time)
    # print('path to the goal:')
    # print_states(list_of_states)

    # Stage 4: Results
    print()
    print_states(steps)
    print()
    print('.:[ SOLUTION STATS ]:.')
    print('[ ] [bold]Cost of Path[/bold]:', cost_of_path)
    print('[ ] [bold]Nodes Expanded[/bold]:', nodes_expanded)
    print('[ ] [bold]Search Depth[/bold]:', search_depth)
    print('[ ] [bold]Running Time[/bold]:', running_time)
    print(steps[0])

   ##################################################GUI
    # create root window
    # root = Tk()
    # j=0
    # def draw(j):
    #     ls=steps[j]
    #     lst=[[ls[0],ls[1],ls[2]],[ls[3],ls[4],ls[5]],[ls[6],ls[7],ls[8]]]
    #     # code for creating table
    #     for i in range(3):
    #         for j in range(3):    
    #             e = Entry(root, width=10, fg='blue',
    #                             font=('Arial',16,'bold'))
                    
    #             e.grid(row=i, column=j)
    #             e.insert(END, lst[i][j])
    #     B1 = Button(text ="next",command=lambda:next())
    #     B1.place(x=50,y=100)
    #     B2 = Button(text ="back" )
    #     B2.place(x=200,y=100)
    # def next():
    #     global j
    #     j=j+1
        
    # draw(j)
    # root.mainloop()
    ############################################################
    root=Tk()
    j=0
    ls=steps[j]
    print(ls,"ss")
    

    b1=Button(root,text=ls[0],font=("Helvetica",20),height=3, width=6,bg="SystemButtonFace")
    b2=Button(root,text=ls[1],font=("Helvetica",20),height=3, width=6,bg="SystemButtonFace")
    b3=Button(root,text=ls[2],font=("Helvetica",20),height=3, width=6,bg="SystemButtonFace")
    b4=Button(root,text=ls[3],font=("Helvetica",20),height=3, width=6,bg="SystemButtonFace")
    b5=Button(root,text=ls[4],font=("Helvetica",20),height=3, width=6,bg="SystemButtonFace")
    b6=Button(root,text=ls[5],font=("Helvetica",20),height=3, width=6,bg="SystemButtonFace")
    b7=Button(root,text=ls[6],font=("Helvetica",20),height=3, width=6,bg="SystemButtonFace")
    b8=Button(root,text=ls[7],font=("Helvetica",20),height=3, width=6,bg="SystemButtonFace")
    b9=Button(root,text=ls[8],font=("Helvetica",20),height=3, width=6,bg="SystemButtonFace")

    
    
    b1.grid(row=0,column=0)
    b2.grid(row=0,column=1)
    b3.grid(row=0,column=2)
    b4.grid(row=1,column=0)
    b5.grid(row=1,column=1)
    b6.grid(row=1,column=2)
    b7.grid(row=2,column=0)
    b8.grid(row=2,column=1)
    b9.grid(row=2,column=2)

    def next_click():
        global j
        if j<=len(steps)-2:
            j=j+1
            ls=steps[j]
            b1["text"]=ls[0]
            b2["text"]=ls[1]
            b3["text"]=ls[2]
            b4["text"]=ls[3]
            b5["text"]=ls[4]
            b6["text"]=ls[5]
            b7["text"]=ls[6]
            b8["text"]=ls[7]
            b9["text"]=ls[8]
    
    def back_click():
      
        global j 
        if j>=1:
            j=j-1
            ls=steps[j]
            b1["text"]=ls[0]
            b2["text"]=ls[1]
            b3["text"]=ls[2]
            b4["text"]=ls[3]
            b5["text"]=ls[4]
            b6["text"]=ls[5]
            b7["text"]=ls[6]
            b8["text"]=ls[7]
            b9["text"]=ls[8]
     
    next_photo= PhotoImage(file='forward_button.png')
    back_photo= PhotoImage(file='back_button.png')
    B1 = Button(text ="next",image=next_photo,command=next_click,borderwidth=0)
    B1.place(x=50,y=400)
    B2 = Button(text ="back",image=back_photo,command=back_click ,borderwidth=0)
    B2.place(x=200,y=400)
    root.mainloop()
    
        
   

     

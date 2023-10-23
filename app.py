from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
import sys

from solvers import Solver

TITLE = '8 Puzzle AI Solver'

class Solver_GUI(QWidget):
    def __init__(self, parent=None):
        super(Solver_GUI, self).__init__(parent)
        self.steps = []
        self.steps_index = 0

        self.setFixedSize(315, 550)
        self.setWindowTitle(TITLE)

        grid = QGridLayout()
        self.setLayout(grid)

        # Dropdown Widgets
        self.cb_algorithm = QComboBox()
        self.cb_algorithm.addItems(['Select Algorithm', 'DFS', 'BFS', 'A* (Manhattan)', 'A* (Euclidean)'])

        # Button Widgets
        self.btn_reset = QPushButton('Reset')
        self.btn_solve = QPushButton('Solve')
        self.btn_next = QPushButton()
        self.btn_previous = QPushButton()
        icon_back = QIcon("img/back_button.png")
        icon_forward = QIcon("img/forward_button.png")
        self.btn_previous.setIcon(icon_back)
        self.btn_next.setIcon(icon_forward)

        # Label Widgets
        self.lbl_stats = QLabel('STATISTICS\n\nCost of Path:\nNodes Expanded:\nSearch Depth:\nRunning Time:')
        self.lbl_move = QLabel()
        self.lbl_move.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.board = []
        for i in range(9):
            self.board.append(QTextEdit())
            self.board[i].setFixedSize(85, 85)
            self.board[i].setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.board[i].setFont(QFont('Arial', 42))
            grid.addWidget(self.board[i], 1 + i//3, i%3)

        grid.addWidget(self.btn_previous, 4, 0)
        grid.addWidget(self.btn_next, 4, 2)
        grid.addWidget(self.lbl_move, 4, 1)
        grid.addWidget(self.cb_algorithm, 0, 0, 1, 3)
        grid.addWidget(self.lbl_stats, 5, 0, 1, 3)
        grid.addWidget(self.btn_solve, 6, 0, 1, 2)
        grid.addWidget(self.btn_reset, 6, 2)

        self.btn_reset.clicked.connect(self.reset)
        self.btn_solve.clicked.connect(self.solve)
        self.btn_next.clicked.connect(self.next_step)
        self.btn_previous.clicked.connect(self.previous_step)

    def solve(self):
        user_choice_algorithm = str(self.cb_algorithm.currentIndex())
        if user_choice_algorithm == '0':
            self.lbl_move.setText('Select Algorithm')
            return
        
        initial_state = ''
        zero_index = 0

        for i in range(9):
            if self.board[i].toPlainText() == '0':
                zero_index = i
            initial_state += self.board[i].toPlainText()

        initial_state += str(zero_index)
        goal_state = '0123456780'
        solver = Solver()
        solution, steps, cost_of_path, nodes_expanded, search_depth, running_time = solver.solve(user_choice_algorithm, initial_state, goal_state)
        if not solution:
            self.lbl_move.setText('No Solution')
            return
        self.updateStatistics(cost_of_path, nodes_expanded, search_depth, running_time)
        self.updateBoard(steps[-1])
        self.steps = steps
        self.steps_index = len(steps) - 1

    def updateStatistics(self, cost_of_path, nodes_expanded, search_depth, running_time):
        self.lbl_stats.setText(f'STATISTICS\n\nCost of Path: {cost_of_path}\nNodes Expanded: {nodes_expanded}\nSearch Depth: {search_depth}\nRunning Time: {running_time}')
            

    def updateBoard(self, board):
        for i in range(9):
            self.board[i].setText(str(board[i]))
            self.board[i].setAlignment(Qt.AlignmentFlag.AlignCenter)
            if str(board[i]) == '0':
                self.board[i].setStyleSheet('QTextEdit {color: blue;}')
            else:
                self.board[i].setStyleSheet('QTextEdit {color: none;}')
        
    def get_movement(self, from_state, to_state):
        zero_index_from = from_state.index('0')
        zero_index_to = to_state.index('0')
        if zero_index_from == zero_index_to + 1:
            return 'Right'
        elif zero_index_from == zero_index_to - 1:
            return 'Left'
        elif zero_index_from == zero_index_to + 3:
            return 'Down'
        elif zero_index_from == zero_index_to - 3:
            return 'Up'
        else:
            return 'Invalid'

    def reset(self):
        for i in range(9):
            self.board[i].setText('')
            self.board[i].setAlignment(Qt.AlignmentFlag.AlignCenter)

    def previous_step(self):
        if self.steps_index == 0: return
        self.steps_index -= 1
        self.updateBoard(self.steps[self.steps_index])
        movement = self.get_movement(self.steps[self.steps_index], self.steps[self.steps_index + 1])
        self.lbl_move.setText(movement)
    
    def next_step(self):
        if not self.steps or self.steps_index == len(self.steps) - 1: return
        self.steps_index += 1
        self.updateBoard(self.steps[self.steps_index])
        movement = self.get_movement(self.steps[self.steps_index], self.steps[self.steps_index - 1])
        self.lbl_move.setText(movement)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Solver_GUI()
    ex.show()
    sys.exit(app.exec())
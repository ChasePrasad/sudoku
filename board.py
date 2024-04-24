import pygame

import sudoku_generator
from cell import Cell

class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty

        #if self.difficulty == 1:
            #generator = SudokuGenerator(9, 30)
        #elif self.difficulty == 2:
            #generator = SudokuGenerator(9, 40)
        #else:
            #generator = SudokuGenerator(9, 50)

        self.answerBoard, self.playerBoard = sudoku_generator.generate_sudoku(9, 30)

        self.boardList = [[0] * 9 for i in range(9)]

        for i in range(9):
            for j in range(9):
                self.boardList[i][j] = Cell(self.playerBoard[i][j], i, j, self.screen)

    def draw(self):
        for row in range(1, 10):
            for col in range(1, 10):
                if (col % 3 == 0 and row % 3 == 0):
                    pygame.draw.line(self.screen, (0, 0, 0), (col*100, 0), (col*100, 900), 3)
                    pygame.draw.line(self.screen, (0, 0, 0), (0, row * 100), (900, row * 100), 3)
                else:
                    pygame.draw.line(self.screen, (0, 0, 0), (col*100, 0), (col*100, 900), 1)
                    pygame.draw.line(self.screen, (0, 0, 0), (0, row * 100), (900, row * 100), 1)

    def click(self):
        # determines whether player clicks inside game board.
        # Big if true: return True, x coordinate of click, y coordinate of click
        # Garbaje if false, return None
        coordinates = pygame.mouse.get_pos()
        if ((0 < coordinates[0] and coordinates[0] < 900) and (0< coordinates[1] and coordinates[1] < 900)):
            return True, coordinates[0], coordinates[1]
        else:
            return None

    #finds which cell is selected, returns x and y coordinates
    def select(self):
        self.status, self.xcoordinate, self.ycoordinate = self.click()
        if(self.status):
            self.selectedColumn = self.xcoordinate // 100
            self.selectedRow = self.ycoordinate // 100
            return self.selectedColumn, self.selectedRow
        else:
            return None

    def clear(self, row, col):
        self.boardList[row][col] = Cell(0, row, col, self.screen)

    def sketch(self, value):
        self.sketchValue = value
        Cell.set_sketched_value(self.sketchValue)
        Cell.draw()

    def place_number(self, value):
        self.userInputColumn, self.userInputRow = self.select()
        self.boardList[self.UserInputRow][self.userInputColumn] = Cell(value, self.UserInputRow, self.userInputColumn, self.screen)
        self.update_board(value, self.UserInputRow, self.userInputColumn)

    def reset_to_original(self):
        for i in range(9):
            for j in range(9):
                self.boardList[i][j] = [Cell(self.playerBoard[i][j], i, j, self.screen)]

    def is_full(self):
        for i in range(9):
            for j in range(9):
                if self.boardList[i][j].getValue() == 0:
                    return False
        return True

    def update_board(self, value, row, col):
        self.playerBoard[row][col] = value

    def find_empty(self):
        for i in range(9):
            for j in range(9):
                if(self.boardList[i][j].getValue() == 0):
                    #returns row, column
                    return i, j
        return False

    def check_board(self):
        for i in range(9):
            for j in range(9):
                if((self.boardList[i][j].getValue()) != self.answerBoard[i][j]):
                    return False
        return True

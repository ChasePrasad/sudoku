
import pygame
import math

from sudoku_generator import SudokuGenerator
from cell import Cell

class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty

        if self.difficulty == 1:
            self.generator = SudokuGenerator(9, 30)
        elif self.difficulty == 2:
            self.generator = SudokuGenerator(9, 40)
        elif self.difficulty == 3:
            self.generator = SudokuGenerator(9, 50)

        self.generator.fill_values()
        self.answerBoard = self.generator.get_board()

        for i in range(9):
            for j in range(9):
                print(self.answerBoard[i][j], end=' ')
            print()
        print()

        self.generator.remove_cells()
        self.playerBoardOriginal = self.generator.get_board()
        self.playerBoardInputs = self.playerBoardOriginal.copy()

        for i in range(9):
            for j in range(9):
                print(self.playerBoardOriginal[i][j], end=' ')
            print()
        print()

        self.boardList = [[0] * 9 for i in range(9)]

        for i in range(9):
            for j in range(9):
                self.boardList[i][j] = Cell(self.playerBoardInputs[i][j], i, j, self.screen)

    def setDifficulty(self, diff):
        self.difficulty = diff

    def getCell(self, row, col):
        return self.boardList[row][col]

    def draw(self):
         for row in range(9):
            for col in range(9):
                self.boardList[row][col].draw()
                if (row != 0 and col != 0 and col % 3 == 0 and row % 3 == 0):
                    pygame.draw.line(self.screen, (0, 0, 0), (col * 60, 0), (col * 60, self.height - 60), 6)
                    pygame.draw.line(self.screen, (0, 0, 0), (0, row * 60), (self.width, row * 60), 6)

    def click(self, xcoord, ycoord):

        if ((0 < xcoord and xcoord < 540) and (0< ycoord and ycoord < 540)):
            self.selectedColumn = math.floor(float(xcoord / 60))
            self.selectedRow = math.floor(float(ycoord / 60))
            return self.selectedRow, self.selectedColumn
        else:
            return None, None

    #finds which cell is selected, returns x and y coordinates
    def select(self, row, col):
        if(self.boardList[row][col].get_value() == 0):

            self.boardList[row][col].set_chosen(True)
        else:
            #return False if player CANNOT edit
            self.boardList[row][col].set_chosen(False)

    def deselect(self, row, col):
        self.boardList[row][col].set_chosen(False)
        self.boardList[row][col].colored_cell(row, col)
    def clear(self, row, col):
        self.boardList[row][col].set_sketched_value(0)

    def sketch(self, value, row, col):
        self.boardList[row][col].set_sketched_value(value)

    def place_number(self, value, row, col):
        self.userInputColumn, self.userInputRow = col, row
        self.boardList[self.userInputRow][self.userInputColumn] = Cell(value, self.userInputRow, self.userInputColumn, self.screen)
        self.update_board(value, self.userInputRow, self.userInputColumn)

    def reset_to_original(self):
        for i in range(9):
            for j in range(9):
                print(self.answerBoard[i][j], end=' ')
            print()
        print()

        # for i in range(9):
        #     for j in range(9):
        #         print(self.playerBoardOriginal[i][j], end=' ')
        #     print()

        newArray = self.generator.get_board()

        for i in range(9):
            for j in range(9):
                print(newArray[i][j], end=' ')
            print()

        for i in range(9):
            for j in range(9):
                # print("Answer board: \n" + str(self.answerBoard[i][j]))
                # print("Original Board: \n" + str(self.playerBoardOriginal[i][j]))
                self.boardList[i][j].set_sketched_value(0)

                self.boardList[i][j].set_cell_value(newArray[i][j])



    def is_full(self):
        for i in range(9):
            for j in range(9):
                if self.boardList[i][j].get_value() == 0:
                    return False
        return True
    def update_board(self, value, row, col):
        self.playerBoardInputs[row][col] = value

    def find_empty(self):
        for i in range(9):
            for j in range(9):
                if(Cell.get_value(self.boardList[i][j]) == 0):
                    #returns row, column
                    return i, j
        return None

    def check_board(self):
        for i in range(9):
            for j in range(9):
                if(Cell.get_value(self.boardList[i][j]) != self.answerBoard[i][j]):
                    return False

        return True

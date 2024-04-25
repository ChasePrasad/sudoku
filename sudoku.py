import pygame
from board import Board

pygame.init()
screen = pygame.display.set_mode((540, 600))
pygame.display.set_caption("Sudoku")
screen.fill((205, 173, 135))


def main():
    # homescreen for sudoku
    # centers and imports the sudoku logo
    screen.blit(pygame.image.load("bg.jpg"), (0, 0))

    # prints and centers the welcome text using the correct font, font size, color
    welcome_surf = pygame.font.Font("font.ttf", 50).render("Welcome to Sudoku", 1, "black")
    welcome_rect = welcome_surf.get_rect(center=(270, 80))
    screen.blit(welcome_surf, welcome_rect)

    # prints and centers the game mode selection text using the correct font, font size, color
    mode_surf = pygame.font.Font("font.ttf", 35).render("Select Game Mode:", 1, "black")
    mode_rect = mode_surf.get_rect(center=(270, 500))
    screen.blit(mode_surf, mode_rect)

    # prints and centers a rectangle
    button_easy = pygame.draw.rect(screen, "white", pygame.Rect(75, 530, 90, 35))
    # prints and centers the game mode: easy text using the correct font, font size, color
    easy_surf = pygame.font.Font("font.ttf", 18).render("Easy", 1, "black")
    easy_rect = easy_surf.get_rect(center=(120, 548))
    screen.blit(easy_surf, easy_rect)

    # prints and centers a rectangle
    button_med = pygame.draw.rect(screen, "white", pygame.Rect(225, 530, 90, 35))
    # prints and centers the game mode: medium text using the correct font, font size, color
    medium_surf = pygame.font.Font("font.ttf", 18).render("Medium", 1, "black")
    medium_rect = medium_surf.get_rect(center=(270, 548))
    screen.blit(medium_surf, medium_rect)

    # prints and centers a rectangle
    button_hard = pygame.draw.rect(screen, "white", pygame.Rect(375, 530, 90, 35))
    # prints and centers the game mode: hard text using the correct font, font size, color
    hard_surf = pygame.font.Font("font.ttf", 18).render("Hard", 1, "black")
    hard_rect = hard_surf.get_rect(center=(420, 548))
    screen.blit(hard_surf, hard_rect)

    while True:
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    pygame.quit()
                    exit()
                case pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    # lets the user pick game modes
                    # easy mode
                    if button_easy.collidepoint(x, y):
                        draw_game_run(1)

                    # medium mode
                    elif button_med.collidepoint(x, y):
                        draw_game_run(2)

                    # hard mode
                    elif button_hard.collidepoint(x, y):
                        draw_game_run(3)

        pygame.display.update()


def draw_game_won():
    # centers and imports the sudoku logo
    screen.blit(pygame.image.load("bg.jpg"), (0, 0))

    # prints and centers the winner text using the correct font, font size, color
    won_surf = pygame.font.Font("font.ttf", 50).render("Game Won!", 1, "black")
    won_rect = won_surf.get_rect(center=(270, 80))
    screen.blit(won_surf, won_rect)

    # prints and centers a rectangle
    button_won_exit = pygame.draw.rect(screen, "white", pygame.Rect(225, 530, 90, 35))
    # prints and centers the exit text using the correct font, font size, color
    exit_surf = pygame.font.Font("font.ttf", 18).render("Exit", 1, "black")
    exit_rect = exit_surf.get_rect(center=(270, 548))
    screen.blit(exit_surf, exit_rect)

    # lets the user exit the game when they win
    while True:
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    pygame.quit()
                    exit()
                case pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if button_won_exit.collidepoint(x, y):
                        exit()
        pygame.display.update()

def draw_game_over():
    # centers and imports the sudoku logo
    screen.blit(pygame.image.load("bg.jpg"), (0, 0))

    # prints and centers the losing text using the correct font, font size, color
    welcome_surf = pygame.font.Font("font.ttf", 50).render("Game Over :(", 1, "black")
    welcome_rect = welcome_surf.get_rect(center=(270, 80))
    screen.blit(welcome_surf, welcome_rect)

    # prints and centers a rectangle
    button_over_restart = pygame.draw.rect(screen, "white", pygame.Rect(225, 530, 90, 35))
    # prints and centers the restart text using the correct font, font size, color
    restart_surf = pygame.font.Font("font.ttf", 18).render("Restart", 1, "black")
    restart_rect = restart_surf.get_rect(center=(270, 548))
    screen.blit(restart_surf, restart_rect)

    # lets the user restart the game when they lose
    while True:
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    pygame.quit()
                    exit()
                case pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if button_over_restart.collidepoint(x, y):
                        main()
        pygame.display.update()


def draw_game_run(difficulty):
    screen.fill((205, 173, 135))
    board = Board(540, 600, screen, difficulty)
    board.draw()

    # prints and centers a rectangle
    button_reset = pygame.draw.rect(screen, "white", pygame.Rect(75, 550, 90, 35))
    # prints and centers the game mode: easy text using the correct font, font size, color
    easy_surf = pygame.font.Font("font.ttf", 18).render("Reset", 1, "black")
    easy_rect = easy_surf.get_rect(center=(120, 568))
    screen.blit(easy_surf, easy_rect)

    # prints and centers a rectangle
    button_restart = pygame.draw.rect(screen, "white", pygame.Rect(225, 550, 90, 35))
    # prints and centers the game mode: medium text using the correct font, font size, color
    medium_surf = pygame.font.Font("font.ttf", 18).render("Restart", 1, "black")
    medium_rect = medium_surf.get_rect(center=(270, 568))
    screen.blit(medium_surf, medium_rect)

    # prints and centers a rectangle
    button_exit = pygame.draw.rect(screen, "white", pygame.Rect(375, 550, 90, 35))
    # prints and centers the game mode: hard text using the correct font, font size, color
    hard_surf = pygame.font.Font("font.ttf", 18).render("Exit", 1, "black")
    hard_rect = hard_surf.get_rect(center=(420, 568))
    screen.blit(hard_surf, hard_rect)

    # lets the user reset, restart, and exit when the game is running
    while True:
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    pygame.quit()
                    exit()
                case pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if button_reset.collidepoint(x, y):
                        board.clear()

                    elif button_restart.collidepoint(x, y):
                        main()

                    elif button_exit.collidepoint(x, y):
                        exit()
                case pygame.MOUSEBUTTONDOWN:
                    # allows the user to select a cell


        pygame.display.update()



if __name__ == "__main__":
    main()

import pygame
from board import Board
from cell import Cell

# use the screen size of 630, 700
pygame.init()
screen = pygame.display.set_mode((540, 600))
pygame.display.set_caption("Sudoku")
screen.fill((205, 173, 135))

def main():
    draw_game_start()
    boardobj = Board(900, 900, screen, None)
    
    while True:
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    pygame.quit()
                    exit()

                case pygame.KEYDOWN:
                    match event.key:
                        case pygame.MOUSEBUTTONDOWN:
                            x, y = event.pos
                            draw_game_start()

                        case pygame.K_w:
                            draw_game_won()
                            
                        case pygame.K_o:
                            draw_game_over()

                        case pygame.K_r:
                            draw_game_run()

                        case pygame.K_b:
                            boardobj.draw()

        pygame.display.update()

def draw_game_start():
    screen.fill((205, 173, 135))
    image = pygame.image.load("bg.jpg")
    image = pygame.transform.scale(image, (540, 600))
    screen.blit(image, (0, 0))

    welcome_surf = pygame.font.Font("font.ttf", 75).render("Welcome to Sudoku", 1, "black")
    welcome_rect = welcome_surf.get_rect(center=(270, 115))
    screen.blit(welcome_surf, welcome_rect)

    mode_surf = pygame.font.Font("font.ttf", 50).render("Select Game Mode:", 1, "black")
    mode_rect = mode_surf.get_rect(center=(270, 730))
    screen.blit(mode_surf, mode_rect)

    pygame.draw.rect(screen, "white", pygame.Rect(250, 780, 100, 50))
    easy_surf = pygame.font.Font("font.ttf", 22).render("Easy", 1, "black")
    easy_rect = easy_surf.get_rect(center=(300, 805))
    screen.blit(easy_surf, easy_rect)

    pygame.draw.rect(screen, "white", pygame.Rect(400, 780, 100, 50))
    medium_surf = pygame.font.Font("font.ttf", 22).render("Medium", 1, "black")
    medium_rect = medium_surf.get_rect(center=(270, 805))
    screen.blit(medium_surf, medium_rect)

    pygame.draw.rect(screen, "white", pygame.Rect(550, 780, 100, 50))
    hard_surf = pygame.font.Font("font.ttf", 22).render("Hard", 1, "black")
    hard_rect = hard_surf.get_rect(center=(600, 805))
    screen.blit(hard_surf, hard_rect)

def draw_game_won():
    screen.fill((205, 173, 135))
    screen.blit(pygame.image.load("bg.jpg"), (50, 50))

    won_surf = pygame.font.Font("font.ttf", 75).render("Game Won!", 1, "black")
    won_rect = won_surf.get_rect(center=(450, 115))
    screen.blit(won_surf, won_rect)

    pygame.draw.rect(screen, "white", pygame.Rect(400, 780, 100, 50))
    exit_surf = pygame.font.Font("font.ttf", 22).render("Exit", 1, "black")
    exit_rect = exit_surf.get_rect(center=(450, 805))
    screen.blit(exit_surf, exit_rect)

def draw_game_over():
    screen.fill((205, 173, 135))
    screen.blit(pygame.image.load("bg.jpg"), (50, 50))

    welcome_surf = pygame.font.Font("font.ttf", 75).render("Game Over :(", 1, "black")
    welcome_rect = welcome_surf.get_rect(center=(450, 115))
    screen.blit(welcome_surf, welcome_rect)

    pygame.draw.rect(screen, "white", pygame.Rect(400, 780, 100, 50))
    restart_surf = pygame.font.Font("font.ttf", 22).render("Restart", 1, "black")
    restart_rect = restart_surf.get_rect(center=(450, 805))
    screen.blit(restart_surf, restart_rect)

def draw_game_run():
    screen.fill((205, 173, 135))
    c = Cell(1,0,0, screen)
    c.draw()


if __name__ == "__main__":
    main()

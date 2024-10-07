import pygame
import random
import os

# Initialize Pygame
pygame.init()

# Colors
BACKGROUND_COLOR = (250, 248, 239)
GRID_COLOR = (187, 173, 160)
EMPTY_CELL_COLOR = (205, 193, 180)
TEXT_COLOR = (119, 110, 101)
LIGHT_TEXT_COLOR = (249, 246, 242)
BUTTON_COLOR = (143, 122, 102)
BUTTON_HOVER_COLOR = (133, 112, 92)

TILE_COLORS = {
    2: (238, 228, 218),
    4: (237, 224, 200),
    8: (242, 177, 121),
    16: (245, 149, 99),
    32: (246, 124, 95),
    64: (246, 94, 59),
    128: (237, 207, 114),
    256: (237, 204, 97),
    512: (237, 200, 80),
    1024: (237, 197, 63),
    2048: (237, 194, 46),
    4096: (60, 58, 50),
    8192: (60, 58, 50),
}

# Game constants
TILE_SIZE = 80  # Updated for more precise tile size
GRID_SIZE = 4
GRID_PADDING = 7  # Reduced padding for better alignment
WINDOW_WIDTH = TILE_SIZE * GRID_SIZE + GRID_PADDING * (GRID_SIZE + 1)
WINDOW_HEIGHT = WINDOW_WIDTH + 250

# Create the game window
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("2048")

# Fonts
title_font = pygame.font.Font(None, 90)
score_font = pygame.font.Font(None, 40)
button_font = pygame.font.Font(None, 36)


class Game2048:
    def __init__(self):
        self.board = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
        self.score = 0
        self.high_score = self.load_high_score()
        self.add_new_tile()
        self.add_new_tile()

    def load_high_score(self):
        if os.path.exists("high_score.txt"):
            with open("high_score.txt", "r") as f:
                return int(f.read())
        return 0

    def save_high_score(self):
        with open("high_score.txt", "w") as f:
            f.write(str(self.high_score))

    def add_new_tile(self):
        empty_cells = [
            (i, j)
            for i in range(GRID_SIZE)
            for j in range(GRID_SIZE)
            if self.board[i][j] == 0
        ]
        if empty_cells:
            i, j = random.choice(empty_cells)
            self.board[i][j] = 2 if random.random() < 0.9 else 4

    def move(self, direction):
        moved = False
        if direction == "up":
            for j in range(GRID_SIZE):
                column = [
                    self.board[i][j] for i in range(GRID_SIZE) if self.board[i][j] != 0
                ]
                merged_column = self.merge(column)
                for i in range(GRID_SIZE):
                    new_value = merged_column[i] if i < len(merged_column) else 0
                    if self.board[i][j] != new_value:
                        moved = True
                    self.board[i][j] = new_value
        elif direction == "down":
            for j in range(GRID_SIZE):
                column = [
                    self.board[i][j]
                    for i in range(GRID_SIZE - 1, -1, -1)
                    if self.board[i][j] != 0
                ]
                merged_column = self.merge(column)
                for i in range(GRID_SIZE - 1, -1, -1):
                    new_value = (
                        merged_column[GRID_SIZE - 1 - i]
                        if GRID_SIZE - 1 - i < len(merged_column)
                        else 0
                    )
                    if self.board[i][j] != new_value:
                        moved = True
                    self.board[i][j] = new_value
        elif direction == "left":
            for i in range(GRID_SIZE):
                row = [
                    self.board[i][j] for j in range(GRID_SIZE) if self.board[i][j] != 0
                ]
                merged_row = self.merge(row)
                for j in range(GRID_SIZE):
                    new_value = merged_row[j] if j < len(merged_row) else 0
                    if self.board[i][j] != new_value:
                        moved = True
                    self.board[i][j] = new_value
        elif direction == "right":
            for i in range(GRID_SIZE):
                row = [
                    self.board[i][j]
                    for j in range(GRID_SIZE - 1, -1, -1)
                    if self.board[i][j] != 0
                ]
                merged_row = self.merge(row)
                for j in range(GRID_SIZE - 1, -1, -1):
                    new_value = (
                        merged_row[GRID_SIZE - 1 - j]
                        if GRID_SIZE - 1 - j < len(merged_row)
                        else 0
                    )
                    if self.board[i][j] != new_value:
                        moved = True
                    self.board[i][j] = new_value
        if moved:
            self.add_new_tile()
        self.high_score = max(self.high_score, self.score)
        self.save_high_score()

    def merge(self, line):
        merged = []
        i = 0
        while i < len(line):
            if i + 1 < len(line) and line[i] == line[i + 1]:
                merged.append(line[i] * 2)
                self.score += line[i] * 2
                i += 2
            else:
                merged.append(line[i])
                i += 1
        return merged

    def is_game_over(self):
        if any(0 in row for row in self.board):
            return False
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                if (i < GRID_SIZE - 1 and self.board[i][j] == self.board[i + 1][j]) or (
                    j < GRID_SIZE - 1 and self.board[i][j] == self.board[i][j + 1]
                ):
                    return False
        return True

    def draw(self):
        screen.fill(BACKGROUND_COLOR)

        # Draw title
        title_text = title_font.render("2048", True, TEXT_COLOR)
        screen.blit(title_text, (20, 20))

        # Draw score and high score
        score_text = score_font.render(f"Score: {self.score}", True, TEXT_COLOR)
        high_score_text = score_font.render(
            f"Best: {self.high_score}", True, TEXT_COLOR
        )
        screen.blit(score_text, (WINDOW_WIDTH - 180, 30))
        screen.blit(high_score_text, (WINDOW_WIDTH - 180, 80))

        # Draw game board
        self.draw_game_board()

    def draw_game_board(self):
        pygame.draw.rect(
            screen,
            GRID_COLOR,
            (
                GRID_PADDING,
                120,
                WINDOW_WIDTH - 2 * GRID_PADDING,
                WINDOW_WIDTH - 2 * GRID_PADDING,
            ),
            border_radius=12,
        )

        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                value = self.board[i][j]
                x = j * (TILE_SIZE + GRID_PADDING) + GRID_PADDING
                y = i * (TILE_SIZE + GRID_PADDING) + 120 + GRID_PADDING
                tile_rect = pygame.Rect(x, y, TILE_SIZE, TILE_SIZE)

                if value == 0:
                    pygame.draw.rect(
                        screen, EMPTY_CELL_COLOR, tile_rect, border_radius=10
                    )
                else:
                    color = TILE_COLORS.get(min(value, 8192), (60, 58, 50))
                    pygame.draw.rect(screen, color, tile_rect, border_radius=10)

                    # Adjust font size based on the number of digits
                    font_size = 50 if value < 100 else 40 if value < 1000 else 30
                    font = pygame.font.Font(None, font_size)

                    text_color = TEXT_COLOR if value < 8 else LIGHT_TEXT_COLOR
                    text = font.render(str(value), True, text_color)
                    text_rect = text.get_rect(center=tile_rect.center)
                    screen.blit(text, text_rect)


def draw_button(text, x, y, width, height, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x < mouse[0] < x + width and y < mouse[1] < y + height:
        pygame.draw.rect(screen, BUTTON_HOVER_COLOR, (x, y, width, height))
        if click[0] == 1 and action is not None:
            action()
    else:
        pygame.draw.rect(screen, BUTTON_COLOR, (x, y, width, height))

    text_surf = button_font.render(text, True, LIGHT_TEXT_COLOR)
    text_rect = text_surf.get_rect(center=((x + (width / 2)), (y + (height / 2))))
    screen.blit(text_surf, text_rect)


def main():
    game = Game2048()
    running = True
    game_over = False

    def restart_game():
        nonlocal game, game_over
        game = Game2048()
        game_over = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and not game_over:
                if event.key == pygame.K_UP:
                    game.move("up")
                elif event.key == pygame.K_DOWN:
                    game.move("down")
                elif event.key == pygame.K_LEFT:
                    game.move("left")
                elif event.key == pygame.K_RIGHT:
                    game.move("right")

        game.draw()

        if game.is_game_over() and not game_over:
            game_over = True

        if game_over:
            # Draw semi-transparent overlay
            overlay = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
            overlay.set_alpha(180)
            overlay.fill((255, 255, 255))
            screen.blit(overlay, (0, 0))

            game_over_text = title_font.render("Game Over!", True, TEXT_COLOR)
            text_rect = game_over_text.get_rect(
                center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 50)
            )
            screen.blit(game_over_text, text_rect)

        # Draw restart button
        draw_button(
            "Restart",
            WINDOW_WIDTH // 2 - 100,
            WINDOW_HEIGHT - 80,
            200,
            50,
            restart_game,
        )

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()

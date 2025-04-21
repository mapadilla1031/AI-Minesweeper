import random

# Parameters
WIDTH = 5
HEIGHT = 5
NUM_MINES = 5

# Directions for neighbors
DIRS = [(-1, -1), (-1, 0), (-1, 1),
        (0, -1),         (0, 1),
        (1, -1),  (1, 0), (1, 1)]


class MinesweeperAI:
    def __init__(self, width, height, num_mines):
        self.width = width
        self.height = height
        self.board = [[' ' for _ in range(width)] for _ in range(height)]
        self.revealed = [[False]*width for _ in range(height)]
        self.mines = set()
        self.num_mines = num_mines
        self.generate_board()

    def generate_board(self):
        while len(self.mines) < self.num_mines:
            x = random.randint(0, self.height - 1)
            y = random.randint(0, self.width - 1)
            self.mines.add((x, y))

    def count_adjacent_mines(self, x, y):
        count = 0
        for dx, dy in DIRS:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.height and 0 <= ny < self.width:
                if (nx, ny) in self.mines:
                    count += 1
        return count

    def reveal(self, x, y):
        if (x, y) in self.mines:
            print("💥 BOOM! Stepped on a mine at", x, y)
            return False
        self.revealed[x][y] = True
        count = self.count_adjacent_mines(x, y)
        self.board[x][y] = str(count)
        return True

    def get_unrevealed_neighbors(self, x, y):
        neighbors = []
        for dx, dy in DIRS:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.height and 0 <= ny < self.width and not self.revealed[nx][ny]:
                neighbors.append((nx, ny))
        return neighbors

    def predict_safest_move(self):
        probability_map = {}
        for x in range(self.height):
            for y in range(self.width):
                if self.revealed[x][y] and self.board[x][y].isdigit():
                    num = int(self.board[x][y])
                    unrevealed = self.get_unrevealed_neighbors(x, y)
                    if unrevealed:
                        prob = num / len(unrevealed)
                        for cell in unrevealed:
                            probability_map[cell] = max(probability_map.get(cell, 0), prob)

        # Fallback: all unknowns treated equally
        all_unrevealed = [(x, y) for x in range(self.height)
                          for y in range(self.width) if not self.revealed[x][y]]
        if not probability_map and all_unrevealed:
            return random.choice(all_unrevealed)

        # Choose the cell with lowest probability
        if probability_map:
            best_cell = min(probability_map.items(), key=lambda item: item[1])[0]
            return best_cell

        return None

    def print_board(self):
        print("\nCurrent board:")
        for i in range(self.height):
            row = ""
            for j in range(self.width):
                if self.revealed[i][j]:
                    row += f" {self.board[i][j]} "
                else:
                    row += " . "
            print(row)
        print()

    def play(self):
        while True:
            self.print_board()
            move = self.predict_safest_move()
            if move is None:
                print("🎉 Game complete or no safe moves left.")
                break
            print(f"AI selects: {move}")
            if not self.reveal(*move):
                self.print_board()
                break


if __name__ == "__main__":
    game = MinesweeperAI(WIDTH, HEIGHT, NUM_MINES)
    game.play()

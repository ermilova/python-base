#Interactive Tic-Tac-Toe game
def print_grid(grid):
    print('-' * 9)
    for i in range(0, 3):
        print("|", " ".join(grid[i]), "|")
    print('-' * 9)


def get_move():
    while True:
        user_input = [x for x in input("Enter the coordinates: ").split()]
        try:
            user_move = [int(x) - 1 for x in user_input]
            if not 0 <= user_move[0] < 3 or not 0 <= user_move[1] < 3:
                print("Coordinates should be from 1 to 3!")
            elif grid[user_move[0]][user_move[1]] != "_":
                print("This cell is occupied! Choose another one!")
            else:
                break
        except ValueError:
            print("You should enter numbers!")
    return user_move[0], user_move[1]


grid_str = '_' * 9
grid = []
for i in range(0, 3):
    grid.append([])
    for j in range(0, 3):
        grid[i].append(grid_str[i * 3 + j])
print_grid(grid)

move = ["X", "O"]
current_player = 0
for _ in range(0, 9):
    x, y = get_move()
    grid[x][y] = move[current_player]
    current_player = (current_player + 1) % 2
    print_grid(grid)

    win = {"X": False, "O": False, "_": False}
    for i in range(0, 3):
        if grid[i][0] == grid[i][1] == grid[i][2]:
            win[grid[i][0]] = True
    for j in range(0, 3):
        if grid[0][j] == grid[1][j] == grid[2][j]:
            win[grid[0][j]] = True
    if grid[0][0] == grid[1][1] == grid[2][2]:
        win[grid[1][1]] = True
    if grid[0][2] == grid[1][1] == grid[2][0]:
        win[grid[1][1]] = True
    if win["X"]:
        print("X wins")
        break
    elif win["O"]:
        print("O wins")
        break
else:
    print("Draw")

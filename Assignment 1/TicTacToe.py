import math
import copy

class TicTacToe():
    def __init__(self, state=[[0,0,0],[0,0,0],[0,0,0]]):
        self.state = state

    def make_move(self, row, col, val):
        if (
            0 <= row < 3 and
            0 <= col < 3 and
            self.state[row][col] == 0
        ):
            self.state[row][col] = val
            return True
        else:
            return False

    def display_board(self):
        for row in self.state:
            symbols = []
            for i in row:
                if i == 1:
                    symbols.append("X")
                elif i == -1:
                    symbols.append("O")
                elif i == 0:
                    symbols.append(" ")
            print(" | ".join(symbols))
            print("-" * 9)

    def try_move(state, row, col, val):
        if 0 <= row < 3 and 0 <= col < 3 and state[row][col] == 0:
            state[row][col] = val
        return state

    def terminal_node(self, state):

        isWinner = False

        # Check rows
        for i in range(3):
            sum_p1_row, sum_p2_row = 0, 0
            for j in range(3):
                if state[i][j] == 1:
                    sum_p1_row += 1
                elif state[i][j] == -1:
                    sum_p2_row += -1
            if sum_p1_row == 3:
                isWinner = True
                return {"gameover": True, "result": 10}
            elif sum_p2_row == -3:
                isWinner = True
                return {"gameover": True, "result": -10}

        # Check columns
        for i in range(3):
            sum_p1_col, sum_p2_col = 0, 0
            for j in range(3):
                if state[j][i] == 1:
                    sum_p1_col += 1
                elif state[j][i] == -1:
                    sum_p2_col += -1
            if sum_p1_col == 3:
                isWinner = True
                return {"gameover": True, "result": 10}
            elif sum_p2_col == -3:
                isWinner = True
                return {"gameover": True, "result": -10}

        # Check top-left to bottom-right diagonal
        sum_p1_diag, sum_p2_diag = 0, 0
        for i in range(3):
            if state[i][i] == 1:
                sum_p1_diag += 1
            elif state[i][i] == -1:
                sum_p2_diag += -1
        if sum_p1_diag == 3:
            isWinner = True
            return {"gameover": True, "result": 10}
        elif sum_p2_diag == -3:
            isWinner = True
            return {"gameover": True, "result": -10}

        # Check top-right to bottom-left diagonal
        sum_p1_rev_diag, sum_p2_rev_diag = 0, 0
        for i in range(3):
            if state[i][2 - i] == 1:
                sum_p1_rev_diag += 1
            elif state[i][2 - i] == -1:
                sum_p2_rev_diag += -1
        if sum_p1_rev_diag == 3:
            isWinner = True
            return {"gameover": True, "result": 10}
        elif sum_p2_rev_diag == -3:
            isWinner = True
            return {"gameover": True, "result": -10}

        emptyCells = False
        for i in range(3):
            emptyCells = any(state[i][j] == 0 for j in range(3))

        if isWinner:
            return {"gameover": True, "result": 10}
        elif not emptyCells:
            return {"gameover": True, "result": 0}
        else:
            return {"gameover": False, "result": 0}


    def expand_state(self, state):
        children = []
        for i in range(3):
            for j in range(3):
                if state[i][j] == 0:
                    child = [i, j]
                    children.append(child)
        return children


    def computer_move(self):
        _, best_move = self.minimax(self.state, -1, 9, True)
        if best_move is not None:
            row, col = best_move
            self.make_move(row, col, -1)
        return best_move

    def minimax(self, state, player, depth, isMaxPlayer):
        if self.terminal_node(state)["gameover"] or depth == 0:
            return self.terminal_node(state)["result"], None

        best_move = None
        if isMaxPlayer:
            best_score = -math.inf
            for move in self.expand_state(state):
                row, col = move
                child = copy.deepcopy(state)
                child[row][col] = 1
                score, _ = self.minimax(child, -1, depth - 1, not isMaxPlayer)
                if score > best_score:
                    best_score = score
                    best_move = move
            return best_score, best_move
        else:
            best_score = math.inf
            for move in self.expand_state(state):
                row, col = move
                child = copy.deepcopy(state)
                child[row][col] = -1
                score, _ = self.minimax(child, 1, depth - 1, not isMaxPlayer)
                if score < best_score:
                    best_score = score
                    best_move = move
            return best_score, best_move


def user_move():
    while True:
        try:
            row = int(input("Enter the row (0, 1, 2): "))
            col = int(input("Enter the column (0, 1, 2): "))
            return row, col
        except ValueError:
            print("Invalid input. Please enter valid row and column numbers.")

def main():
    game = TicTacToe()
    player_turn = True

    while True:
        game.display_board()

        if player_turn:
            print("Player's turn (X):")
            row, col = user_move()
            if game.make_move(row, col, 1):
                player_turn = False
        else:
            print("Computer's turn (O):")
            row, col = game.computer_move()
            game.make_move(row, col, -1)
            player_turn = True

        result = game.terminal_node(game.state)
        if result["gameover"]:
            game.display_board()
            if result["result"] == 10:
                print("You win!")
            elif result["result"] == -10:
                print("Computer wins!")
            else:
                print("It's a tie!")
            break

if __name__ == "__main__":
    main()

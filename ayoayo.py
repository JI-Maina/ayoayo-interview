class Player:
    def __init__(self, name):
        self.name = name
        self.store = 0 

class Ayoayo:
    def __init__(self):
        self.players = [None, None, None]
        self.board = [[4] * 6, [4] * 6]  
        self.current_player = 1  

    def createPlayer(self, player_name):
        if self.players[1] is None:
            self.players[1] = Player(player_name)
        elif self.players[2] is None:
            self.players[2] = Player(player_name)
        return Player(player_name)

    def printBoard(self):
        print(f"{self.players[1].name}:")
        print(f"Store: {self.players[1].store}")
        print(f"Pits: {self.board[0]}")
        print(f"{self.players[2].name}:")
        print(f"Store: {self.players[2].store}")
        print(f"Pits: {self.board[1]}")
        print("-" * 30)

    def returnWinner(self):
        if sum(self.board[0]) == 0 or sum(self.board[1]) == 0:
            self.players[1].store += sum(self.board[0])
            self.players[2].store += sum(self.board[1])
            self.board = [[0] * 6, [0] * 6]  # Clear the board

            if self.players[1].store > self.players[2].store:
                return f"Winner is player 1: {self.players[1].name}"
            elif self.players[2].store > self.players[1].store:
                return f"Winner is player 2: {self.players[2].name}"
            else:
                return "It's a tie"
        return "Game has not ended"


    def playGame(self, player_index, pit_index):
        if pit_index < 1 or pit_index > 6:
            return "Invalid number for pit index"
        if sum(self.board[0]) == 0 or sum(self.board[1]) == 0:
            return "Game is ended"

        row = 0 if player_index == 1 else 1
        opponent_row = 1 - row
        pit = pit_index - 1
        seeds = self.board[row][pit]

        if seeds == 0:
            return "Invalid move, pit is empty"

        # Remove seeds from selected pit
        self.board[row][pit] = 0
        index = pit

        while seeds > 0:
            # Move to the next pit (forward for Player 1, backward for Player 2)
            if player_index == 1:
                index += 1
            else:
                index -= 1

            # When reaching the store
            if (player_index == 1 and index == 6) or (player_index == 2 and index == -1):
                if player_index == 1:
                    self.players[1].store += 1
                else:
                    self.players[2].store += 1
                seeds -= 1

                if seeds == 0:
                    return f"Player {player_index} takes another turn"

                # Switch to opponent's pits
                row = opponent_row
                if player_index == 1:
                    index = 5
                else:
                    index = 0

                while seeds > 0:
                    if 0 <= index < 6:
                        self.board[row][index] += 1
                        seeds -= 1
                    
                    if player_index == 1:
                        index -= 1
                    else:
                        index += 1

                    # Handle wrap-around to player's own pits after distributing to opponent's pits
                    if seeds > 0 and (index < 0 or index >= 6):
                        row = 0 if player_index == 1 else 1
                        if player_index == 1:
                            index = 0 
                        else:
                            index = 5

            # Distribute seeds to pits
            else:
                if 0 <= index < 6:
                    self.board[row][index] += 1
                    seeds -= 1

                    # Check for the special rule
                if seeds == 0 and row == (0 if player_index == 1 else 1):
                    if self.board[row][index] == 1:
                        opponent_pit = index

                        # Capture opponent's seeds
                        captured_seeds = self.board[opponent_row][opponent_pit]
                        if captured_seeds > 0:
                            if player_index == 1:
                                self.players[1].store += captured_seeds + 1
                            else:
                                self.players[2].store += captured_seeds + 1
                            
                            self.board[row][index] = 0
                            self.board[opponent_row][opponent_pit] = 0

        # Switch turn to the next player
        self.current_player = 3 - player_index
        return self.getBoardState()
                
    def getBoardState(self):
        return [
            *self.board[0], self.players[1].store,
            *self.board[1], self.players[2].store
        ]

def main():
    game = Ayoayo()
    name1 = input("Enter Player 1 Name: ")
    name2 = input("Enter Player 2 Name: ")
    game.createPlayer(name1)
    game.createPlayer(name2)

    while game.returnWinner() == "Game has not ended":
        game.printBoard()
        print(f"{game.players[game.current_player].name}'s turn")
        pit = int(input(f"Choose a pit (1-6): "))
        result = game.playGame(game.current_player, pit)
        print(result)

    game.printBoard()
    print(game.returnWinner())

if __name__ == "__main__":
    main()

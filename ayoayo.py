class Player:
    def __init__(self, name):
        self.name = name
        self.store = 0  # Number of seeds in player's store

class Ayoayo:
    def __init__(self):
        self.players = [None, None, None]  # Fix: Make space for two players
        self.board = [[4] * 6, [4] * 6]  # Two rows of six pits
        self.current_player = 1  # Player 1 starts

    def createPlayer(self, player_name):
        if self.players[1] is None:
            self.players[1] = Player(player_name)
        elif self.players[2] is None:
            self.players[2] = Player(player_name)
        return Player(player_name)  # Fix: Ensure a player is always returned

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

    # def playGame(self, player_index, pit_index):
    #     if pit_index < 1 or pit_index > 6:
    #         return "Invalid number for pit index"
    #     if sum(self.board[0]) == 0 or sum(self.board[1]) == 0:
    #         return "Game is ended"

    #     row = 0 if player_index == 1 else 1  # Current player's row
    #     opponent_row = 1 - row  # Opponent's row
    #     pit = pit_index - 1  # Convert to zero-based index
    #     seeds = self.board[row][pit]

    #     if seeds == 0:
    #         return "Invalid move, pit is empty"

    #     # Remove seeds from selected pit
    #     self.board[row][pit] = 0
    #     index = pit

    #     if player_index == 1:
    #         while seeds > 0:
    #             index += 1

    #             # When reaching the store
    #             if index == 6:
    #                 if player_index == 1:
    #                     self.players[1].store += 1  # Player 1's store
    #                 else:
    #                     self.players[2].store += 1  # Player 2's store
    #                 seeds -= 1

    #                 # If last seed lands in store, give another turn
    #                 if seeds == 0:
    #                     return f"Player {player_index} takes another turn"

    #                 # Switch to opponent's pits after updating the store
    #                 row = opponent_row
    #                 if player_index == 1:
    #                     index = 5  # Start from Player 2's last pit
    #                     print(f"Opponets index reset to {index} {seeds}")
    #                     while seeds > 0:
    #                         self.board[row][index] += 1
    #                         seeds -= 1
    #                         index -= 1
    #                         print(f"Updating opponets {index} {seeds}")
    #                 else:
    #                     index = 0  # Start from Player 1's first pit

    #             # Distribute seeds to pits
    #             else:
    #                 if 0 <= index < 6:
    #                     self.board[row][index] += 1
    #                     seeds -= 1
    #     else:
    #         print(f"player 2 playing index: {index} seeds: {seeds}")
    #         while seeds > 0:
    #             index -= 1  # Move to the previous pit

    #             # When reaching the store (-1th pit)
    #             if index == -1:
    #                 self.players[2].store += 1  # Player 2's store
    #                 seeds -= 1

    #                 # If last seed lands in store, give another turn
    #                 if seeds == 0:
    #                     return f"Player {player_index} takes another turn"

    #                 # Switch to opponent's pits after updating the store
    #                 row = opponent_row
    #                 if player_index == 2:
    #                     index = 0  # Start from Player 2's last pit
    #                     print(f"Opponets index reset to {index} {seeds}")
    #                     while seeds > 0:
    #                         self.board[row][index] += 1
    #                         seeds -= 1
    #                         index += 1
    #                         print(f"Updating opponets {index} {seeds}")
    #                 else:
    #                     index = 0  # Start from Player 1's first pit

    #             # Distribute seeds to the opponent's pits
    #             else:
    #                 if 0 <= index < 6:
    #                     self.board[row][index] += 1
    #                     seeds -= 1
            

    #     # Switch turn to the next player
    #     self.current_player = 3 - player_index
    #     return self.getBoardState()
    def playGame(self, player_index, pit_index):
        if pit_index < 1 or pit_index > 6:
            return "Invalid number for pit index"
        if sum(self.board[0]) == 0 or sum(self.board[1]) == 0:
            return "Game is ended"

        row = 0 if player_index == 1 else 1  # Current player's row
        opponent_row = 1 - row  # Opponent's row
        pit = pit_index - 1  # Convert to zero-based index
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
                    self.players[1].store += 1  # Player 1's store
                else:
                    self.players[2].store += 1  # Player 2's store
                seeds -= 1

                # If last seed lands in store, give another turn
                if seeds == 0:
                    return f"Player {player_index} takes another turn"

                # Switch to opponent's pits
                row = opponent_row
                if player_index == 1:
                    index = 5  # Start from Player 2's last pit
                else:
                    index = 0  # Start from Player 1's first pit

                while seeds > 0:
                    if 0 <= index < 6:
                        self.board[row][index] += 1
                        seeds -= 1
                    # Move to the next pit
                    if player_index == 1:
                        index -= 1
                    else:
                        index += 1

                    # Handle wrap-around to player's own pits after distributing to opponent's pits
                    if seeds > 0 and (index < 0 or index >= 6):
                        # Switch back to player's own pits
                        row = 0 if player_index == 1 else 1
                        if player_index == 1:
                            index = 0  # Start from Player 1's first pit
                        else:
                            index = 5  # Start from Player 2's last pit

            # Distribute seeds to pits
            else:
                if 0 <= index < 6:
                    self.board[row][index] += 1
                    seeds -= 1

                    # Check for the special rule
                if seeds == 0 and row == (0 if player_index == 1 else 1):  # Last seed lands in player's own pit
                    if self.board[row][index] == 1:  # Pit was empty before adding the last seed
                        opponent_pit = index

                        # Capture opponent's seeds
                        captured_seeds = self.board[opponent_row][opponent_pit]
                        if captured_seeds > 0:
                            # Add captured seeds and the last seed to the player's store
                            if player_index == 1:
                                self.players[1].store += captured_seeds + 1
                            else:
                                self.players[2].store += captured_seeds + 1
                            # Empty the pits
                            self.board[row][index] = 0
                            self.board[opponent_row][opponent_pit] = 0

                        print(f"capturing seeds: {seeds} cap: {captured_seeds} || idx: {index} - {opponent_pit}")

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

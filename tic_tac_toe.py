"""This is a tic-tac-toe game module"""


class Game:
    """The tic-tac-toe game class"""
    victory_conditions = ((0, 1, 2), (3, 4, 5), (6, 7, 8),
                          (0, 3, 6), (1, 4, 7), (2, 5, 8),
                          (0, 4, 8), (2, 4, 6))

    def __init__(self):
        print("Welcome to awesome game!\n "
              + "Type the name of the first player,please: ", end="")
        self.first_player_name = input()
        print("Type the name of the second player, please:", end="")
        self.first_player_flag = 'X'
        self.second_player_name = input()
        self.second_player_flag = 'O'
        self._board = {i: "-" for i in range(9)}

    def __str__(self):
        result = ""
        counter = 1
        for i in range(len(self._board)):
            if i == 0 or counter % 3 != 0:
                result += "{case}\t".format(case=self._board[i])
            else:
                result += "{case}\n".format(case=self._board[i])
                counter = 1
                continue
            counter += 1
        return result

    @staticmethod
    def check_for_int(inputted_var):
        """Checks for inputted value of being an integer"""
        while not isinstance(inputted_var, int):
            try:
                inputted_var = int(inputted_var)
                if not 0 < inputted_var < 9:
                    raise ValueError
            except ValueError:
                print("Type the correct input again")
                inputted_var = input()
        return inputted_var -1

    def is_pos_free(self, position):
        """checks whether the chosen position is free or not"""
        if self._board[position] != '-':
            print("It is not possible to set your flag to the position"
                  + f"{position + 1}. Please repeat your choice")
            return False
        return True

    def turn_suggestion(self, i):
        """prompt player to choose next position"""
        if i % 2 == 0:
            print(f"{self.first_player_name}\'s turn."
                  + "Choose your next position: ")
            position = Game.check_for_int(input())
            while not self.is_pos_free(position):
                position = Game.check_for_int(input())
            self._board[position] = self.first_player_flag
            return self.first_player_flag
        print(f"{self.second_player_name}\'s turn."
              + "Choose your next position: ", end="")
        position = Game.check_for_int(input())
        while not self.is_pos_free(position):
            position = Game.check_for_int(input())
        self._board[position] = self.second_player_flag
        return self.second_player_flag

    def check_the_winner(self, flag):
        """Checks if the current state of board satisfies
        victory conditions"""
        for i in self.victory_conditions:
            victory = True
            for j in i:
                if self._board[j] != flag:
                    victory = False
                    break
            if victory:
                return victory
        return victory

    def play(self):
        """Starts  the game and runs until completion"""
        steps_counter = 0
        while True:
            flag = self.turn_suggestion(steps_counter)
            print(self)
            if self.check_the_winner(flag):
                if steps_counter % 2 == 0:
                    print(f"{self.first_player_name} is the Winner!")
                else:
                    print(f"{self.second_player_name} is the Winner!")
                break
            steps_counter += 1
            if steps_counter == len(self._board):
                print("Perfect game.Both of players skilled enough.")
                break


if __name__ == "__main__":
    game = Game()
    game.play()
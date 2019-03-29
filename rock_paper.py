
import random
"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']


class Player:        # The Player class is the parent class for all of
    def move(self):  # the Players class in this game
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class CheaterPlayer(Player):
    def move(self):
        pass

    def learn(self, my_move, their_move):
        pass


class RandomPlayer(Player):  # It's a subclass of Player class
    def move(self):          # It plays randomly
        return random.choice(moves)

    def learn(self, my_move, their_move):
        pass


class ReflectPlayer(Player):  # It's a subclass of Player class. It remembers
    def __init__(self):       # what move the opponent played last round and
        self.my_move = RandomPlayer().move()  # that will be its next move.

    def move(self):
        return self.my_move

    def learn(self, my_move, their_move):
        self.my_move = my_move


class CyclePlayer(Player):  # It's a subclass of Player class. It remembers
    def __init__(self):    # what move it played last round, and cycles through
        self.their_move = RandomPlayer().move()  # the different moves.

    def move(self):
        return self.their_move

    def learn(self, my_move, their_move):
        index = moves.index(their_move)
        if index < 2:
            self.their_move = moves[index + 1]
        else:
            self.their_move = moves[0]


class HumanPlayer(Player):  # It's a subclass of Player class. Asks the human
    def move(self):     # user what move to make.
        while True:
            hplayer = input("Rock, paper, scissors? >> ")
            hplayer = hplayer.strip()
            if (hplayer.lower() == "rock" or
               hplayer.lower() == "paper" or
               hplayer.lower() == "scissors"):
                break
        return hplayer.lower()


class Game:  # Put values into instance variables when we create a new
    def __init__(self, p1, p2, p3, p4, p5, p6):  # game object in the memory
        self.p1 = p1
        self.p2, self.p3, self.p4, self.p5, self.p6 = p2, p3, p4, p5, p6
        self.human_score = 0
        self.computer_score = 0
        self.human_name = ""
        self.play_again = ""

    def beats(self, one, two):  # Tells whether one move beats another one.
        if ((one == 'rock' and two == 'scissors') or
           (one == 'scissors' and two == 'paper') or
           (one == 'paper' and two == 'rock')):
            self.human_score += 1
            win = f"** {self.human_name.upper()} WINS **"
        elif ((one == 'rock' and two == 'rock') or
              (one == 'scissors' and two == 'scissors') or
              (one == 'paper' and two == 'paper')):
            win = '** TIE **'
        else:
            self.computer_score += 1
            win = '** COMPUTER WINS **'
        print(f">>{self.human_name} played {one}.\n>>Computer played"
              f" {two}.\n{win}")
        print(f"Score: {self.human_name} {self.human_score},"
              f" Computer {self.computer_score}")

    def play_round(self, opponent):  # It collects the movements and sends
        move1 = self.p1.move()       # them to evaluate
        if opponent == self.p6:
            move2 = self.cheating(move1)  # cheating :)
        else:
            move2 = opponent.move()
        self.beats(move1, move2)
        opponent.learn(move1, move2)

    def play_game(self):  # It calls methods where ask user about their name,
        if not self.play_again:  # rounds to play and type of opponents.
            self.welcome()
        opponent = self.opponent()
        plays = self.plays()
        for round in range(1, plays):
            print(f"\nRound {round}:")
            self.play_round(opponent)
        self.the_end()

    def welcome(self):  # Set the user name.
        print("Welcome to this game. Rock Paper Scissors, Go!")
        welcome = input("What's your name? (max. 6 char).>> ")
        while len(welcome) > 6 or not welcome.strip():
            welcome = input("Please type less than 6 characters.>> ")
        self.human_name = welcome.title().strip()

    def opponent(self):  # Set the game type.
        print("\nWhich computer player do you want to play with? (1-5).")
        games = input("1. COMP1 - Static\n2. COMP2 - Random\n"
                      "3. COMP3 - Reflect\n4. COMP4 - Cycle\n"
                      "5. COMP5 - You never win :)\n>> ")
        while (games.strip() != '1' and games.strip() != '2'
               and games.strip() != '3' and games.strip() != '4'
               and games.strip() != '5'):
            games = input("Please chose 1, 2, 3, 4 or 5: >> ")
        games = games.strip()
        if games == '1':
            opponent = self.p2
        elif games == '2':
            opponent = self.p3
        elif games == '3':
            opponent = self.p4
        elif games == '4':
            opponent = self.p5
        else:
            opponent = self.p6
        return opponent

    def plays(self):  # Set the game rouds.
        plays = input("\nHow many rounds do you want to play? (max.9).>> ")
        try:
            while int(plays) > 9 or int(plays) <= 0:
                plays = input("Please key in a number between 1 and 9.>> ")
            plays = int(plays) + 1
        except ValueError:
            print("Oh well, as you did't chose a number"
                  " we assigned you the default 3 rounds.")
            plays = 4
        return plays

    def the_end(self):  # The end of game user can play again or finish
        self.score_board(self.human_score, self.computer_score)  # the game
        print("Game over!")
        play_again = input("Would you like to play again?(y/n) >> ")
        while (play_again.lower().strip() != 'y' and
               play_again.lower().strip() != 'n'):
            play_again = input("Please chose('y/n'). >> ")
        play_again = play_again.strip()
        if play_again == 'y':
            self.human_score = 0
            self.computer_score = 0
            self.play_again = 'True'
            self.play_game()
        else:
            exit()

    def score_board(self, score1, score2):  # The final score
        if score1 > score2:
            text = "** You WON this game! **"
        elif score1 < score2:
            text = "** You LOST this game! **"
        else:
            text = "** Nobody won this game it's a TIE **"
        print(f"\n{text}\nFinal score:\n{self.human_name} {score1} vs "
              f"Computer {score2}\n")

    def cheating(self, move1):
        if move1 == "rock":
            move2 = "paper"
        elif move1 == "paper":
            move2 = "scissors"
        else:
            move2 = "rock"
        return move2


if __name__ == '__main__':  # It creates a game object and calls one of the
    game = Game(HumanPlayer(), Player(), RandomPlayer(),  # game class methods
                ReflectPlayer(), CyclePlayer(), CheaterPlayer())
    game.play_game()

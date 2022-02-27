import random

class WordGame():
    def __init__(self, rounds: int):
        self.wins1 = 0
        self.wins2 = 0
        self.rounds = rounds

    def round_winner(self, player1_word: str, player2_word: str):
        # determine a random winner
        return random.randint(1, 2)

    def play(self):
        print("Word game:")
        for i in range(1, self.rounds+1):
            print(f"round {i}")
            answer1 = input("player1: ")
            answer2 = input("player2: ")

            if self.round_winner(answer1, answer2) == 1:
                self.wins1 += 1
                print("player 1 won")
            elif self.round_winner(answer1, answer2) == 2:
                self.wins2 += 1
                print("player 2 won")
            else:
                pass # it"s a tie

        print("game over, wins:")
        print(f"player 1: {self.wins1}")
        print(f"player 2: {self.wins2}")

class LongestWord(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)
    
    def round_winner(self, player1_word: str, player2_word: str):
        if len(player1_word) > len(player2_word):
            return 1
        elif len(player2_word) > len(player1_word):
            return 2
        else:
            return None

class MostVowels(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)
    
    def round_winner(self, player1_word: str, player2_word: str):
        player1_vowels = self.__countVowels(player1_word)
        player2_vowels = self.__countVowels(player2_word)
        if player1_vowels > player2_vowels:
            return 1
        elif player2_vowels > player1_vowels:
            return 2
        else:
            return None

    def __countVowels(self, word: str):
        count = 0
        for letter in word:
            if letter in "aeiou":
                count +=1
        return count

class RockPaperScissors(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)
    
    def __is_valid(self, word: str):
        if word in ("rock", "paper", "scissors"):
            return True
        return False

    def round_winner(self, player1_word: str, player2_word: str):
        if (self.__is_valid(player1_word) == True) and (self.__is_valid(player2_word) == True):
            if player1_word == player2_word:
                return None
            elif ((player1_word == "rock" and player2_word == "scissors") or 
                (player1_word == "paper" and player2_word == "rock") or 
                    (player1_word == "scissors" and player2_word == "paper")):
                return 1
            else:
                return 2
        elif self.__is_valid(player1_word):
            return 1
        elif self.__is_valid(player2_word):
            return 2
        else:
            return None
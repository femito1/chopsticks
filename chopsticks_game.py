class Player:
    def __init__(self, name):
        self.name = name
        self.hands = [1, 1]  # Start with 1 finger on each hand

    def is_alive(self):
        return any(0 < hand < 5 for hand in self.hands)

    def has_valid_hand(self):
        return any(0 < hand < 5 for hand in self.hands)

    def can_split(self):
        return (self.hands[0] == 0 and self.hands[1] % 2 == 0 and self.hands[1] > 0) or \
               (self.hands[1] == 0 and self.hands[0] % 2 == 0 and self.hands[0] > 0)

class ChopsticksGame:
    def __init__(self, player1_name, player2_name):
        self.players = [Player(player1_name), Player(player2_name)]
        self.current_player = 0
        self.hand_dict = {"left": 0, "right": 1, "r": 1, "l": 0, 0:0, 1:1}

    def play_turn(self):

        attacker = self.players[self.current_player]
        defender = self.players[1 - self.current_player]

        print(f"\n{attacker.name}'s turn")
        self.display_game_state()

        if not attacker.has_valid_hand():
            print(f"{attacker.name} has no valid hands to play. Skipping turn.")
            self.current_player = 1 - self.current_player
            return

        if attacker.can_split():
            action = input("Do you want to (a)ttack or (s)plit? ").lower()
            if action == 's':
                self.split(attacker)
                return
        if attacker.hands[0] == 0 or attacker.hands[1] == 0:
            ind = attacker.hands.index(0)
            attacking_hand = self.choose_hand(f"Only available hand to attack with: {self.hand_dict[1 - ind]} ", attacker, forced=1 - ind)
        else:
            attacking_hand = self.choose_hand(f"Choose your attacking hand,nand (l)eft or (r)ight: ", attacker)
        if defender.hands[0] == 0 or defender.hands[1] == 0:
            ind = defender.hands.index(0)
            defending_hand = self.choose_hand(f"Only one of {defender.name}'s hand to attack ({self.hand_dict[1 - ind]}): ", defender, forced= 1-ind)
        else:
            defending_hand = self.choose_hand(f"Choose {defender.name}'s hand to attack, (l)eft or (r)ight: ", defender)

        defender.hands[defending_hand] = (defender.hands[defending_hand] + attacker.hands[attacking_hand]) % 5
        self.current_player = 1 - self.current_player

    def split(self, player):
        if player.hands[0] == 0:
            fingers = player.hands[1] // 2
            player.hands = [fingers, fingers]
        else:
            fingers = player.hands[0] // 2
            player.hands = [fingers, fingers]
        self.current_player = 1 - self.current_player
        print(f"{player.name} split their fingers.")

    def choose_hand(self, prompt, player, forced=None):
        while True:
            try:
                x = input(prompt)
                x = int(x) if x.isdigit() else self.hand_dict[x]
                choice = forced if forced is not None else x
                if choice in {0, 1} and player.hands[choice] > 0:
                    return choice
                else:
                    print("Invalid choice. Please choose left (0) or right (1) for a valid hand (1-4 fingers).")
                    
            except ValueError:
                print("Invalid input. Please enter left (0) or right (1).")

    def display_game_state(self):
        for player in self.players:
            print(f"{player.name}: {player.hands}")

    def play_game(self):
        while all(player.is_alive() for player in self.players):
            self.play_turn()

        winner = self.players[1 - self.current_player]
        print(f"\nGame Over! {winner.name} wins!")

if __name__ == "__main__":
    p1_name = input("Enter Player 1's name: ")
    p2_name = input("Enter Player 2's name: ")
    game = ChopsticksGame(p1_name, p2_name)
    game.play_game()





print("   ___________\n"
      "   |          |\n"
      "___|          |\n"
      "\  |          |\n"
      " \ |__________|")

print("   |-| |-| |-|       \n"
      "   | | | | | |     \n"
      "    ___________\n"
      "   |          |\n"
      "___|          |\n"
      "\  |          |\n"
      " \ |__________|")
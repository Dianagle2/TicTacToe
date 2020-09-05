class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def get_name(self):
        return self.name
    
    def get_symbol(self):
        return self.symbol
    
    def ask_move(self):
        raise NotImplementedError


class HumanPlayer(Player):
    def ask_move(self):
        movement = input("Please enter your move: ")
        # TODO: Add input check
        return movement

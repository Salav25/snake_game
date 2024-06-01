from src.game import game
from src.instrastructure import Infrastructure

if __name__ == "__main__":
    game = game(Infrastructure())
    game.loop()

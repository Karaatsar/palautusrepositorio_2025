import requests
from player import Player

class PlayerReader:
    def __init__(self, url):
        self.__url = url

    def get_players(self):
        response = requests.get(self.__url).json()
        players = [Player(player_data) for player_data in response]
        return players

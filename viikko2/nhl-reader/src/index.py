import requests
from player import Player

def main():
    url="https://studies.cs.helsinki.fi/nhlstats/2024-25/players"
    response = requests.get(url).json()

    players = [Player(player_data) for player_data in response]

    finnish_players = [player for player in players if player.nationality=="FIN"]

    sorted_finnish_players = sorted(finnish_players, key=lambda player: player.goals + player.assists, reverse=True)

    print("players from FIN:\n")
    for player in sorted_finnish_players:
        print(player)
if __name__ == "__main__":
    main()

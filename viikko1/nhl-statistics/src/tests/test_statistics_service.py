from statistics_service import StatisticsService

from player import Player

def test_two_consecutive_calculations():
    players=[
        Player["Saku", "MTL", 10, 20],
        Player["Teemu", "ANA", 15, 25]
    ]
    stats= StatisticsService(players)

    player1=stats.search("Saku")
    player2=stats.search("Teemu")

    assert player1.points(30)
    assert player2.points(40)
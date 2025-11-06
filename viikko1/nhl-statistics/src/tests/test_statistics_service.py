from statistics_service import StatisticsService

from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Saku", "MTL", 10, 20),
            Player("Teemu", "ANA", 15,25)
        ]
    
    def test_two_calculations():
        reader_stub= PlayerReaderStub()
        stats = StatisticsService()
        stats._players = reader_stub.get_players()

        player1=stats.search("Saku")
        player2=stats.search("Teemu")

        assert player1.points==30
        assert player2.points==40

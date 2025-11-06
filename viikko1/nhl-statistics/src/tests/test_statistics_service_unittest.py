import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),  #  4+12 = 16
            Player("Lemieux", "PIT", 45, 54), # 45+54 = 99
            Player("Kurri",   "EDM", 37, 53), # 37+53 = 90
            Player("Yzerman", "DET", 42, 56), # 42+56 = 98
            Player("Gretzky", "EDM", 35, 89)  # 35+89 = 124
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )
    def test_search_existing_player(self):
        player= self.stats.search("Gretzky")
        self.assertIsNotNone(player)
        self.assertEqual(player.name, "Gretzky")
    
    def test_search_non_existing_player(self):
        player=self.stats.search("Atsar")
        self.assertIsNone(player)
    
    def test_team_players(self):
        team_players=self.stats.team("EDM")
        self.assertEqual(len(team_players), 3)
        names = [player.name for player in team_players]
        self.assertIn("Gretzky", names)
        self.assertIn("Semenko", names)
        self.assertIn("Kurri", names)
    
    def test_top_scorers(self):
        top_scorers=self.stats.top_scorers(2)
        self.assertEqual(len(top_scorers), 3)
        self.assertEqual(top_scorers[0].name, "Gretzky")  # 124 points
        self.assertEqual(top_scorers[1].name, "Lemieux")  # 99 points
        self.assertEqual(top_scorers[2].name, "Yzerman")  # 98 points
    
    if __name__=="__main__":
        unittest.main()
        
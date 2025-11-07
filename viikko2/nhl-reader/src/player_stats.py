class PlayerStats:
    def __init__(self, reader):
        self.__players = reader.get_players()
    
    def top_scorers(self, nationality):
        filtered = [p for p in self.__players if p.nationality == nationality]
        sorted_players = sorted(filtered, key=lambda p: p.goals + p.assists, reverse=True)
        return sorted_players

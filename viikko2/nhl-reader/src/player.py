class Player:
    def __init__(self, data):
        self.name=data["name"]
        self.nationality=data["nationality"]
        self.team=data["team"]
        self.goals=data["goals"]
        self.assists=data["assists"]

    
    def __str__(self):
        return f"{self.name:20}{self.team:10}{self.goals:2}+{self.assists:2}={self.goals + self.assists}"
    

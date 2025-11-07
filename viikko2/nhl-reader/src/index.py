from player import Player
from rich.console import Console
from rich.table import Table
from player_reader import PlayerReader
from player_stats import PlayerStats

def main():
    console = Console()

    console.print("NHL Player Stats", style="bold underline magenta")
    season = input("Enter the NHL season (e.g., 2024-25): ").strip()
    nationality = input("enter nationality (e.g., FIN, SWE, USA): ").strip().upper()

    url="https://studies.cs.helsinki.fi/nhlstats/2024-25/players"

    console.print(f"Fetching data for the {season} season...\n", style="italic cyan")

    try:
        reader = PlayerReader(url)
        stats= PlayerStats(reader)
        players = stats.top_scorers(nationality)

        if not players:
            console.print(f"No players found for nationality '{nationaluty}'", style="pink")
            return
        
        table = Table(title=f"Top Scorers from {nationality} in {season} Season")
        table.add_column("Name", style="white", justify="left")
        table.add_column("Team", style="magenta")
        table.add_column("Goals", style="green", justify="right")
        table.add_column("Assists", style="blue", justify="right")
        table.add_column("Points", style="yellow", justify="right")

        for player in players: 
            table.add_row(
                player.name, 
                player.team, 
                str(player.goals), 
                str(player.assists),
                str(player.total_points()),
            )
        console.print(table)

    except Exeption as e:
        console.print(f"An error occurred: {e}", style="bold red")

    

if __name__ == "__main__":
    main()

"""RPS-001: the rules for Rock, Paper, Scissors."""


def determine_winner(player: str, computer: str) -> str:
    """Return 'win', 'lose', or 'tie' from the player's perspective."""
    if player == computer:
        return "tie"

    winning_moves = {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper",
    }

    if winning_moves[player] == computer:
        return "win"

    return "lose"

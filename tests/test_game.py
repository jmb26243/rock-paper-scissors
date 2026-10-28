"""Unit tests for the Rock, Paper, Scissors rules."""

import pytest
import app as web
from game import determine_winner

# pylint:disable=redefined-outer-name

pytestmark = pytest.mark.unit


@pytest.mark.parametrize(
    ("player", "computer", "expected"),
    [
        ("rock", "rock", "tie"),
        ("rock", "paper", "lose"),
        ("rock", "scissors", "win"),
        ("paper", "rock", "win"),
        ("paper", "paper", "tie"),
        ("paper", "scissors", "lose"),
        ("scissors", "rock", "lose"),
        ("scissors", "paper", "win"),
        ("scissors", "scissors", "tie"),
    ],
)
def test_determine_winner(player, computer, expected):
    """Return the expected outcome for each valid matchup."""
    assert determine_winner(player, computer) == expected


@pytest.fixture
def game_client():
    """Create a Flask test client."""
    web.app.config.update(TESTING=True)
    return web.app.test_client()


@pytest.mark.integration
def test_real_request_displays_correct_result(game_client, monkeypatch):
    """Display the actual rule result for a submitted round."""
    monkeypatch.setattr(web.random, "choice", lambda _moves: "paper")

    response = game_client.post("/", data={"move": "rock"})

    page = response.get_data(as_text=True)

    assert response.status_code == 200
    assert "You chose" in page
    assert "Computer chose" in page
    assert "Rock" in page
    assert "Paper" in page
    assert "Computer wins" in page
    assert 'data-outcome="lose"' in page

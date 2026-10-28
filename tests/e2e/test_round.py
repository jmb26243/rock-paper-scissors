"""Real-browser tests for playing and replaying a round."""

import pytest
from playwright.sync_api import Page, expect

import app as web

pytestmark = pytest.mark.e2e


def test_play_round_and_replay(page: Page, live_server, monkeypatch):
    """Play a real round, then play another independent round."""
    monkeypatch.setattr(web.random, "choice", lambda _moves: "paper")

    page.goto(live_server)

    page.get_by_role("button", name="Rock", exact=True).click()

    expect(page.get_by_label("This round’s choices")).to_be_visible()
    expect(page.get_by_text("You chose", exact=True)).to_be_visible()
    expect(page.get_by_text("Computer chose", exact=True)).to_be_visible()
    expect(page.get_by_role("region", name="Computer wins")).to_be_visible()
    expect(page.locator('[data-outcome="lose"]')).to_have_count(1)

    page.get_by_role("button", name="Scissors", exact=True).click()

    expect(page.get_by_label("This round’s choices")).to_be_visible()
    expect(page.get_by_role("region", name="You win!")).to_be_visible()
    expect(page.locator('[data-outcome="win"]')).to_have_count(1)

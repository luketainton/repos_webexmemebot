#!/usr/bin/env python3

"""Provides test cases for webexmemebot/img.py."""

from webex_bot.models.response import Response  # pragma: no cover

from app import meme  # pragma: no cover


def test_adaptive_card_create() -> None:
    """Test to ensure that the adaptive card is created."""
    command = meme.MakeMemeCommand()
    result = command.execute(None, None, None)
    assert isinstance(result, Response)


def test_error_true() -> None:
    """Test to ensure that execute() exits when error=True."""
    callback = meme.MakeMemeCallback()
    callback.error = True
    result = callback.execute(None, None, None)
    assert result is None


def test_error_false() -> None:
    """Test to ensure that execute() completes when error=False."""
    callback = meme.MakeMemeCallback()
    callback.meme = "oprah.png"
    callback.text_top = "TEST"
    callback.text_bottom = "TEST"
    result: Response = callback.execute(None, None, {"target": {"globalId": "TEST"}})
    assert isinstance(result, Response) and result.roomId == "TEST" and result.files[0] == callback.meme_filename

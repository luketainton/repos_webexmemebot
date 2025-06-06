"""Provides test cases for app/config.py."""

import os

env_vars: dict = {
    "APP_VERSION": "dev",
    "WEBEX_API_KEY": "testing",
}


for var, value in env_vars.items():
    os.environ[var] = value

# needs to be imported AFTER environment variables are set
from app.config import (
    config,
)  # pylint: disable=wrong-import-position # pragma: no cover  # noqa: E402


def test_config() -> None:
    """Test the configuration settings."""
    assert config.webex_token == env_vars["WEBEX_API_KEY"]
    assert config.version == env_vars["APP_VERSION"]

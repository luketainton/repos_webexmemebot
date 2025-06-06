"""Command module for handling the 'exit' command in the Webex meme bot."""

from webex_bot.models.command import Command


class ExitCommand(Command):
    """Command to handle the 'exit' command in the Webex meme bot."""

    def __init__(self) -> None:
        """Initialize the ExitCommand with command keyword and help message."""
        super().__init__(
            command_keyword="exit",
            help_message="Exit",
            delete_previous_message=True,
        )
        self.sender: str = ""

    def pre_execute(self, message, attachment_actions, activity) -> None:  # pylint: disable=unused-argument
        """Pre-execution logic for the exit command."""
        return

    def execute(self, message, attachment_actions, activity) -> None:  # pylint: disable=unused-argument
        """Execute the exit command."""
        return

    def post_execute(self, message, attachment_actions, activity) -> None:  # pylint: disable=unused-argument
        """Post-execution logic for the exit command."""
        return

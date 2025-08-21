from .base_agent import BaseAgent

HELP_TEXT = (
    """
Available commands:
  • balance  - Show current balance
  • deposit  - Add money to your account
  • withdraw - Remove money from your account
  • help     - Show this help
  • exit     - Quit the program
""".strip()
)

class HelpAgent(BaseAgent):
    def handle(self):
        self.respond_ok("Showing help.")
        print(HELP_TEXT)

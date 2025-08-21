from .base_agent import BaseAgent

class BalanceAgent(BaseAgent):
    def handle(self):
        bal = self.context.balance
        currency = self.context.currency
        if bal < 0:
            self.respond_warn("Your account is overdrawn. Please deposit funds soon.")
        self.respond_ok(f"Your current balance is: {bal:.2f} {currency}")

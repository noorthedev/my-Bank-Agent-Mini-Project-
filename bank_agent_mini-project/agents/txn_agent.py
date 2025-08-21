from .base_agent import BaseAgent
from utils.guardrails import is_positive_amount, enforce_limits

class TransactionAgent(BaseAgent):
    def handle(self, txn_type: str):
        raw = input(f"Enter amount to {txn_type}: ").strip()
        ok_amount, amount, err = is_positive_amount(raw)
        if not ok_amount:
            self.respond_error(err)
            return

        if txn_type == "deposit":
            ok_limit, msg = enforce_limits(amount, self.context.deposit_limit, "deposit")
            if not ok_limit:
                self.respond_warn(msg)
                return
            self.context.balance += amount
            self.respond_ok(f"Deposited {amount:.2f}. New balance: {self.context.balance:.2f} {self.context.currency}")
        elif txn_type == "withdraw":
            ok_limit, msg = enforce_limits(amount, self.context.withdraw_limit, "withdraw")
            if not ok_limit:
                self.respond_warn(msg)
                return
            if amount > self.context.balance:
                self.respond_error("Insufficient funds.")
                return
            self.context.balance -= amount
            self.respond_ok(f"Withdrawn {amount:.2f}. New balance: {self.context.balance:.2f} {self.context.currency}")
        else:
            self.respond_error("Unsupported transaction type.")

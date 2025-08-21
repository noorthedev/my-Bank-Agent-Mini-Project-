import json
from utils.context import Context
from agents.bank_agent import BankAgent

def load_context_from_file(path: str) -> Context:
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return Context(
        user_name=data.get("user_name", "User"),
        account_number=data.get("account_number", "0000000000"),
        currency=data.get("currency", "PKR"),
        balance=float(data.get("balance", 0.0)),
        withdraw_limit=float(data.get("withdraw_limit", 50000.0)),
        deposit_limit=float(data.get("deposit_limit", 1000000.0)),
    )

if __name__ == "__main__":
    ctx = load_context_from_file("data/account.json")
    app = BankAgent(ctx)
    app.run()

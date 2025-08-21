from dataclasses import dataclass, field

@dataclass
class Context:
    user_name: str
    account_number: str
    currency: str = "PKR"
    balance: float = 0.0
    withdraw_limit: float = 50000.0
    deposit_limit: float = 1000000.0
    meta: dict = field(default_factory=dict)

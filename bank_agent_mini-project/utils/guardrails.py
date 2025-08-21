from typing import Iterable

ALLOWED_COMMANDS = {"balance", "deposit", "withdraw", "help", "exit"}

def is_valid_command(cmd: str) -> bool:
    return cmd.strip().lower() in ALLOWED_COMMANDS

def sanitize_command(cmd: str) -> str:
    return cmd.strip().lower()

def is_positive_amount(raw: str) -> tuple[bool, float | None, str | None]:
    try:
        value = float(raw.strip())
        if value <= 0:
            return False, None, "Amount must be greater than 0."
        return True, value, None
    except Exception:
        return False, None, "Please enter a valid number (e.g., 2500)."

def is_valid_account_number(acc: str) -> bool:
    acc = acc.strip()
    return len(acc) == 10 and acc.isdigit()

def enforce_limits(value: float, limit: float, kind: str) -> tuple[bool, str | None]:
    if value > limit:
        return False, f"{kind.capitalize()} limit exceeded. Max allowed is {limit:.2f}."
    return True, None

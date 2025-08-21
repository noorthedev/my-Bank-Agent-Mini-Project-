from typing import Literal

Level = Literal["ok", "warn", "error"]

def render(level: Level, message: str) -> str:
    prefix = {
        "ok": "✅ ",
        "warn": "⚠️ ",
        "error": "❌ ",
    }.get(level, "")
    return f"{prefix}{message}"

def ok(msg: str) -> str:
    return render("ok", msg)

def warn(msg: str) -> str:
    return render("warn", msg)

def error(msg: str) -> str:
    # Hide raw/internal details from end-users; keep messages friendly and bounded
    safe = msg.strip().splitlines()[0][:300]
    return render("error", safe)

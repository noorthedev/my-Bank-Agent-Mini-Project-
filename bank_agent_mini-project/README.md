# Bank Agent Mini Project (CLI)

This is a **ready-to-run** mini project demonstrating:
- Proper **input guardrails** (validation + sanitization)
- Proper **output guardrails** (controlled, consistent responses)
- **At least 2 handoff agents** (BalanceAgent, TransactionAgent; plus HelpAgent as an extra)
- A clear and meaningful **context** shared across agents

## 🏁 Quick Start

1) Make sure you have Python 3.9+ installed.
2) (Optional) Create and activate a virtual environment.
3) Install requirements (only `python-dotenv`, but project runs fine without a `.env`):  
   ```bash
   pip install -r requirements.txt
   ```
4) Run:
   ```bash
   python bank.py
   ```

## 🧱 Project Structure
```
bank_agent_project/
│── bank.py
│── README.md
│── requirements.txt
│── data/
│   └── account.json
│── agents/
│   ├── __init__.py
│   ├── base_agent.py
│   ├── bank_agent.py
│   ├── balance_agent.py
│   ├── txn_agent.py
│   └── help_agent.py
└── utils/
    ├── context.py
    ├── guardrails.py
    └── output_policies.py
```

## ✨ Notes
- No external LLMs or APIs are required. This is a pure Python CLI.
- Guardrails demonstrate **how** to validate inputs, constrain outputs, and protect logic flow.
- `output_policies.py` centralizes response formatting to ensure consistency (success/warn/error patterns).

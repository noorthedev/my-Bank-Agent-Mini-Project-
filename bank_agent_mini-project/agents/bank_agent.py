from .balance_agent import BalanceAgent
from .txn_agent import TransactionAgent
from .help_agent import HelpAgent
from utils.guardrails import is_valid_command, sanitize_command
from utils.output_policies import ok, warn, error

class BankAgent:
    def __init__(self, context):
        self.context = context
        self.balance_agent = BalanceAgent(context)
        self.txn_agent = TransactionAgent(context)
        self.help_agent = HelpAgent(context)

    def greet(self):
        print(ok(f"Welcome, {self.context.user_name}! ✨"))
        print("Type 'help' to see available commands.\n")

    def run(self):
        self.greet()
        while True:
            try:
                raw = input("How can I help you? (balance/deposit/withdraw/help/exit): ")
                if not is_valid_command(raw):
                    print(warn("Invalid choice. Type 'help' to see options."))
                    continue
                cmd = sanitize_command(raw)
                if cmd == "balance":
                    self.balance_agent.handle()
                elif cmd in ("deposit", "withdraw"):
                    self.txn_agent.handle(cmd)
                elif cmd == "help":
                    self.help_agent.handle()
                elif cmd == "exit":
                    print(ok("Goodbye!"))
                    break
            except KeyboardInterrupt:
                print("\n" + warn("Interrupted. Type 'exit' next time to quit safely."))
                break
            except Exception:
                # Do not expose raw errors
                print(error("Something went wrong, but your data is safe. Please try again."))

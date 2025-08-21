from utils.output_policies import ok, warn, error

class BaseAgent:
    def __init__(self, context):
        self.context = context

    def respond_ok(self, msg: str):
        print(ok(msg))

    def respond_warn(self, msg: str):
        print(warn(msg))

    def respond_error(self, msg: str):
        print(error(msg))

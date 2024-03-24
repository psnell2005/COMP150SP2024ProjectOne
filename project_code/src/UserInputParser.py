class UserInputParser:

    def __init__(self):
        self.style = "console"

    def parse(self, prompt) -> str:
        return input(prompt)
      
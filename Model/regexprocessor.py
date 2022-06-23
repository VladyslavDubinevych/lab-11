import re

class RegexProcessor:
    def __init__(self, pattern: str) -> None:
        self.pattern = pattern
    
    def __str__(self) -> str:
        return f"Regular Expression Processor with \"{self.pattern}\" pattern"

    def __repr__(self) -> str:
        return f"RegexProcessor(pattern: str = {self.pattern})"

    def amount_of_occurrances(self, input: str) -> int:
        amount = 0
        for objects in re.findall(self.pattern, input):
            amount += 1
        return amount
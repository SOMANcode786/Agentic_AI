from dataclasses import dataclass
from typing import ClassVar

@dataclass
class American:
    name: str
    age: int
    language: ClassVar[str] = "English"

    def eats(self):
        return f"{self.name} eats hamburgers."

    def speak(self):
        return f"{self.name} is speaking .. {American.language}"
    
    @staticmethod
    def get_language():  # renamed to avoid conflict
        return American.language

john = American(name="john", age=25)
# print(john.speak())           # ✅ john is speaking .. English
# print(john.eats())            # ✅ john eats hamburgers.
print(American.get_language())  # ✅ English

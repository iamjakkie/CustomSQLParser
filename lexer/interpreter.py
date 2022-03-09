from abc import ABC, abstractmethod

# from Pickuery_structures.ast import AST
from CustomSQLParser.lexer.tokenizer import SnowflakeTokenizer


class Interpreter(ABC):
    @abstractmethod
    def __init__(self, tokenizer):
        self.tokenizer = tokenizer
    
    @abstractmethod
    def translate_query(self, query) -> None:
        print(self.tokenizer)
        tokens = self.tokenizer.tokenize(query)
        for token in tokens:
            print(token)

class SnowflakeInterpreter(Interpreter):
    def __init__(self):
        super().__init__(SnowflakeTokenizer)

    def translate_query(self, query) -> None:
        return super().translate_query(query)
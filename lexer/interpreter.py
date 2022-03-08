from abc import ABC, abstractmethod

from Pickuery_structures.ast import AST
from CustomSQLParser.lexer.tokenizer import Tokenizer


class Interpreter(ABC):
    @abstractmethod
    def __init__(self, tokenizer):
        self.tokenizer = tokenizer
    
    @abstractmethod
    def translate_query(self, query) -> AST:
        ...
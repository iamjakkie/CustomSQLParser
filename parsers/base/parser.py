from abc import ABC, abstractmethod
from dataclasses import dataclass
from Pickuery_structures.ast import AST
import json

@dataclass 
class ParsedQuery(ABC):
    query: str
    ast: AST #TODO: AST structure
    internal_representation: json 

class Parser(ABC):
    @abstractmethod
    def __init__(self):
        ...

    @abstractmethod
    def parseSQL(query:str) -> ParsedQuery:
        ...

    @abstractmethod
    def generateAST(query:str) -> AST:
        ...

    
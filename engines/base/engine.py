from abc import ABC, abstractmethod
import json

class Engine(ABC):
    @abstractmethod
    def __init__(self):
        ...

    @abstractmethod
    def parseSQL(query:str):
        ...

@dataclass 
class ParsedQuery(ABC):
    ast: str #TODO: AST structure
    internal_representation: json 
    
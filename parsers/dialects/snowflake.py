from dataclasses import dataclass
from CustomSQLParser.parsers.base.parser import Parser, ParsedQuery
from Pickuery_structures.ast import AST


class Snowflake_Parser(Parser):
    def __init__(self):
        pass

    def parseSQL(self, query: str):
        ast = self.generateAST(query)
        return ParsedQuery(query, ast, ast.generateJSON()) 

    def generateAST(self, query: str) -> AST:
        return AST

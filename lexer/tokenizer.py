from abc import ABC, abstractmethod
from typing import List
from CustomSQLParser.lexer.token import Token
from CustomSQLParser.lexer.token import SnowflakeTokenType, SnowflakeToken
# from CustomSQLParser.Pickuery_structures.ast import AST

class Tokenizer():
    @abstractmethod
    def __init__(self, tokentype, token) -> None:
        self.tokentype = tokentype
        self.tokenfamily = token
        #TODO: move tokens to single data structure in token
        self.SINGLE_TOKENS = {
            "(": self.tokentype.LEFTPAREN,
            ")": self.tokentype.RIGHTPAREN,
            ":": self.tokentype.COLON,
            ",": self.tokentype.COMMA,
            ".": self.tokentype.DOT,
            "-": self.tokentype.DASH,
            "=": self.tokentype.EQ,
            ">": self.tokentype.GT,
            "<": self.tokentype.LT,
            "%": self.tokentype.MOD,
            "!": self.tokentype.NOT,
            "+": self.tokentype.PLUS,
            ";": self.tokentype.SEMICOLON,
            "/": self.tokentype.SLASH,
            "*": self.tokentype.STAR,
        }
        self.KEYWORDS = {
            "(": self.tokentype.LEFTPAREN,
            ")": self.tokentype.RIGHTPAREN,
            ":": self.tokentype.COLON,
            ",": self.tokentype.COMMA,
            ".": self.tokentype.DOT,
            "-": self.tokentype.DASH,
            "=": self.tokentype.EQ,
            ">": self.tokentype.GT,
            "<": self.tokentype.LT,
            "%": self.tokentype.MOD,
            "!": self.tokentype.NOT,
            "+": self.tokentype.PLUS,
            ";": self.tokentype.SEMICOLON,
            "/": self.tokentype.SLASH,
            "*": self.tokentype.STAR,
            "--": self.tokentype.COMMENT_SINGLE,
            "/*": self.tokentype.COMMENT_START,
            "*/": self.tokentype.COMMENT_END,
            "==": self.tokentype.EQ,
            ">=": self.tokentype.GTE,
            "<=": self.tokentype.LTE,
            "<>": self.tokentype.NEQ,
            "!=": self.tokentype.NEQ,
            "ALTER": self.tokentype.ALTER,
            "AND": self.tokentype.AND,
            "ASC": self.tokentype.ASC,
            "AS": self.tokentype.ALIAS,
            "BETWEEN": self.tokentype.BETWEEN,
            "BY": self.tokentype.BY,
            "CASE": self.tokentype.CASE,
            "CAST": self.tokentype.CAST,
            "COUNT": self.tokentype.COUNT,
            "CREATE": self.tokentype.CREATE,
            "CROSS": self.tokentype.CROSS,
            "DELETE": self.tokentype.DELETE,
            "DESC": self.tokentype.DESC,
            "DISTINCT": self.tokentype.DISTINCT,
            "DROP": self.tokentype.DROP,
            "ELSE": self.tokentype.ELSE,
            "END": self.tokentype.END,
            "EXCEPT": self.tokentype.EXCEPT,
            "EXISTS": self.tokentype.EXISTS,
            "EXTRACT": self.tokentype.EXTRACT,
            "FALSE": self.tokentype.FALSE,
            "FULL": self.tokentype.FULL,
            "FROM": self.tokentype.FROM,
            "GROUP BY": self.tokentype.GROUP,
            "HAVING": self.tokentype.HAVING,
            "IF": self.tokentype.IF,
            "IN": self.tokentype.IN,
            "INNER": self.tokentype.INNER,
            "INSERT": self.tokentype.INSERT,
            "INTERVAL": self.tokentype.INTERVAL,
            "INTERSECT": self.tokentype.INTERSECT,
            "INTO": self.tokentype.INTO,
            "IS": self.tokentype.IS,
            "JOIN": self.tokentype.JOIN,
            "LATERAL": self.tokentype.LATERAL,
            "LEFT": self.tokentype.LEFT,
            "LIKE": self.tokentype.LIKE,
            "LIMIT": self.tokentype.LIMIT,
            "NOT": self.tokentype.NOT,
            "NULL": self.tokentype.NULL,
            "ON": self.tokentype.ON,
            "OR": self.tokentype.OR,
            "ORDER BY": self.tokentype.ORDER,
            "OUTER": self.tokentype.OUTER,
            "OVER": self.tokentype.OVER,
            "PARTITION": self.tokentype.PARTITION,
            "PARTITION BY": self.tokentype.PARTITION_BY,
            "RIGHT": self.tokentype.RIGHT,
            "SELECT": self.tokentype.SELECT,
            "SET": self.tokentype.SET,
            "SHOW": self.tokentype.SHOW,
            "TABLE": self.tokentype.TABLE,
            "THEN": self.tokentype.THEN,
            "TIME": self.tokentype.TIME,
            "TRUE": self.tokentype.TRUE,
            "TRUNCATE": self.tokentype.TRUNCATE,
            "TRY_CAST": self.tokentype.TRY_CAST,
            "UNION": self.tokentype.UNION,
            "UNNEST": self.tokentype.UNNEST,
            "UPDATE": self.tokentype.UPDATE,
            "VALUES": self.tokentype.VALUES,
            "VIEW": self.tokentype.VIEW,
            "WHEN": self.tokentype.WHEN,
            "WHERE": self.tokentype.WHERE,
            "WITH": self.tokentype.WITH,
            "ARRAY": self.tokentype.ARRAY,
            "BOOL": self.tokentype.BOOLEAN,
            "BOOLEAN": self.tokentype.BOOLEAN,
            "BYTE": self.tokentype.TINYINT,
            "TINYINT": self.tokentype.TINYINT,
            "SHORT": self.tokentype.SMALLINT,
            "SMALLINT": self.tokentype.SMALLINT,
            "INT2": self.tokentype.SMALLINT,
            "INTEGER": self.tokentype.INT,
            "INT": self.tokentype.INT,
            "INT4": self.tokentype.INT,
            "LONG": self.tokentype.BIGINT,
            "BIGINT": self.tokentype.BIGINT,
            "INT8": self.tokentype.BIGINT,
            "DECIMAL": self.tokentype.DECIMAL,
            "NUMERIC": self.tokentype.DECIMAL,
            "FIXED": self.tokentype.DECIMAL,
            "REAL": self.tokentype.FLOAT,
            "FLOAT": self.tokentype.FLOAT,
            "FLOAT4": self.tokentype.FLOAT,
            "FLOAT8": self.tokentype.DOUBLE,
            "DOUBLE": self.tokentype.DOUBLE,
            "JSON": self.tokentype.JSON,
            "CHAR": self.tokentype.CHAR,
            "VARCHAR": self.tokentype.VARCHAR,
            "STRING": self.tokentype.TEXT,
            "TEXT": self.tokentype.TEXT,
            "BINARY": self.tokentype.BINARY,
            "TIMESTAMP": self.tokentype.TIMESTAMP,
            "TIMESTAMPTZ": self.tokentype.TIMESTAMP_TZ,
            "DATE": self.tokentype.DATE,

            "COLUMN": self.tokentype.COLUMN,
        }
        self.WHITE_SPACE = {
            " ": self.tokentype.SPACE,
            "\t": self.tokentype.SPACE,
            "\n": self.tokentype.BREAK,
            "\r": self.tokentype.BREAK,
            "\rn": self.tokentype.BREAK,
        }
        self.COMMANDS = {
            self.tokentype.ALTER,
            self.tokentype.CREATE,
            self.tokentype.DELETE,
            self.tokentype.DROP,
            self.tokentype.INSERT,
            self.tokentype.SELECT,
            self.tokentype.SET,
            self.tokentype.SHOW,
            self.tokentype.TRUNCATE,
        }
        self.COMMENTS = {
            "--": self.tokentype.COMMENT_SINGLE,
            "/*": self.tokentype.COMMENT_START,
            "*/": self.tokentype.COMMENT_END,
        }
        self.CMDTOKENS = {
            self.tokentype.SELECT,
            self.tokentype.FROM,
        }

    @abstractmethod
    def getToken(self, value):
        return self.tokenfamily(self.KEYWORDS.get(value), value)

    # def getPrevCmd(self, token):
    #     print(type(self.CMDTOKENS.SELECT))
        # print(f"isinstance: {token.type is self.CMDTOKENS.SELECT}")
        # if token.type is self.CMDTOKENS.SELECT:
        #     print('here')
        #     return token 

    @abstractmethod
    def createToken(self, type, value):
        return self.tokenfamily(self.KEYWORDS.get(type), value)

    @abstractmethod
    def tokenize(self, query:str):
        # print(query)
        # statements = query.split()
        # cmd = None
        # #TODO: convert to loop with try except, None should not become a Token object
        # tokens = []
        # # for word in statements:
        # #     tokens.append(self.tokenfamily(self.KEYWORDS.get(word), word))
        # # statement_type = tokens[0].value
        # prevtoken = prevcmd = None
        # paren_depth = 0
        # # tokens = [self.tokenfamily(self.KEYWORDS.get(word, None), word) for word in statements]
        # for i, word in enumerate(statements):
        #     currtoken = self.getToken(word)
        #     if i == 0:
        #         cmd = currtoken
        #     #TODO: process here all the tokens to save the order
        #     if not currtoken.type:
        #         curchar = ''
        #         for char in currtoken.value:
        #             #TODO: char can be both, append to the prev char and separate token
        #             chartoken = self.getToken(char)
        #             if chartoken.type:
        #                 if chartoken.type is self.tokentype.LEFTPAREN:
        #                     paren_depth+=1
        #                 elif chartoken.type is self.tokentype.RIGHTPAREN:
        #                     paren_depth-=1
        #                     tokens.append(self.createToken("TABLE", curchar))

        #                 # if curchar and prevcmd and prevcmd.type is self.tokentype.SELECT:
        #                 #     print('column', curchar)
        #                 #     tokens.append(self.createToken("COLUMN", curchar))
        #                 #     curchar = ''
        #                 # elif curchar and prevcmd and prevcmd.type is self.tokentype.FROM:
        #                 #     tokens.append(self.createToken("TABLE", curchar))
        #                 #     curchar = ''
        #                 tokens.append(chartoken)
        #                 prevtoken = chartoken
        #                 continue
        #             else:
        #                 curchar+=char
        #                 curchartoken = self.getToken(curchar)
        #                 if curchartoken.type:
        #                     tokens.append(curchartoken)
        #                     prevtoken = curchartoken
        #                 else:
        #                     if prevtoken:
        #                         if prevtoken.type is self.tokentype.RIGHTPAREN or prevtoken.type is self.tokentype.COLUMN or prevtoken.type is self.tokentype.ALIAS:
        #                             temp_token = self.createToken("AS", curchar)
        #                             tokens.append(temp_token)
        #                             prevtoken = temp_token
        #                         if prevtoken.type is self.tokentype.COMMA or prevtoken.type is self.tokentype.SELECT:   
        #                             temp_token = self.createToken("COLUMN", curchar)
        #                             tokens.append(temp_token)
        #                             prevtoken = temp_token
                          
        #         if prevtoken:
        #             if prevtoken.type is self.tokentype.FROM:
        #                 temp_token = self.createToken("TABLE", curchar)
        #                 tokens.append(temp_token)
        #                 prevtoken = temp_token
        #                 continue
        #             # if prevtoken.type is self.tokentype.TABLE or prevtoken.type is self.tokentype.COLUMN:
        #             #     temp_token = self.createToken("AS", curchar)
        #             #     tokens.append(temp_token)
        #             #     prevtoken = temp_token
                        
        #     else:
        #         tokens.append(currtoken)
        #         prevtoken = currtoken
            
        #     if currtoken.type is self.tokentype.SELECT or currtoken.type is self.tokentype.FROM:
        #         prevcmd = currtoken
        #     # try:
        #     #     prevcmd = self.getPrevCmd(currtoken.type)
        #     # except Exception as e:
        #     #     print(e)
        # return tokens
        # print(f"Statement type: {cmd.value}")
        # print("Found tokens:")
        # for token in tokens:
        #     print(token)
        ...

class SnowflakeTokenizer(Tokenizer):
    def __init__(self) -> None:
        super().__init__(SnowflakeTokenType, SnowflakeToken)

    def getToken(self, value):
        return super().getToken(value)

    def createToken(self, type, value):
        return super().createToken(type, value)

    def tokenize(self, query: str):
        statements = query.split()
        cmd = None
        #TODO: convert to loop with try except, None should not become a Token object
        tokens = []
        # for word in statements:
        #     tokens.append(self.tokenfamily(self.KEYWORDS.get(word), word))
        # statement_type = tokens[0].value
        prevtoken = prevcmd = None
        paren_depth = 0
        # tokens = [self.tokenfamily(self.KEYWORDS.get(word, None), word) for word in statements]
        for i, word in enumerate(statements):
            currtoken = self.getToken(word)
            if i == 0:
                cmd = currtoken
            #TODO: process here all the tokens to save the order
            if not currtoken.type:
                curchar = ''
                for char in currtoken.value:
                    #TODO: char can be both, append to the prev char and separate token
                    chartoken = self.getToken(char)
                    if chartoken.type:
                        if chartoken.type is self.tokentype.LEFTPAREN:
                            paren_depth+=1
                        elif chartoken.type is self.tokentype.RIGHTPAREN:
                            paren_depth-=1
                            tokens.append(self.createToken("TABLE", curchar))

                        # if curchar and prevcmd and prevcmd.type is self.tokentype.SELECT:
                        #     print('column', curchar)
                        #     tokens.append(self.createToken("COLUMN", curchar))
                        #     curchar = ''
                        # elif curchar and prevcmd and prevcmd.type is self.tokentype.FROM:
                        #     tokens.append(self.createToken("TABLE", curchar))
                        #     curchar = ''
                        tokens.append(chartoken)
                        prevtoken = chartoken
                        continue
                    else:
                        curchar+=char
                        curchartoken = self.getToken(curchar)
                        if curchartoken.type:
                            tokens.append(curchartoken)
                            prevtoken = curchartoken
                        else:
                            if prevtoken:
                                if prevtoken.type is self.tokentype.RIGHTPAREN or prevtoken.type is self.tokentype.COLUMN or prevtoken.type is self.tokentype.ALIAS:
                                    temp_token = self.createToken("AS", curchar)
                                    tokens.append(temp_token)
                                    prevtoken = temp_token
                                if prevtoken.type is self.tokentype.COMMA or prevtoken.type is self.tokentype.SELECT:   
                                    temp_token = self.createToken("COLUMN", curchar)
                                    tokens.append(temp_token)
                                    prevtoken = temp_token
                                if prevtoken.type is self.tokentype.JOIN:
                                    temp_token = self.createToken("TABLE", curchar)
                                    tokens.append(temp_token)
                                    prevtoken = temp_token
                          
                if prevtoken:
                    if prevtoken.type is self.tokentype.FROM:
                        temp_token = self.createToken("TABLE", curchar)
                        tokens.append(temp_token)
                        prevtoken = temp_token
                        continue
                    # if prevtoken.type is self.tokentype.TABLE or prevtoken.type is self.tokentype.COLUMN:
                    #     temp_token = self.createToken("AS", curchar)
                    #     tokens.append(temp_token)
                    #     prevtoken = temp_token
                        
            else:
                tokens.append(currtoken)
                prevtoken = currtoken
            
            if currtoken.type is self.tokentype.SELECT or currtoken.type is self.tokentype.FROM:
                prevcmd = currtoken
            # try:
            #     prevcmd = self.getPrevCmd(currtoken.type)
            # except Exception as e:
            #     print(e)
        return tokens

    
# class SnowflakeTokenizer(Tokenizer):
#     def __init__(self, tokenizer) -> None:
#         self.tokentype = SnowflakeTokenType
#         self.SINGLE_TOKENS = {}
#         self.KEYWORDS = {}
#         self.WHITE_SPACE = {}
#         self.COMMANDS = {}
#         self.COMMENTS = {}
    
#     def combine_tokens(self) -> None:
#         SINGLE_TOKENS = {
#             "(": self.tokentype.LEFTPAREN,
#             ")": self.tokentype.RIGHTPAREN,
#             ":": self.tokentype.COLON,
#             ",": self.tokentype.COMMA,
#             ".": self.tokentype.DOT,
#             "-": self.tokentype.DASH,
#             "=": self.tokentype.EQ,
#             ">": self.tokentype.GT,
#             "<": self.tokentype.LT,
#             "%": self.tokentype.MOD,
#             "!": self.tokentype.NOT,
#             "+": self.tokentype.PLUS,
#             ";": self.tokentype.SEMICOLON,
#             "/": self.tokentype.SLASH,
#             "*": self.tokentype.STAR,
#         }

#         KEYWORDS = {
#             "--": self.tokentype.COMMENT,
#             "/*": self.tokentype.COMMENT_START,
#             "*/": self.tokentype.COMMENT_END,
#             "==": self.tokentype.EQ,
#             ">=": self.tokentype.GTE,
#             "<=": self.tokentype.LTE,
#             "<>": self.tokentype.NEQ,
#             "!=": self.tokentype.NEQ,
#             "ALTER": self.tokentype.ALTER,
#             "AND": self.tokentype.AND,
#             "ASC": self.tokentype.ASC,
#             "AS": self.tokentype.ALIAS,
#             "BETWEEN": self.tokentype.BETWEEN,
#             "BY": self.tokentype.BY,
#             "CASE": self.tokentype.CASE,
#             "CAST": self.tokentype.CAST,
#             "COUNT": self.tokentype.COUNT,
#             "CREATE": self.tokentype.CREATE,
#             "CROSS": self.tokentype.CROSS,
#             "DELETE": self.tokentype.DELETE,
#             "DESC": self.tokentype.DESC,
#             "DISTINCT": self.tokentype.DISTINCT,
#             "DROP": self.tokentype.DROP,
#             "ELSE": self.tokentype.ELSE,
#             "END": self.tokentype.END,
#             "EXCEPT": self.tokentype.EXCEPT,
#             "EXISTS": self.tokentype.EXISTS,
#             "EXTRACT": self.tokentype.EXTRACT,
#             "FALSE": self.tokentype.FALSE,
#             "FULL": self.tokentype.FULL,
#             "FROM": self.tokentype.FROM,
#             "GROUP BY": self.tokentype.GROUP,
#             "HAVING": self.tokentype.HAVING,
#             "IF": self.tokentype.IF,
#             "IN": self.tokentype.IN,
#             "INNER": self.tokentype.INNER,
#             "INSERT": self.tokentype.INSERT,
#             "INTERVAL": self.tokentype.INTERVAL,
#             "INTERSECT": self.tokentype.INTERSECT,
#             "INTO": self.tokentype.INTO,
#             "IS": self.tokentype.IS,
#             "JOIN": self.tokentype.JOIN,
#             "LATERAL": self.tokentype.LATERAL,
#             "LEFT": self.tokentype.LEFT,
#             "LIKE": self.tokentype.LIKE,
#             "LIMIT": self.tokentype.LIMIT,
#             "NOT": self.tokentype.NOT,
#             "NULL": self.tokentype.NULL,
#             "ON": self.tokentype.ON,
#             "OR": self.tokentype.OR,
#             "ORDER BY": self.tokentype.ORDER,
#             "OUTER": self.tokentype.OUTER,
#             "OVER": self.tokentype.OVER,
#             "PARTITION": self.tokentype.PARTITION,
#             "PARTITION BY": self.tokentype.PARTITION_BY,
#             "RIGHT": self.tokentype.RIGHT,
#             "SELECT": self.tokentype.SELECT,
#             "SET": self.tokentype.SET,
#             "SHOW": self.tokentype.SHOW,
#             "TABLE": self.tokentype.TABLE,
#             "THEN": self.tokentype.THEN,
#             "TIME": self.tokentype.TIME,
#             "TRUE": self.tokentype.TRUE,
#             "TRUNCATE": self.tokentype.TRUNCATE,
#             "TRY_CAST": self.tokentype.TRY_CAST,
#             "UNION": self.tokentype.UNION,
#             "UNNEST": self.tokentype.UNNEST,
#             "UPDATE": self.tokentype.UPDATE,
#             "VALUES": self.tokentype.VALUES,
#             "VIEW": self.tokentype.VIEW,
#             "WHEN": self.tokentype.WHEN,
#             "WHERE": self.tokentype.WHERE,
#             "WITH": self.tokentype.WITH,
#             "ARRAY": self.tokentype.ARRAY,
#             "BOOL": self.tokentype.BOOLEAN,
#             "BOOLEAN": self.tokentype.BOOLEAN,
#             "BYTE": self.tokentype.TINYINT,
#             "TINYINT": self.tokentype.TINYINT,
#             "SHORT": self.tokentype.SMALLINT,
#             "SMALLINT": self.tokentype.SMALLINT,
#             "INT2": self.tokentype.SMALLINT,
#             "INTEGER": self.tokentype.INT,
#             "INT": self.tokentype.INT,
#             "INT4": self.tokentype.INT,
#             "LONG": self.tokentype.BIGINT,
#             "BIGINT": self.tokentype.BIGINT,
#             "INT8": self.tokentype.BIGINT,
#             "DECIMAL": self.tokentype.DECIMAL,
#             "NUMERIC": self.tokentype.DECIMAL,
#             "FIXED": self.tokentype.DECIMAL,
#             "REAL": self.tokentype.FLOAT,
#             "FLOAT": self.tokentype.FLOAT,
#             "FLOAT4": self.tokentype.FLOAT,
#             "FLOAT8": self.tokentype.DOUBLE,
#             "DOUBLE": self.tokentype.DOUBLE,
#             "JSON": self.tokentype.JSON,
#             "CHAR": self.tokentype.CHAR,
#             "VARCHAR": self.tokentype.VARCHAR,
#             "STRING": self.tokentype.TEXT,
#             "TEXT": self.tokentype.TEXT,
#             "BINARY": self.tokentype.BINARY,
#             "TIMESTAMP": self.tokentype.TIMESTAMP,
#             "TIMESTAMPTZ": self.tokentype.TIMESTAMP_TZ,
#             "DATE": self.tokentype.DATE,
#         }

#         WHITE_SPACE = {
#             " ": self.tokentype.SPACE,
#             "\t": self.tokentype.SPACE,
#             "\n": self.tokentype.BREAK,
#             "\r": self.tokentype.BREAK,
#             "\rn": self.tokentype.BREAK,
#         }

#         COMMANDS = {
#             self.tokentype.ALTER,
#             self.tokentype.SET,
#             self.tokentype.SHOW,
#             self.tokentype.TRUNCATE,
#         }

#         COMMENTS = {
#             "--": self.tokentype.SINGLE_COMMENT,
#             "/*": self.tokentype.START_COMMENT,
#             "*/": self.tokentype.END_COMMENT,
#         }

#         __slots__ = (
#             "quotes",
#             "identifier",
#             "escape",
#             "encode",
#             "numeric_literals",
#             "code",
#             "size",
#             "tokens",
#             "_start",
#             "_current",
#             "_line",
#             "_col",
#             "_char",
#             "_end",
#             "_peek",
#             "__text",
#         )
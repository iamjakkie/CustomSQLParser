from CustomSQLParser.lexer.token import SnowflakeTokenType, SnowflakeToken
from CustomSQLParser.lexer.tokenizer import Tokenizer

def main():
    sftokenizer = Tokenizer(SnowflakeTokenType, SnowflakeToken)
    queries = ['SELECT a, b, c FROM (SELECT a, b, c FROM test) a'
                ,'SELECT a, b c FROM xyz a'
                ,'SELECT a AS b FROM db2']
    for query in queries:
        sftokenizer.tokenize(query)

if __name__ == "__main__":
    main()
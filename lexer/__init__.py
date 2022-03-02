from CustomSQLParser.lexer.token import SnowflakeTokenType, SnowflakeToken
from CustomSQLParser.lexer.tokenizer import Tokenizer

def main():
    sftokenizer = Tokenizer(SnowflakeTokenType, SnowflakeToken)
    query = 'SELECT a, b, c FROM (SELECT a, b, c FROM test) a'
    sftokenizer.tokenize(query)

if __name__ == "__main__":
    main()
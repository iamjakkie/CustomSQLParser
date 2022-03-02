from CustomSQLParser.lexer.token import SnowflakeTokenType
from CustomSQLParser.lexer.tokenizer import Tokenizer

def main():
    sftokenizer = Tokenizer(SnowflakeTokenType)
    query = 'SELECT * FROM test'
    sftokenizer.tokenize(query)

if __name__ == "__main__":
    main()
from CustomSQLParser.lexer.interpreter import SnowflakeInterpreter

def main():
    sfinterpreter = SnowflakeInterpreter()
    queries = ['SELECT a, b, c FROM (SELECT a, b, c FROM test) a'
                ,'SELECT a, b c FROM xyz a'
                ,'SELECT a AS b FROM db2']
    for query in queries:
        sfinterpreter.translate_query(query)

if __name__ == "__main__":
    main()
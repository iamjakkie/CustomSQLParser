from CustomSQLParser.lexer.interpreter import SnowflakeInterpreter

def main():
    sfinterpreter = SnowflakeInterpreter()
    queries = ['SELECT a, b, c FROM (SELECT a, b, c FROM test) a'
                ,'SELECT a, b c FROM xyz a'
                ,'SELECT a AS b FROM db2'
                ,'SELECT a.* FROM a JOIN b ON (a.id = b.id)']
    for query in queries:
        print(query)
        sfinterpreter.translate_query(query)

if __name__ == "__main__":
    main()
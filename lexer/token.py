from enum import auto
from utils.tokenutils import IdGenerator


# Token categories
class TokenType(IdGenerator):
    EOF = auto()
    ASSIGNOP = auto()
    LEFTPAREN = auto()
    RIGHTPAREN = auto()
    COMMA = auto()
    DOT = auto()
    PLUS = auto()
    COLON = auto()
    SEMICOLON = auto()
    STAR = auto()
    SLASH = auto()
    DASH = auto()
    LT = auto()
    LTE = auto()
    GT = auto()
    GTE = auto()
    NOT = auto()
    EQ = auto()
    NEQ = auto()
    AND = auto()
    OR = auto()
    MOD = auto()

    SPACE = auto()
    BREAK = auto()

    STRING = auto()
    NUMBER = auto()
    COLUMN = auto()
    SCHEMA = auto()
    TABLE = auto()

    NUMBER = auto()
    DECIMAL = auto()
    NUMERIC = auto()
    INT = auto()
    INTEGER = auto()
    BIGINT = auto()
    SMALLINT = auto()
    TINYINT = auto()
    BYTEINT = auto()
    FLOAT = auto()
    FLOAT4 = auto()
    FLOAT8 = auto()
    DOUBLE = auto()
    DOUBLEPRECISION = auto()
    REAL = auto()
    VARCHAR = auto()
    CHAR = auto()
    CHARACTER = auto()
    TEXT = auto()
    BINARY = auto()
    VARBINARY = auto()
    BOOLEAN = auto()
    DATE = auto()
    DATETIME = auto()
    TIME = auto()
    TIMESTAMP = auto()
    TIMESTAMP_LTZ = auto()
    TIMESTAMP_NTZ = auto()
    TIMESTAMP_TZ = auto()
    VARIANT = auto()
    OBJECT = auto()
    ARRAY = auto()
    GEOGRAPHY = auto()
    JSON = auto()

    ALIAS = auto()
    ALTER = auto()
    AS = auto()
    ASC = auto()
    BETWEEN = auto()
    BY = auto()
    CASE = auto()
    CAST = auto()
    COUNT = auto()
    COMMENT = auto()
    COMMENT_END = auto()
    COMMENT_START = auto()
    CREATE = auto()
    CROSS = auto()
    DELETE = auto()
    DESC = auto()
    DISTINCT = auto()
    DROP = auto()
    ELSE = auto()
    END = auto()
    EXCEPT = auto()
    EXISTS = auto()
    EXTRACT = auto()
    FALSE = auto()
    FULL = auto()
    FROM = auto()
    GROUP = auto()
    HAVING = auto()
    IF = auto()
    IN = auto()
    INNER = auto()
    INSERT = auto()
    INTERSECT = auto()
    INTERVAL = auto()
    INTO = auto()
    IS = auto()
    JOIN = auto()
    LATERAL = auto()
    LEFT = auto()
    LIKE = auto()
    LIMIT = auto()
    NULL = auto()
    ON = auto()
    ORDER = auto()
    OUTER = auto()
    OVER = auto()
    PARTITION = auto()
    PARTITION_BY = auto()
    QSTRING = auto()
    DQSTRING = auto()
    RIGHT = auto()
    SELECT = auto()
    SET = auto()
    SHOW = auto()
    THEN = auto()
    TRUE = auto()
    TRUNCATE = auto()
    TRY_CAST = auto()
    UNION = auto()
    UNNEST = auto()
    UPDATE = auto()
    VALUES = auto()
    VIEW = auto()
    WHEN = auto()
    WHERE = auto()
    WITH = auto()


class Tokenizer:
    SINGLE_TOKENS = {
        "(": TokenType.LEFTPAREN,
        ")": TokenType.RIGHTPAREN,
        ":": TokenType.COLON,
        ",": TokenType.COMMA,
        ".": TokenType.DOT,
        "-": TokenType.DASH,
        "=": TokenType.EQ,
        ">": TokenType.GT,
        "<": TokenType.LT,
        "%": TokenType.MOD,
        "!": TokenType.NOT,
        "+": TokenType.PLUS,
        ";": TokenType.SEMICOLON,
        "/": TokenType.SLASH,
        "*": TokenType.STAR,
    }

    KEYWORDS = {
        "--": TokenType.COMMENT,
        "/*": TokenType.COMMENT_START,
        "*/": TokenType.COMMENT_END,
        "==": TokenType.EQ,
        ">=": TokenType.GTE,
        "<=": TokenType.LTE,
        "<>": TokenType.NEQ,
        "!=": TokenType.NEQ,
        "ALTER": TokenType.ALTER,
        "AND": TokenType.AND,
        "ASC": TokenType.ASC,
        "AS": TokenType.ALIAS,
        "BETWEEN": TokenType.BETWEEN,
        "BY": TokenType.BY,
        "CASE": TokenType.CASE,
        "CAST": TokenType.CAST,
        "COUNT": TokenType.COUNT,
        "CREATE": TokenType.CREATE,
        "CROSS": TokenType.CROSS,
        "DELETE": TokenType.DELETE,
        "DESC": TokenType.DESC,
        "DISTINCT": TokenType.DISTINCT,
        "DROP": TokenType.DROP,
        "ELSE": TokenType.ELSE,
        "END": TokenType.END,
        "EXCEPT": TokenType.EXCEPT,
        "EXISTS": TokenType.EXISTS,
        "EXTRACT": TokenType.EXTRACT,
        "FALSE": TokenType.FALSE,
        "FULL": TokenType.FULL,
        "FROM": TokenType.FROM,
        "GROUP BY": TokenType.GROUP,
        "HAVING": TokenType.HAVING,
        "IF": TokenType.IF,
        "IN": TokenType.IN,
        "INNER": TokenType.INNER,
        "INSERT": TokenType.INSERT,
        "INTERVAL": TokenType.INTERVAL,
        "INTERSECT": TokenType.INTERSECT,
        "INTO": TokenType.INTO,
        "IS": TokenType.IS,
        "JOIN": TokenType.JOIN,
        "LATERAL": TokenType.LATERAL,
        "LEFT": TokenType.LEFT,
        "LIKE": TokenType.LIKE,
        "LIMIT": TokenType.LIMIT,
        "NOT": TokenType.NOT,
        "NULL": TokenType.NULL,
        "ON": TokenType.ON,
        "OR": TokenType.OR,
        "ORDER BY": TokenType.ORDER,
        "OUTER": TokenType.OUTER,
        "OVER": TokenType.OVER,
        "PARTITION": TokenType.PARTITION,
        "PARTITION BY": TokenType.PARTITION_BY,
        "RIGHT": TokenType.RIGHT,
        "SELECT": TokenType.SELECT,
        "SET": TokenType.SET,
        "SHOW": TokenType.SHOW,
        "TABLE": TokenType.TABLE,
        "THEN": TokenType.THEN,
        "TIME": TokenType.TIME,
        "TRUE": TokenType.TRUE,
        "TRUNCATE": TokenType.TRUNCATE,
        "TRY_CAST": TokenType.TRY_CAST,
        "UNION": TokenType.UNION,
        "UNNEST": TokenType.UNNEST,
        "UPDATE": TokenType.UPDATE,
        "VALUES": TokenType.VALUES,
        "VIEW": TokenType.VIEW,
        "WHEN": TokenType.WHEN,
        "WHERE": TokenType.WHERE,
        "WITH": TokenType.WITH,
        "ARRAY": TokenType.ARRAY,
        "BOOL": TokenType.BOOLEAN,
        "BOOLEAN": TokenType.BOOLEAN,
        "BYTE": TokenType.TINYINT,
        "TINYINT": TokenType.TINYINT,
        "SHORT": TokenType.SMALLINT,
        "SMALLINT": TokenType.SMALLINT,
        "INT2": TokenType.SMALLINT,
        "INTEGER": TokenType.INT,
        "INT": TokenType.INT,
        "INT4": TokenType.INT,
        "LONG": TokenType.BIGINT,
        "BIGINT": TokenType.BIGINT,
        "INT8": TokenType.BIGINT,
        "DECIMAL": TokenType.DECIMAL,
        "NUMERIC": TokenType.DECIMAL,
        "FIXED": TokenType.DECIMAL,
        "REAL": TokenType.FLOAT,
        "FLOAT": TokenType.FLOAT,
        "FLOAT4": TokenType.FLOAT,
        "FLOAT8": TokenType.DOUBLE,
        "DOUBLE": TokenType.DOUBLE,
        "JSON": TokenType.JSON,
        "CHAR": TokenType.CHAR,
        "VARCHAR": TokenType.VARCHAR,
        "STRING": TokenType.TEXT,
        "TEXT": TokenType.TEXT,
        "BINARY": TokenType.BINARY,
        "TIMESTAMP": TokenType.TIMESTAMP,
        "TIMESTAMPTZ": TokenType.TIMESTAMP_TZ,
        "DATE": TokenType.DATE,
    }

    WHITE_SPACE = {
        " ": TokenType.SPACE,
        "\t": TokenType.SPACE,
        "\n": TokenType.BREAK,
        "\r": TokenType.BREAK,
        "\rn": TokenType.BREAK,
    }

    COMMANDS = {
        TokenType.ALTER,
        TokenType.SET,
        TokenType.SHOW,
        TokenType.TRUNCATE,
    }

    ESCAPE_CODE = "__sqlglot_escape__"

    AMBIGUOUS = new_ambiguous(KEYWORDS, SINGLE_TOKENS)
    COMMENTS = ["--"]
    COMMENT_START = "/*"
    COMMENT_END = "*/"

    __slots__ = (
        "quotes",
        "identifier",
        "escape",
        "encode",
        "numeric_literals",
        "code",
        "size",
        "tokens",
        "_start",
        "_current",
        "_line",
        "_col",
        "_char",
        "_end",
        "_peek",
        "__text",
    )

class Token:
    def __init__(self, type, value) -> None:
        self.type = type
        self.value = value 

    def __repr__(self) -> str:
        if self.value:
            return f"{self.type}:{self.value}"
        return f"{self.type}"
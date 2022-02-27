# Token categories
EOF = 0
TABLE = 1 
COLUMN = 2
ASSIGNOP = 3
LEFTPAREN = 4
RIGHTPAREN = 5
COMMA = 6
DOT = 7
PLUS = 8
COLON = 9
SEMICOLON = 10
STAR = 11
SLASH = 12
LT = 13
LTE = 14
GT = 15
GTE = 16
NOT = 17
EQ = 18
NEQ = 19
AND = 20
OR = 21

SPACE = 22
BREAK = 23

STRING = 24
NUMBER = 25




class TokenType(AutoName):
    L_PAREN = auto()
    R_PAREN = auto()
    L_BRACKET = auto()
    R_BRACKET = auto()
    L_BRACE = auto()
    R_BRACE = auto()
    COMMA = auto()
    DOT = auto()
    DASH = auto()
    PLUS = auto()
    COLON = auto()
    DCOLON = auto()
    SEMICOLON = auto()
    STAR = auto()
    SLASH = auto()
    LT = auto()
    LTE = auto()
    GT = auto()
    GTE = auto()
    NOT = auto()
    EQ = auto()
    NEQ = auto()
    AND = auto()
    OR = auto()
    AMP = auto()
    DPIPE = auto()
    PIPE = auto()
    CARET = auto()
    TILDA = auto()
    LSHIFT = auto()
    RSHIFT = auto()
    LAMBDA = auto()

    SPACE = auto()
    BREAK = auto()

    STRING = auto()
    NUMBER = auto()
    IDENTIFIER = auto()
    COLUMN = auto()
    COLUMN_DEF = auto()
    SCHEMA = auto()
    TABLE = auto()
    VAR = auto()

    # types
    BOOLEAN = auto()
    TINYINT = auto()
    SMALLINT = auto()
    INT = auto()
    BIGINT = auto()
    FLOAT = auto()
    DOUBLE = auto()
    DECIMAL = auto()
    CHAR = auto()
    VARCHAR = auto()
    TEXT = auto()
    BINARY = auto()
    JSON = auto()
    TIMESTAMP = auto()
    TIMESTAMPTZ = auto()
    DATE = auto()

    # keywords
    ADD_FILE = auto()
    ALIAS = auto()
    ALL = auto()
    ALTER = auto()
    ARRAY = auto()
    ASC = auto()
    AUTO_INCREMENT = auto()
    BETWEEN = auto()
    BUCKET = auto()
    BY = auto()
    CACHE = auto()
    UNCACHE = auto()
    CASE = auto()
    CAST = auto()
    CHARACTER_SET = auto()
    COUNT = auto()
    COLLATE = auto()
    COMMENT = auto()
    COMMENT_END = auto()
    COMMENT_START = auto()
    CREATE = auto()
    CROSS = auto()
    CURRENT_ROW = auto()
    DIV = auto()
    DEFAULT = auto()
    DELETE = auto()
    DESC = auto()
    DISTINCT = auto()
    DROP = auto()
    ELSE = auto()
    END = auto()
    ENGINE = auto()
    EXCEPT = auto()
    EXISTS = auto()
    EXPLAIN = auto()
    EXTRACT = auto()
    FALSE = auto()
    FOLLOWING = auto()
    FORMAT = auto()
    FULL = auto()
    FROM = auto()
    GROUP = auto()
    HAVING = auto()
    HINT = auto()
    IF = auto()
    ILIKE = auto()
    IN = auto()
    INNER = auto()
    INSERT = auto()
    INTERSECT = auto()
    INTERVAL = auto()
    INTO = auto()
    IS = auto()
    JOIN = auto()
    LATERAL = auto()
    LAZY = auto()
    LEFT = auto()
    LIKE = auto()
    LIMIT = auto()
    MAP = auto()
    MOD = auto()
    NULL = auto()
    ON = auto()
    OPTIMIZE = auto()
    OPTIONS = auto()
    ORDER = auto()
    ORDERED = auto()
    ORDINALITY = auto()
    OUTER = auto()
    OUT_OF = auto()
    OVER = auto()
    OVERWRITE = auto()
    PARTITION = auto()
    PARTITION_BY = auto()
    PERCENT = auto()
    PRECEDING = auto()
    PRIMARY_KEY = auto()
    RANGE = auto()
    RECURSIVE = auto()
    REPLACE = auto()
    RIGHT = auto()
    RLIKE = auto()
    ROWS = auto()
    SCHEMA_COMMENT = auto()
    SELECT = auto()
    SET = auto()
    SHOW = auto()
    STORED = auto()
    TABLE_SAMPLE = auto()
    TEMPORARY = auto()
    TIME = auto()
    THEN = auto()
    TRUE = auto()
    TRUNCATE = auto()
    TRY_CAST = auto()
    UNBOUNDED = auto()
    UNION = auto()
    UNNEST = auto()
    UPDATE = auto()
    VALUES = auto()
    VIEW = auto()
    WHEN = auto()
    WHERE = auto()
    WITH = auto()
    WITHOUT = auto()
    ZONE = auto()

class Tokenizer:
    SINGLE_TOKENS = {
        "(": TokenType.L_PAREN,
        ")": TokenType.R_PAREN,
        "[": TokenType.L_BRACKET,
        "]": TokenType.R_BRACKET,
        "{": TokenType.L_BRACE,
        "}": TokenType.R_BRACE,
        "&": TokenType.AMP,
        "^": TokenType.CARET,
        ":": TokenType.COLON,
        ",": TokenType.COMMA,
        ".": TokenType.DOT,
        "-": TokenType.DASH,
        "=": TokenType.EQ,
        ">": TokenType.GT,
        "<": TokenType.LT,
        "%": TokenType.MOD,
        "!": TokenType.NOT,
        "|": TokenType.PIPE,
        "+": TokenType.PLUS,
        ";": TokenType.SEMICOLON,
        "/": TokenType.SLASH,
        "*": TokenType.STAR,
        "~": TokenType.TILDA,
    }

    KEYWORDS = {
        "/*+": TokenType.HINT,
        "--": TokenType.COMMENT,
        "/*": TokenType.COMMENT_START,
        "*/": TokenType.COMMENT_END,
        "==": TokenType.EQ,
        "::": TokenType.DCOLON,
        "||": TokenType.DPIPE,
        ">=": TokenType.GTE,
        "<=": TokenType.LTE,
        "<>": TokenType.NEQ,
        "!=": TokenType.NEQ,
        "<<": TokenType.LSHIFT,
        ">>": TokenType.RSHIFT,
        "->": TokenType.LAMBDA,
        "ADD ARCHIVE": TokenType.ADD_FILE,
        "ADD ARCHIVES": TokenType.ADD_FILE,
        "ADD FILE": TokenType.ADD_FILE,
        "ADD FILES": TokenType.ADD_FILE,
        "ADD JAR": TokenType.ADD_FILE,
        "ADD JARS": TokenType.ADD_FILE,
        "ALL": TokenType.ALL,
        "ALTER": TokenType.ALTER,
        "AND": TokenType.AND,
        "ASC": TokenType.ASC,
        "AS": TokenType.ALIAS,
        "AUTO_INCREMENT": TokenType.AUTO_INCREMENT,
        "BETWEEN": TokenType.BETWEEN,
        "BUCKET": TokenType.BUCKET,
        "BY": TokenType.BY,
        "CACHE": TokenType.CACHE,
        "UNCACHE": TokenType.UNCACHE,
        "CASE": TokenType.CASE,
        "CAST": TokenType.CAST,
        "CHARACTER SET": TokenType.CHARACTER_SET,
        "COLLATE": TokenType.COLLATE,
        "COMMENT": TokenType.SCHEMA_COMMENT,
        "COUNT": TokenType.COUNT,
        "CREATE": TokenType.CREATE,
        "CROSS": TokenType.CROSS,
        "CURRENT ROW": TokenType.CURRENT_ROW,
        "DIV": TokenType.DIV,
        "DEFAULT": TokenType.DEFAULT,
        "DELETE": TokenType.DELETE,
        "DESC": TokenType.DESC,
        "DISTINCT": TokenType.DISTINCT,
        "DROP": TokenType.DROP,
        "ELSE": TokenType.ELSE,
        "END": TokenType.END,
        "ENGINE": TokenType.ENGINE,
        "EXCEPT": TokenType.EXCEPT,
        "EXISTS": TokenType.EXISTS,
        "EXPLAIN": TokenType.EXPLAIN,
        "EXTRACT": TokenType.EXTRACT,
        "FALSE": TokenType.FALSE,
        "FORMAT": TokenType.FORMAT,
        "FULL": TokenType.FULL,
        "FOLLOWING": TokenType.FOLLOWING,
        "FROM": TokenType.FROM,
        "GROUP BY": TokenType.GROUP,
        "HAVING": TokenType.HAVING,
        "IF": TokenType.IF,
        "ILIKE": TokenType.ILIKE,
        "IN": TokenType.IN,
        "INNER": TokenType.INNER,
        "INSERT": TokenType.INSERT,
        "INTERVAL": TokenType.INTERVAL,
        "INTERSECT": TokenType.INTERSECT,
        "INTO": TokenType.INTO,
        "IS": TokenType.IS,
        "JOIN": TokenType.JOIN,
        "LATERAL": TokenType.LATERAL,
        "LAZY": TokenType.LAZY,
        "LEFT": TokenType.LEFT,
        "LIKE": TokenType.LIKE,
        "LIMIT": TokenType.LIMIT,
        "NOT": TokenType.NOT,
        "NULL": TokenType.NULL,
        "ON": TokenType.ON,
        "OPTIMIZE": TokenType.OPTIMIZE,
        "OPTIONS": TokenType.OPTIONS,
        "OR": TokenType.OR,
        "ORDER BY": TokenType.ORDER,
        "ORDINALITY": TokenType.ORDINALITY,
        "OUTER": TokenType.OUTER,
        "OUT OF": TokenType.OUT_OF,
        "OVER": TokenType.OVER,
        "OVERWRITE": TokenType.OVERWRITE,
        "PARTITION": TokenType.PARTITION,
        "PARTITION BY": TokenType.PARTITION_BY,
        "PERCENT": TokenType.PERCENT,
        "PRECEDING": TokenType.PRECEDING,
        "PRIMARY KEY": TokenType.PRIMARY_KEY,
        "RANGE": TokenType.RANGE,
        "RECURSIVE": TokenType.RECURSIVE,
        "REGEXP": TokenType.RLIKE,
        "REPLACE": TokenType.REPLACE,
        "RIGHT": TokenType.RIGHT,
        "RLIKE": TokenType.RLIKE,
        "ROWS": TokenType.ROWS,
        "SELECT": TokenType.SELECT,
        "SET": TokenType.SET,
        "SHOW": TokenType.SHOW,
        "STORED": TokenType.STORED,
        "TABLE": TokenType.TABLE,
        "TABLESAMPLE": TokenType.TABLE_SAMPLE,
        "TEMP": TokenType.TEMPORARY,
        "TEMPORARY": TokenType.TEMPORARY,
        "THEN": TokenType.THEN,
        "TIME": TokenType.TIME,
        "TRUE": TokenType.TRUE,
        "TRUNCATE": TokenType.TRUNCATE,
        "TRY_CAST": TokenType.TRY_CAST,
        "UNBOUNDED": TokenType.UNBOUNDED,
        "UNION": TokenType.UNION,
        "UNNEST": TokenType.UNNEST,
        "UPDATE": TokenType.UPDATE,
        "VALUES": TokenType.VALUES,
        "VIEW": TokenType.VIEW,
        "WHEN": TokenType.WHEN,
        "WHERE": TokenType.WHERE,
        "WITH": TokenType.WITH,
        "WITHOUT": TokenType.WITHOUT,
        "ZONE": TokenType.ZONE,
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
        "MAP": TokenType.MAP,
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
        "TIMESTAMPTZ": TokenType.TIMESTAMPTZ,
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
        TokenType.ADD_FILE,
        TokenType.EXPLAIN,
        TokenType.OPTIMIZE,
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
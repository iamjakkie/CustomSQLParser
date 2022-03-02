from abc import ABC, abstractmethod
from enum import auto
from CustomSQLParser.utils.tokenutils import IdGenerator


# Token categories
class SnowflakeTokenType(IdGenerator):
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
    COMMENT_SINGLE = auto()
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


class Token(ABC):
    #TODO: Setters, getters, errors
    @abstractmethod
    def __init__(self, type, value) -> None:
        self.type = type
        self.value = value 

    @abstractmethod
    def __repr__(self) -> str:
        if self.value:
            return f"{self.type}:{self.value}"
        return f"{self.type}"

class SnowflakeToken(Token):
    def __init__(self, type, value) -> None:
        self.type = type
        self.value = value 

    def __repr__(self) -> str:
        return super().__repr__()


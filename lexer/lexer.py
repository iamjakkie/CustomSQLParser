class Lexer:
    def __init__(self, query) -> None:
        self.query = query 
        self.pos = -1
        self.current_char = None
        self.advance()

    def advance(self):
        self.pos+=1
        self.current_char = self.query[pos] if sel.pos < len(self.query) else None

    def make_tokens(self):
        tokens = []

        while self.current_char != None:
            if self.current_char in ' \t\n':
                self.advance()
            elif s
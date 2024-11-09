class ParserError(Exception):
    def __init__(self, message, token=None):
        self.token = token
        super().__init__(message)

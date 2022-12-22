class InvalidCommand(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__()
    def __str__(self) -> str:
        return self.message
class AccountNotFound(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__()
    def __str__(self) -> str:
        return self.message
        
class UserNotFound(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__()
    def __str__(self) -> str:
        return self.message
class InvalidAccountCurrency(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__()
    def __str__(self) -> str:
        return self.message
class InvalidAccountCurrency(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__()
    def __str__(self) -> str:
        return self.message
class InvalidADataFormat(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__()
    def __str__(self) -> str:
        return self.message       
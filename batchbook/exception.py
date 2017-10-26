class BaseError(Exception):
    pass

class InvalidCredential(BaseError):
    pass

class Bad_Request(BaseError):
    pass

class Not_Found(BaseError):
    pass
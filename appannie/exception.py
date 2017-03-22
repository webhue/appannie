class AppAnnieException(Exception):
    DEFAULT_ERROR_CODE = 500

    def __init__(self, message, code=None):
        Exception.__init__(self, message)
        self.code = code if code else self.DEFAULT_ERROR_CODE


class AppAnnieBadRequestException(AppAnnieException):
    ERROR_CODE = 400

    def __init__(self, message):
        AppAnnieException.__init__(self, message, code=self.ERROR_CODE)


class AppAnnieNotFoundException(AppAnnieException):
    ERROR_CODE = 404

    def __init__(self, message):
        AppAnnieException.__init__(self, message, code=self.ERROR_CODE)


class AppAnnieUnauthorizedException(AppAnnieException):
    ERROR_CODE = 401

    def __init__(self, message):
        AppAnnieException.__init__(self, message, code=self.ERROR_CODE)


class AppAnnieRateLimitException(AppAnnieException):
    ERROR_CODE = 429

    def __init__(self, message):
        AppAnnieException.__init__(self, message, code=self.ERROR_CODE)

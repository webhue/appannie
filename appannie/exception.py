class AppAnnieException(Exception):
    ERROR_CODE = 500


class AppAnnieBadRequestException(AppAnnieException):
    ERROR_CODE = 400


class AppAnnieNotFoundException(AppAnnieException):
    ERROR_CODE = 404


class AppAnnieUnauthorizedException(AppAnnieException):
    ERROR_CODE = 401


class AppAnnieRateLimitException(AppAnnieException):
    ERROR_CODE = 429

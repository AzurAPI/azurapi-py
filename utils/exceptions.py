class AzurApiException(Exception):
    pass

class UnknownShipException(AzurApiException):
    pass

class UnknownLanguageException(AzurApiException):
    pass
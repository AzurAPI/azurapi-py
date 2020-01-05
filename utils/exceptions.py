class AzurApiException(Exception):
    pass

class UnknownShipException(AzurApiException):
    pass

class UnknownLanguageException(AzurApiException):
    pass

class UnknownChapterException(AzurApiException):
    pass

class UnknownDifficultyException(AzurApiException):
    pass
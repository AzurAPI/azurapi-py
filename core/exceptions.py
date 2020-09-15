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

class UnknownMemoryException(AzurApiException):
    pass

class UnknownFactionException(AzurApiException):
    pass

class UnknownEquipmentException(AzurApiException):
    pass
#region Exceptions
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
#endregion

#region Helpers
def is_str_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False
#endregion
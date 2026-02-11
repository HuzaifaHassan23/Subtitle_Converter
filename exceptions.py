class SubtitleError(Exception):
    pass


class InvalidFormatError(SubtitleError):
    pass


class FileTypeMismatchError(SubtitleError):
    pass

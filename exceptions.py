class SubtitleError(Exception):
    def __init__(self, message: str):
        super().__init__(message)
        self.message = message


class InvalidFormatError(SubtitleError):
    def __init__(self, message: str, file_path: str = None, line_number: int = None): # type: ignore
        self.file_path = file_path
        self.line_number = line_number
        
        ctx = []
        if file_path:
            ctx.append(f"in '{file_path}'")
        if line_number:
            ctx.append(f"at line {line_number}")
            
        ctx_str = " " + " ".join(ctx) if ctx else ""
        super().__init__(f"{message}{ctx_str}")


class FileTypeMismatchError(SubtitleError):
    def __init__(self, input_file: str, output_file: str):
        super().__init__(f"Input and output formats are incompatible: '{input_file}' -> '{output_file}'")

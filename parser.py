from cue import SubtitleCue
from utils import time_to_seconds
from exceptions import InvalidFormatError

def parse_srt(path: str) -> list[SubtitleCue]:
    cues = []
    with open(path, encoding="utf-8") as f:
        lines = [line.rstrip() for line in f]

    i = 0
    while i < len(lines):
        if lines[i].isdigit():
            if i + 1 >= len(lines):
                raise InvalidFormatError("Unexpected end of file", path, i + 1)
            try:
                start, end = lines[i + 1].split(" --> ")
            except ValueError:
                raise InvalidFormatError("Invalid SRT timing line", path, i + 2)

            try:
                start_sec = time_to_seconds(start)
                end_sec = time_to_seconds(end)
            except ValueError as e:
                raise InvalidFormatError(str(e), path, i + 2)

            i += 2
            text = []
            while i < len(lines) and lines[i]:
                text.append(lines[i])
                i += 1

            cues.append(
                SubtitleCue(start=start_sec, end=end_sec, text="\n".join(text))
            )
        else:
            i += 1

    return cues


def parse_vtt(path: str) -> list[SubtitleCue]:
    cues = []
    with open(path, encoding="utf-8") as f:
        # Keep original lines to maintain accurate line numbers
        lines = [line.strip() for line in f]

    if not lines or lines[0] != "WEBVTT":
        raise InvalidFormatError("Missing WEBVTT header", path, 1)

    i = 1
    while i < len(lines):
        if not lines[i]:
            i += 1
            continue
            
        if "-->" in lines[i]:
            try:
                start, end = lines[i].split(" --> ")
                start_sec = time_to_seconds(start)
                end_sec = time_to_seconds(end)
            except ValueError as e:
                raise InvalidFormatError(str(e), path, i + 1)

            i += 1
            text = []
            while i < len(lines) and lines[i] and "-->" not in lines[i]:
                text.append(lines[i])
                i += 1

            cues.append(
                SubtitleCue(start=start_sec, end=end_sec, text="\n".join(text))
            )
        else:
            # Skip identifier strings or bad lines
            i += 1

    return cues

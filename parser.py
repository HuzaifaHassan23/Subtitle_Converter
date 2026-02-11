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
            try:
                start, end = lines[i + 1].split(" --> ")
            except ValueError:
                raise InvalidFormatError("Invalid SRT timing line")

            start_sec = time_to_seconds(start)
            end_sec = time_to_seconds(end)

            i += 2
            text = []
            while i < len(lines) and lines[i]:
                text.append(lines[i])
                i += 1

            cues.append(
                SubtitleCue(start=start_sec, end=end_sec, text="\n".join(text))
            )
        i += 1

    return cues


def parse_vtt(path: str) -> list[SubtitleCue]:
    cues = []
    with open(path, encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]

    if lines[0] != "WEBVTT":
        raise InvalidFormatError("Missing WEBVTT header")

    i = 1
    while i < len(lines):
        if "-->" in lines[i]:
            start, end = lines[i].split(" --> ")
            start_sec = time_to_seconds(start)
            end_sec = time_to_seconds(end)

            i += 1
            text = []
            while i < len(lines) and "-->" not in lines[i]:
                text.append(lines[i])
                i += 1

            cues.append(
                SubtitleCue(start=start_sec, end=end_sec, text="\n".join(text))
            )
        else:
            i += 1

    return cues

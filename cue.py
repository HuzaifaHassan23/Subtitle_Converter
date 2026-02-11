from dataclasses import dataclass

@dataclass
class SubtitleCue:
    start: float
    end: float
    text: str

import re

# Accept optional hours: (HH:)?MM:SS[.,]ms  where ms is 1-3 digits
_TIME_RE = re.compile(r'^(?:(\d{1,2}):)?(\d{1,2}):(\d{2})[.,](\d{1,3})$')

def time_to_seconds(timestamp: str) -> float:
    """
    Parse timestamps like:
      - "01:02:03.456"  (HH:MM:SS.mmm)
      - "02:03.456"     (MM:SS.mmm)  <-- allowed
      - accepts '.' or ',' as ms separator and 1-3 ms digits
    Returns seconds (float).
    Raises ValueError on invalid format.
    """
    t = timestamp.strip()
    m = _TIME_RE.match(t)
    if not m:
        raise ValueError(f"Invalid timestamp format: '{timestamp}'")
    h_group, mm, ss, ms_digits = m.groups()
    h = int(h_group) if h_group is not None else 0
    mm = int(mm)
    ss = int(ss)
    ms = int(ms_digits)
    # Normalize ms (1 digit -> *100, 2 digits -> *10)
    if len(ms_digits) == 1:
        ms *= 100
    elif len(ms_digits) == 2:
        ms *= 10
    total_seconds = h * 3600 + mm * 60 + ss + ms / 1000.0
    return total_seconds

def seconds_to_srt(seconds: float) -> str:
    ms = int((seconds % 1) * 1000)
    s = int(seconds) % 60
    m = int(seconds // 60) % 60
    h = int(seconds // 3600)
    return f"{h:02}:{m:02}:{s:02},{ms:03}"


def seconds_to_vtt(seconds: float) -> str:
    return seconds_to_srt(seconds).replace(",", ".")

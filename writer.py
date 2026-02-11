from utils import seconds_to_srt, seconds_to_vtt

def write_srt(cues, output_path):
    with open(output_path, "w", encoding="utf-8") as f:
        for i, cue in enumerate(cues, start=1):
            f.write(f"{i}\n")
            f.write(
                f"{seconds_to_srt(cue.start)} --> "
                f"{seconds_to_srt(cue.end)}\n"
            )
            f.write(cue.text + "\n\n")


def write_vtt(cues, output_path):
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("WEBVTT\n\n")
        for cue in cues:
            f.write(
                f"{seconds_to_vtt(cue.start)} --> "
                f"{seconds_to_vtt(cue.end)}\n"
            )
            f.write(cue.text + "\n\n")

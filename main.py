import os
from parser import parse_srt, parse_vtt
from writer import write_srt, write_vtt
from exceptions import SubtitleError, FileTypeMismatchError

def main():
    input_path = "C:/Users/Geo Computer/OneDrive/Desktop/input.vtt"
    output_path = "C:/Users/Geo Computer/OneDrive/Desktop/output.srt"

    if not os.path.exists(input_path):
        print("Error: File does not exist.")
        return

    try:
        if input_path.endswith(".srt") and output_path.endswith(".vtt"):
            cues = parse_srt(input_path)
            write_vtt(cues, output_path)

        elif input_path.endswith(".vtt") and output_path.endswith(".srt"):
            cues = parse_vtt(input_path)
            write_srt(cues, output_path)

        else:
            raise FileTypeMismatchError(
                "Input and output formats are incompatible"
            )

        print("Conversion successful!")

    except SubtitleError as e:
        print(f"Subtitle error: {e}")

    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()

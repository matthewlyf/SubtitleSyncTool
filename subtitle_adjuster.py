from datetime import datetime, timedelta

def parse_srt_timestamp(timestamp):
    """Parse a timestamp from an SRT file into a datetime object."""
    clean_timestamp = timestamp.strip()
    return datetime.strptime(clean_timestamp, "%H:%M:%S,%f")

def format_srt_timestamp(dt):
    """Format a datetime object into a timestamp for an SRT file."""
    return dt.strftime("%H:%M:%S,%f")[:-3]

def adjust_subtitle_timing(srt_content, offset_seconds):
    """
    Adjust subtitle timings by a specified offset in seconds.
    Args:
        srt_content (str): The content of the SRT file.
        offset_seconds (int): The number of seconds to adjust the timing.
    Returns:
        str: The adjusted SRT content.
    """
    offset_duration = timedelta(seconds=offset_seconds)
    adjusted_content = []

    for line in srt_content.splitlines():
        if '-->' in line:
            start_str, end_str = line.split(' --> ')
            start_dt = parse_srt_timestamp(start_str)
            end_dt = parse_srt_timestamp(end_str)
            start_dt += offset_duration
            end_dt += offset_duration
            line = f"{format_srt_timestamp(start_dt)} --> {format_srt_timestamp(end_dt)}"
        adjusted_content.append(line)

    return "\n".join(adjusted_content)

def read_srt_file(file_path):
    """Read the content of an SRT file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def write_srt_file(file_path, content):
    """Write content to an SRT file."""
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)


# SubtitleSyncTool

A Python utility for adjusting subtitle timings in SRT files, allowing precise synchronization with customizable offsets and seamless formatting support.

## Features
- Adjust subtitle timings by a specified offset in seconds.
- Automatically handle common formatting issues in SRT files.

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/matthewlyf/SubtitleSyncTool.git
    ```

## Usage
1. Place your SRT file in the `examples/` directory.
2. Run the script:
    ```python
    from subtitle_adjuster import read_srt_file, write_srt_file, adjust_subtitle_timing

    # File paths
    input_file = "input.srt"  # Path to the input SRT file
    output_file = "output.srt"  # Path to the output SRT file

    # Offset in seconds
    offset_seconds = 3

    # Read the input SRT content
    srt_content = read_srt_file(input_file)

    # Adjust the subtitle timings by the specified offset
    adjusted_content = adjust_subtitle_timing(srt_content, offset_seconds)

    # Write the adjusted subtitles to the output file
    write_srt_file(output_file, adjusted_content)

    print(f"Subtitle timing adjusted by {offset_seconds} seconds and saved to {output_file}")
    ```

3. Check the adjusted output in the specified output file.

## Example
### Input (`input.srt`)
```plaintext
1
00:00:01,000 --> 00:00:05,000
Hello, World!

2
00:00:06,000 --> 00:00:10,000
Welcome to the Subtitle Adjuster!
```

### Output (`output.srt`) After Adjustment (Offset: 3 seconds)
```plaintext
1
00:00:04,000 --> 00:00:08,000
Hello, World!

2
00:00:09,000 --> 00:00:13,000
Welcome to the Subtitle Adjuster!
```

## License
[MIT License](LICENSE)

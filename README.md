
# SubtitleSyncTool

A Python tool for adjusting subtitle timings in SRT files.

## Features
- Adjust subtitle timings by a specified offset in seconds.
- Automatically handle common formatting issues in SRT files.

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/matthewlyf/SubtitleSyncTool.git
    ```
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
1. Place your SRT file in the `examples/` directory.
2. Run the script:
    ```bash
    python src/subtitle_adjuster.py
    ```
3. Check the adjusted output in the specified output file.

## Example
Input:
```plaintext
1
00:00:01,000 --> 00:00:05,000
Hello, World!
```

Output (after offset of 2 seconds):
```plaintext
1
00:00:03,000 --> 00:00:07,000
Hello, World!
```



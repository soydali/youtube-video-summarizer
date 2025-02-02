# YouTube Video Summary Generator

This Python script retrieves the subtitles of a given YouTube video and generates a concise and descriptive summary using the Groq API.

## Features
- Automatically retrieves subtitles from a YouTube video.
- Performs text analysis using the Groq API and generates a summary.

## Requirements
The following libraries need to be installed for this script to work:

```pip
pip install groq youtube-transcript-api
```

Additionally, you need to create a [Groq API](https://console.groq.com/keys) key.

## Usage
1. Run the script:
   ```python
   python main.py
   ```
2. Enter the video link.
3. Script retrives subtitles then send to Groq API key and AI model returns the summary.

## Configuration
- Replace the `API_KEY` variable with your own Groq API key.

## Example Execution
```sh
Video link: https://www.youtube.com/watch?v=abcd1234
Summary: This video covers the topic of XYZ and the key points are...
```


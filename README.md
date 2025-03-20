# WhisperFlow - Real-time & File Transcription

## Overview
WhisperFlow is a real-time speech-to-text transcription tool powered by OpenAI's Whisper model. It supports both microphone input and file-based transcription with GPU acceleration.

## Features
- 🎤 **Live transcription**: Capture audio directly from the microphone.
- 📂 **File-based transcription**: Import `.wav`, `.mp3`, `.m4a`, and other formats.
- ⚡ **CUDA support**: Leverages NVIDIA GPUs for faster inference.
- 🌍 **Multilingual support**: Set a preferred language or use `Auto Detect`.
- 🔠 **Model selection**: Choose between `tiny`, `small`, `medium`, or `large` models.
- 📝 **Custom prompt**: Improve transcription accuracy with predefined prompts.
- 🚀 **Optimized performance**: Uses FP16 precision and tuned parameters.
- ❌ **Triton disabled**: Avoids potential issues on Windows.

## Installation

### 1. Install Dependencies
Ensure you have Python 3.9+ installed and create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

Install required packages:

```bash
pip install -r requirements.txt
```

### 2. Install FFmpeg
FFmpeg is required for processing audio files. Install it via:

```bash
sudo apt install ffmpeg  # Linux
choco install ffmpeg     # Windows (using Chocolatey)
brew install ffmpeg      # macOS
```

### 3. Run the Application
```bash
python whisperflow_app.py
```

## Usage
### Microphone Transcription
1. Click **Start Recording** to begin capturing audio.
2. Click **Stop Recording & Transcribe** to process and display the transcript.
3. Transcription appears in the text box and is copied to the clipboard.

### File-based Transcription
1. Click **Transcription Configuration**.
2. Import audio files (`.wav`, `.mp3`, `.flac`, etc.).
3. Adjust model, language, and other settings.
4. Click **Transcribe** to process selected files.

## Configuration Options
| Setting               | Description |
|----------------------|-------------|
| **Model**            | Choose `tiny`, `small`, `medium`, or `large` |
| **Transcription Language** | Set a preferred language (or Auto Detect) |
| **Translate to English** | Convert output to English (not implemented yet) |
| **Max Characters per Segment** | (Placeholder, not active in PyPI Whisper) |
| **Prompt** | Improve accuracy with a custom transcription prompt |

## Known Issues & Workarounds
- **Windows GPU users** may experience errors with Triton. This is disabled by default using:
  ```python
  os.environ["WHISPER_FORCE_DISABLE_TRITON"] = "1"
  ```
- **WSL users** may need additional configuration for PortAudio (`sounddevice` issues).

## Future Improvements
- 🔧 **GUI Enhancements**: A settings panel to choose model, language, and configure Whisper directly.
- 🗂 **Drag & Drop File Support**: Easier file selection for batch transcription.
- 🌐 **Translation Support**: Implement `task="translate"` for multilingual users.

## Contributing
Feel free to fork this repository, submit issues, or suggest improvements!

## License
This project is open-source and follows the MIT License.

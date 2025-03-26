# WhisperFlow - Real-time Audio Transcription

## Overview

**WhisperFlow** is a simple real-time speech transcription project using OpenAI’s [Whisper](https://github.com/openai/whisper) model. Currently, the app records audio from the microphone, saves it to an `audio.wav` file, and performs transcription in the background.

> **Note:** Some initially mentioned features (like multi-model selection in the UI, direct file transcription, English translation, etc.) **haven’t been implemented yet**. They are only future ideas.

---

## Features (Implemented)

- 🎤 **Real-time transcription**: Records audio through the microphone and saves locally.
    
- ⚡ **GPU acceleration (CUDA)**: Uses NVIDIA GPUs for faster inference (if available).
    
- 🔠 **Custom prompt**: Includes an initial prompt to improve punctuation accuracy.
    
- ❌ **Triton disabled**: Avoids compatibility issues on Windows.
    

## Features (Planned / Not Implemented)

- 📂 **File-based transcription**: Import `.wav`, `.mp3`, `.m4a` via the UI.
    
- 🌍 **Full multilingual support**: Currently, the code is set to Portuguese only.
    
- 📝 **UI model selection**: Right now, the code defaults to the `small` model.
    
- 🌐 **English translation**: The `task="translate"` parameter isn’t added yet.
    
- 🔧 **Advanced settings window**: An easy way to adjust Whisper parameters.
    
- 🗂 **Drag & drop**: Drag and drop files for easier transcription.
    
- 📝 **Character-based segmentation**: Not implemented yet.
    

---

## Installation

### 1. Python Environment

Make sure you have Python 3.9+ installed. Create and activate a virtual environment:

bash

CopiarEditar

`python -m venv venv # Linux/macOS: source venv/bin/activate # Windows: venv\Scripts\activate`

Then install the required packages:

bash

CopiarEditar

`pip install -r requirements.txt`

### 2. FFmpeg

FFmpeg is required to handle audio processing. Install it according to your operating system:

bash

CopiarEditar

`# Linux (Debian/Ubuntu) sudo apt install ffmpeg  # Windows (via Chocolatey) choco install ffmpeg  # macOS (via Homebrew) brew install ffmpeg`

### 3. Running the Application

Run the main file (e.g., `whisperflow_app.py` or `main.py`):

bash

CopiarEditar

`python whisperflow_app.py`

---

## Usage

### Microphone Transcription

1. Click **Start Recording** to begin capturing audio.
    
2. Speak normally; the app stores audio in memory.
    
3. Click **Stop Recording & Transcribe** to finalize capture.
    
4. The audio is saved as `audio.wav` and transcribed in the background.
    
5. The result appears in the UI and is automatically copied to the clipboard (Windows only).
    

---

## Code Settings

Currently, the configuration is fixed in the script:

- **Model:** The code uses `"small"` by default. To change, edit the `MODEL_NAME` variable (e.g., `"tiny"`, `"medium"`, etc.).
    
- **Language:** The `transcribe` method is set to `"portuguese"`. Adjust as desired.
    
- **Initial Prompt:** Used to improve punctuation. Change or remove it as needed.
    

> If no GPU is available, the code automatically defaults to CPU mode.

---

## Known Issues

- **Windows compatibility**: Triton is disabled by default to avoid errors related to Whisper on Windows.
    
- **WSL**: If running under Windows Subsystem for Linux (WSL), additional setup might be needed for `sounddevice` to capture audio.
    

---

## Future Improvements

- 📂 **File-based Transcription**: Load audio files directly via the UI.
    
- 🌐 **Translation**: Add `task="translate"` to convert transcripts to English.
    
- 🗂 **Settings Panel**: Select model, language, and Whisper’s advanced parameters in the app.
    
- 📝 **Segmentation**: Control the maximum character length per segment.
    
- 🗃️ **Batch Processing**: Support multiple files in sequence.
    

---

## Contributing

Feel free to open **issues**, submit PRs, or propose discussions for new features. Contributions are welcome!

---

## License

This project is open-source under the [MIT](LICENSE) License.
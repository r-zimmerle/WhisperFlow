import os

# Force-disable Triton to avoid warnings or errors on Windows
os.environ["WHISPER_FORCE_DISABLE_TRITON"] = "1"

import whisper
import sounddevice as sd
import numpy as np
import wave
import torch
import customtkinter as ctk
import threading

# Whisper Turbo model configuration
MODEL_NAME = "small"
device = "cuda" if torch.cuda.is_available() else "cpu"
model = whisper.load_model(MODEL_NAME).to(device)

# Audio configuration
SAMPLE_RATE = 16000
CHANNELS = 1
OUTPUT_FILE = "audio.wav"
frames = []
recording = False
is_transcribing = False

def record_audio():
    """Starts audio recording."""
    global frames, recording
    frames = []  # Ensure frames always starts as an empty list
    recording = True
    print("🎙️ Recording... Press 'Stop Recording' to finish.")

    def callback(indata, frame_count, time_info, status):
        if recording:
            frames.append(indata.copy())  # Correctly append audio frames

    with sd.InputStream(samplerate=SAMPLE_RATE, channels=CHANNELS, callback=callback):
        while recording:
            sd.sleep(100)  # Controls recording flow

def stop_recording():
    """Stops recording, saves the file, and starts transcription in a background thread."""
    global recording
    recording = False
    print("🛑 Recording stopped. Will now transcribe in background...")

    if len(frames) == 0:
        print("No audio captured.")
        return

    audio_data = np.concatenate(frames, axis=0)
    with wave.open(OUTPUT_FILE, "wb") as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(2)
        wf.setframerate(SAMPLE_RATE)
        wf.writeframes((audio_data * 32767).astype(np.int16).tobytes())

    # Run transcribe_audio in a separate thread to avoid freezing the UI
    threading.Thread(target=transcribe_audio, daemon=True).start()

def transcribe_audio():
    """Transcribes the recorded audio in the background and displays it in the UI."""
    global is_transcribing
    is_transcribing = True

    text_output.delete("1.0", "end")
    text_output.insert("end", "Transcribing... Please wait.\n")
    print("🔎 Transcribing in background...")

    # Perform the transcription
    result = model.transcribe(
        OUTPUT_FILE,
        language="portuguese",
        fp16=True,            # half-precision => faster on most GPUs
        temperature=0,        # fully deterministic
        beam_size=1,
        best_of=1,
        word_timestamps=False,# skip word timing for speed
        no_speech_threshold=0.4,
        condition_on_previous_text=False,
        initial_prompt="Please use correct punctuation, including periods and commas."
    )

    # Update the UI after transcribing
    text_output.delete("1.0", "end")
    text_output.insert("end", result["text"])

    # Copy to clipboard (Windows only)
    os.system(f'echo {result["text"].strip()} | clip')
    text_output.insert("end", "\n(Transcription copied to clipboard!)")
    print("📋 Transcription copied to clipboard!")

    is_transcribing = False

def start_recording_thread():
    """Starts recording in a separate thread."""
    threading.Thread(target=record_audio, daemon=True).start()

def exit_app():
    """Cleanly exit the application."""
    print("Exiting application...")
    app.quit()  # or app.destroy()

# Create UI with CustomTkinter
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("500x450")
app.title("Whisper Turbo Transcriber (No Triton)")

label = ctk.CTkLabel(app, text="Whisper Turbo - Speech-to-Text", font=("Arial", 18))
label.pack(pady=10)

start_button = ctk.CTkButton(app, text="Start Recording", command=start_recording_thread)
start_button.pack(pady=10)

stop_button = ctk.CTkButton(app, text="Stop Recording & Transcribe", command=stop_recording)
stop_button.pack(pady=10)

text_output = ctk.CTkTextbox(app, height=200, wrap="word")
text_output.pack(padx=10, pady=10, fill="both", expand=True)

exit_button = ctk.CTkButton(app, text="Exit", command=exit_app)
exit_button.pack(pady=5)

app.mainloop()

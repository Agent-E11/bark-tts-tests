#!/usr/bin/env python

from bark import (
    SAMPLE_RATE,
    generate_audio,
    preload_models,
)
from scipy.io import wavfile

if input("Download models and generate audio? (y/N): ") not in ("y", "Y"):
    print("Exiting")
    exit(0)

# Download and load all models
preload_models()

# Generate audio from prompt
text_prompt = """
    Hello, I am robot.
"""
audio_array = generate_audio(text_prompt)

# Write to a .wav file
wavfile.write("output/bark_generation.wav", SAMPLE_RATE, audio_array)

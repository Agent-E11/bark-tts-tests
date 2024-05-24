#!/usr/bin/env python

from sys import argv
from nltk import sent_tokenize

from bark import (
    SAMPLE_RATE,
    generate_audio,
    preload_models,
)
from scipy.io import wavfile
import numpy as np

file_name = "prompt.txt" if len(argv) < 2 else argv[1]

text_prompt = ""
with open(file_name, "r") as f:
    for line in f:
        text_prompt += line.replace("\n", " ")

sentences = sent_tokenize(text_prompt)

if input("Download models and generate audio? (y/N): ") not in ("y", "Y"):
    print("Exiting")
    exit(0)

# Download and load all models
preload_models()

speaker = "v2/en_speaker_6"
silence = np.zeros(int(0.25 * SAMPLE_RATE)) # Quarter second of silence

pieces = []
for sentence in sentences:
    audio_array_piece = generate_audio(sentence)
    pieces += [audio_array_piece, silence.copy()]

audio_array = np.concatenate(pieces)

# Generate audio from prompt
audio_array = generate_audio(text_prompt)

# Write to a .wav file
wavfile.write("output/long_generation.wav", SAMPLE_RATE, audio_array)

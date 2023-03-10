import os

from mido import MidiFile


MIDI_FOLDER_ROOT = "adl-piano-midi"


for root, _, files in os.walk(MIDI_FOLDER_ROOT):
    midi_files = [os.path.join(root, file) for file in files if file[-4:] == ".mid"]

    for midi_file in midi_files:
        midi = MidiFile(midi_file)
        print(midi.filename, midi.length)
        # print([msg for msg in midi if not msg.is_meta])
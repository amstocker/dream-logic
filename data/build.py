import os

from mido import MidiFile


MIDI_FOLDER_ROOT = "adl-piano-midi"
META_MESSAGE_SET_TEMPO = "set_tempo"


def midi_tempo_to_bpm(micros_per_beat):
    return 60_000_000 / micros_per_beat


for root, _, files in os.walk(MIDI_FOLDER_ROOT):
    midi_files = [os.path.join(root, file) for file in files if file[-4:] == ".mid"]

    for filename in midi_files:
        midi = MidiFile(filename)
        print(midi.filename, midi.length)
        for meta_msg in [msg for msg in midi if msg.is_meta]:
            if meta_msg.type == META_MESSAGE_SET_TEMPO:
                print(midi_tempo_to_bpm(meta_msg.tempo))
                break
        else:
            print("\tNo \"{}\" meta message!".format(META_MESSAGE_SET_TEMPO))
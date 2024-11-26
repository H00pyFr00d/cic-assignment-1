from player import play
from time import sleep

c_major = ["c", "d", "e", "f", "g", "a", "b", "c"]
d_major = ["d", "e", "f#", "g", "a", "b", "c#", "d"]
octave = 4

# Play each note in the c_major scale beginning at C 4
for index, note in enumerate(c_major):
    if note == "c" and index != 0:
        octave += 1
    play(note, octave)

# Wait 1 second
sleep(1)
octave = 4

# Doesn't work for d_major!
for index, note in enumerate(d_major):
    if note == "c" and index != 0:
        octave += 1
    play(note, octave)

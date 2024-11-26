from player import play

# Solution:
# D major scale given in example
scale = ["d", "e", "f#", "g", "a", "b", "c#", "d"]
octave = 4

# Scores for how far a note is from C
score = {"c": 0, "c#": 1, "d": 2, "d#": 3, "e": 4, "f": 5, "f#": 6, "g": 7, "g#": 8, "a": 9, "a#": 10, "b": 11}

# Make a list of notes paired with their scores
scored = [(note, score[note]) for note in scale]
# Sort the list by the scores and take the lowest score
inc_note = sorted(scored, key=lambda x: x[1])[0][0]

# Play each note in the scale starting at the fourth octave
for index, note in enumerate(scale):
    print(note, inc_note)
    if note == inc_note and index != 0:
        octave += 1
    play(note, octave)
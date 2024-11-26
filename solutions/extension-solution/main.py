from player import play, cycle
from checker import is_music_note
from time import sleep

list_of_fifths = ["c", "g", "d", "a", "e", "b", "f#", "c#", "g#", "d#", "a#", "f"]

# Get the major scale for the provided root
def get_major_scale(root):
    # Check that the input is a valid music note
    if not is_music_note(root):
        raise ValueError("Invalid root note")

    # Solution:
    cycled = cycle(list_of_fifths, list_of_fifths.index(root))
    forwards = cycled[:6]
    backwards = cycled[-1:]

    # Put the notes in alphabetical order
    notes = sorted(forwards + backwards)

    # Return the notes, starting at the root with an extra root on the end
    return cycle(notes, notes.index(root)) + [root]

# Get the relative minor for the provided root note
def get_relative_minor(root):
    # Check that the input is a valid music note
    if not is_music_note(root):
        raise ValueError("Invalid root note")

    # The relative minor is three ahead of the given note
    rm_idx = list_of_fifths.index(root) + 3
    relative_minor = list_of_fifths[rm_idx]
    
    return relative_minor

# Adapted from snippet 2
def play_scale(scale, octave):    
    # Scores for how far a note is from C
    score = {"c": 0, "c#": 1, "d": 2, "d#": 3, "e": 4, "f": 5, "f#": 6, "g": 7, "g#": 8, "a": 9, "a#": 10, "b": 11}
    
    # Make a list of notes paired with their scores
    scored = [(note, score[note]) for note in scale]
    # Sort the list by the scores and take the lowest score
    inc_note = sorted(scored, key=lambda x: x[1])[0][0]

    for index, note in enumerate(scale):
        if note == inc_note and index != 0:
            octave += 1
        play(note, octave)

def play_major_and_relative_minor(root):
    # Get the major scale (snippet 4)
    major = get_major_scale(root)
    # Get the relative minor and construct the scale (snippet 5)
    relative_minor = get_relative_minor(root)
    minor = cycle(major[0:-1], major.index(relative_minor)) + [relative_minor]

    # Play the scales
    play_scale(major, 4)
    sleep(1)
    play_scale(minor, 3)

play_major_and_relative_minor("c")
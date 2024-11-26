from checker import is_music_note
from player import cycle

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
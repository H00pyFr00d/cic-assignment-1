from checker import is_music_note
from player import cycle

list_of_fifths = ["c", "g", "d", "a", "e", "b", "f#", "c#", "g#", "d#", "a#", "f"]

# Get the major scale for the provided root
def get_major_scale(root):
    # Check that the input is a valid music note
    if not is_music_note(root):
        raise ValueError("Invalid root note: " + root)

    # Todo: get the list of fifths set to the root
    cycled = cycle(list_of_fifths, ???)

    # Todo: Get the first 6 elements of the list
    forwards = cycled[:???]
    # Todo: Get the last element of the list
    backwards = cycled[???]

    # Put the notes in alphabetical order
    notes = sorted(forwards + backwards)

    # Return the notes, starting at the root with an extra root on the end
    return cycle(notes, ???) + [root]

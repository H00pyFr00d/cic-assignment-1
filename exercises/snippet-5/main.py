from checker import is_music_note

list_of_fifths = ["c", "g", "d", "a", "e", "b", "f#", "c#", "g#", "d#", "a#", "f"]

# Get the relative minor for the provided root note
def get_relative_minor(root):
    # Check that the input is a valid music note
    if not is_music_note(root):
        raise ValueError("Invalid root note")

    # The relative minor is three ahead of the given note
    rm_idx = list_of_fifths.index(root) + 3
    relative_minor = list_of_fifths[rm_idx]
    
    return relative_minor
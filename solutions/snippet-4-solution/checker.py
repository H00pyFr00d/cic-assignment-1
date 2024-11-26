whole = ["a", "b", "c", "d", "e", "f", "g"]
sharps = ["a#", "c#", "d#", "f#", "g#"]
flats = ["ab", "bb", "db", "eb", "gb"]

def is_music_note(note):
    return note in whole + sharps + flats
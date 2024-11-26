import music

def play(note: str, octave: int):
    print(" - play: " + note + str(octave))
    music.play(note + str(octave) + ":" + "4")

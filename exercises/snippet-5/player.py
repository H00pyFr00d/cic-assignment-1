import music

def play(note: str, octave: int):
    print(" - play: " + note + str(octave))
    music.play(note + str(octave) + ":" + "4")

# Cycles n elements through the provided list
def cycle(list, n):
    start = list[:n]
    end = list[n:]

    cycled = end + start
    return cycled
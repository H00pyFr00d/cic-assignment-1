from player import play

c_major = ["c", "d", "e", "f", "g", "a", "b", "c"]

# Todo: finish c_major_power
c_major_power = c_major[0] + c_major[4] + c_major[7]

# Play the notes in c_major_power
for note in c_major_power:
    # Play the given note at the 4th octave
    play(note, 4)
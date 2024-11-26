list_of_fifths = ["c", "g", "d", "a", "e", "b", "f#", "c#", "g#", "d#", "a#", "f"]

# Cycles n elements through the provided list
def cycle(list, n):
    start = list[:n]
    end = list[n:]

    cycled = end + start
    return cycled

cycled = cycle(list_of_fifths, 3)
print(cycled)

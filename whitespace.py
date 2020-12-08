
def whitespace(sequence):
    return " ".join(sorted(list(set(sequence.split()))))

print(whitespace("hello world and practice makes perfect and hello world again"))
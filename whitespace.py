
def whitespace(sequence):
    lst = list(set(sequence.split()))
    return sorted(lst)

print(whitespace("hello world and practice makes perfect and hello world again"))
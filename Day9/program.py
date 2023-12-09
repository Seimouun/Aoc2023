def setup():
    with open('input.txt') as file:
        sequences = []
        for line in file.readlines():
            sequences.append([int(numb.strip()) for numb in line.split(' ')])
        
        print(sum(p1_getNextInSequence(seq) for seq in sequences))


def p1_getNextInSequence(seq: list[int]):
    next = 0
    if all(x == 0 for x in seq):
        return next
    next_seq = [seq[i+1] - seq[i] for i in range(len(seq)-1)]
    next += seq[len(seq)-1] + p1_getNextInSequence(next_seq)
    return next

def p2_getPrevInSequence(seq: list[int]):
    next = 0
    if all(x == 0 for x in seq):
        return next
    next_seq = [seq[i+1] - seq[i] for i in range(len(seq)-1)]
    next += seq[0] - p2_getPrevInSequence(next_seq)
    return next


setup()
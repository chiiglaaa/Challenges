import itertools

def stairs_in_20(stairs):
    return sum(list(itertools.chain(*stairs))) * 20

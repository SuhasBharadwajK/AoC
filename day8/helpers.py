segment_maps = {
    0: ['a', 'b', 'c', 'e', 'f', 'g'],
    1: ['c', 'f'], # Unique
    2: ['a', 'c', 'd', 'e', 'g'],
    3: ['a', 'c', 'd', 'f', 'g'],
    4: ['b', 'c', 'd', 'f'], # Unique
    5: ['a', 'b', 'd', 'f', 'g'],
    6: ['a', 'b', 'd', 'e', 'f', 'g'],
    7: ['a', 'c', 'f'], # Unique
    8: ['a', 'b', 'c', 'd', 'e', 'f', 'g'], # Unique
    9: ['a', 'b', 'c', 'd', 'f', 'g'],
}

unique_numbers = [1, 4, 7, 8]

def get_segment_map_lenghts() -> dict[int: list]:
    segment_map_lengths: dict[int: list] = {}
    for i in range(0, 10):
        length = len(segment_maps[i])
        if length not in segment_map_lengths.keys():
            segment_map_lengths[length] = [i]
        else:
            segment_map_lengths[length].append(i)
        pass

    return segment_map_lengths
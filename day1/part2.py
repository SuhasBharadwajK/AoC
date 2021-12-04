def program(depths):
    window = 3
    sums = list()
    for i in range(window - 1, len(depths)):
        subarray = depths[i - (window - 1): i + 1]
        sums.append(sum(subarray))

    count = 0
    for i in range(1, len(sums)):
        if sums[i] > sums[i - 1]:
            count += 1

    return count

def program_optimized(depths):
    window = 3
    count = 0
    for i in range(window, len(depths)):
        if depths[i] > depths[i - window]:
            count += 1
    
    return count
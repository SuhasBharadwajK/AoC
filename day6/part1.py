def program(school):
    total = 0
    for fish in school:
        total += get_school(fish, 256)
    return total


def get_school(current_fish, days_to_wait):
    school = [current_fish]

    for i in range(0, days_to_wait):
        for j in range(0, len(school)):
            if school[j] == 0:
                school[j] = 6
                school.append(8)
            else:
                school[j] -= 1
            pass

    return len(school)
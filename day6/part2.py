# a = [5,1,4,1,5,1,1,5,4,4,4,4,5,1,2,2,1,3,4,1,1,5,1,5,2,2,2,2,1,4,2,4,3,3,3,3,1,1,1,4,3,4,3,1,2,1,5,1,1,4,3,3,1,5,3,4,1,1,3,5,2,4,1,5,3,3,5,4,2,2,3,2,1,1,4,1,2,4,4,2,1,4,3,3,4,4,5,3,4,5,1,1,3,2,5,1,5,1,1,5,2,1,1,4,3,2,5,2,1,1,4,1,5,5,3,4,1,5,4,5,3,1,1,1,4,5,3,1,1,1,5,3,3,5,1,4,1,1,3,2,4,1,3,1,4,5,5,1,4,4,4,2,2,5,5,5,5,5,1,2,3,1,1,2,2,2,2,4,4,1,5,4,5,2,1,2,5,4,4,3,2,1,5,1,4,5,1,4,3,4,1,3,1,5,5,3,1,1,5,1,1,1,2,1,2,2,1,4,3,2,4,4,4,3,1,1,1,5,5,5,3,2,5,2,1,1,5,4,1,2,1,1,1,1,1,2,1,1,4,2,1,3,4,2,3,1,2,2,3,3,4,3,5,4,1,3,1,1,1,2,5,2,4,5,2,3,3,2,1,2,1,1,2,5,3,1,5,2,2,5,1,3,3,2,5,1,3,1,1,3,1,1,2,2,2,3,1,1,4,2]
#a = [3,4,3,1,2]
from collections import Counter, defaultdict

def program(a):
    c = Counter(a)
    for i in range(256):
        # loop invariant
        tmp = defaultdict(int)
        for k,v in c.items(): #k,v = 7,4
            if k == 0:
                tmp[8] = c[k]
                tmp[6] += c[k]
            else:
                tmp[k-1] += c[k] #k,v=6,4
            #print(k, tmp)
        #print('--inner done--')
        c= Counter(tmp)

    total = 0
    for _,v in c.items():
        total += v

    return total


##########################################################################################
## Discarded solutions:

current_fish = 2
number_of_days = 7
days_to_wait = 256

# school = [current_fish]

timer_on_day = lambda n, k: ((7 - n % 7) % 7) - (7 % (k + 1) - 1) - 1
zeroes_by_day = lambda n, k: int((n + (6 - k)) / 7)
reduction_factor = lambda n, k: int(timer_on_day(n, k) / (timer_on_day(n, k) - 0.000001)) - 1
new_fish_by_day = lambda n, k: zeroes_by_day(n, k) + reduction_factor(n, k)
time_since_ith_fish = lambda n, k, i: n - ((k + 1) + 7 * (i) + 2)

# time_since_ith_fish(18, 3, 0)
# time_since_ith_fish(18, 3, 1)
# time_since_ith_fish(18, 3, 2)
# zeroes_by_day(time_since_ith_fish(18, 3, 1), 6)
# zeroes_by_day(time_since_ith_fish(18, 3, 2), 6)

# zeroes_by_day(18, 3)

# new_fish_by_day(18, 3)

def get_school(n, k):
    count = 1
    new_fish = new_fish_by_day(n, k)

    # print('n = ' + str(n))
    # print('k = ' + str(k))
    # print('-----------------------------------------')

    if new_fish < 0:
        return 0

    if new_fish == 0:
        return 1
    
    for i in range(0, new_fish):
        duration = time_since_ith_fish(n, k, i)
        count += get_school(duration, 6)
    # get_school()
    
    return count

school = {}
for i in range(0, 9):
    school[i] = 0

print(school)

start = 3

school[start] += 1

# for k, v in school:
#     if k == 0:
#         school[6] += v
#         school[8] = v

#     else:
#         school[k - 1] += v

# for i in [7, 14, 21, 28, 35, 49, 56, 63, 70]:
#     print('Total fish = ' + str(get_school(i, 3)))

# print('Total fish = ' + str(get_school(256, 3)))

# def get_school_old(current_fish, days_to_wait):
#     school = [current_fish]

#     for i in range(0, days_to_wait):
#         for j in range(0, len(school)):
#             if school[j] == 0:
#                 school[j] = 6
#                 school.append(8)
#             else:
#                 school[j] -= 1
#             pass

#     return len(school)

# get_school(6, 43)

# for i in range(1, days_to_wait + 1):
#     for j in range(0, len(school)):
#         if school[j] == 0:
#             school[j] = 6
#             school.append(8)
#         else:
#             school[j] -= 1
#         pass
    
# print(len(school))

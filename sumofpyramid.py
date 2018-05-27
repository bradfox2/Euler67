import random

def longest_slide_down(pyramid):
    if len(pyramid) == 1:
        print(pyramid[0][0])
        return(pyramid[0][0])
    else:
        lower = pyramid.pop()
        upper = pyramid.pop()
        new = [0]*len(upper)
        new[0] = max(upper[0] + lower[0], upper[0] + lower[1])
        new[-1] = max(upper[-1] + lower[-1], upper[-1] + lower[-2])
        for i in range(1,len(upper) - 1):
            new[i] = max(upper[i] + lower[i], upper[i] + lower[i + 1])
        pyramid.append(new)
    return(longest_slide_down(pyramid))

print(longest_slide_down([[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]) == 23)
print(longest_slide_down([
    [75],
    [95, 64],
    [17, 47, 82],
    [18, 35, 87, 10],
    [20,  4, 82, 47, 65],
    [19,  1, 23, 75,  3, 34],
    [88,  2, 77, 73,  7, 63, 67],
    [99, 65,  4, 28,  6, 16, 70, 92],
    [41, 41, 26, 56, 83, 40, 80, 70, 33],
    [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
    [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
    [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
    [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
    [63, 66,  4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
    [ 4, 62, 98, 27, 23,  9, 70, 98, 73, 93, 38, 53, 60,  4, 23],
    ])== 1074)

def make_pyr(depth = 100, highest_num = 100):
    pyr = [[random.randint(1,highest_num)]]
    while len(pyr) < depth:
        r = range(0, len(pyr) + 1)
        pyr.append([random.randint(1,highest_num) for i in r])
    return(pyr)


print(make_pyr(20,100))


longest_slide_down(make_pyr(975,100))



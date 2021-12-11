'''
  如果 a+b+c=1000，且 a^2+b^2=c^2（a,b,c 为自然数），如何求出所有a、b、c可能的组合?
'''

from stopwatch import stopwatch

# BAD: 3层for循环，时间复杂度为O(n^3)
@stopwatch
def combination_bad():
    for a in range(1001):
        for b in range(1001):
            for c in range(1001):
                if a**2 + b**2 == c**2 and a+b+c == 1000:
                    print("a, b, c: %d, %d, %d" % (a, b, c))

# GOOD: 2层for循环，时间复杂度为O(n^2)
@stopwatch
def combination_good():
    for a in range(1001):
        for b in range(1001-a):
            c = 1000 - a - b
            if a**2 + b**2 == c**2:
                print("a, b, c: %d, %d, %d" % (a, b, c))


if __name__ == '__main__':
    combination_bad()
    combination_good()

# BAD Output:
# a, b, c: 0, 500, 500
# a, b, c: 200, 375, 425
# a, b, c: 375, 200, 425
# a, b, c: 500, 0, 500
# Function combination() in model __main__ cost: 1137.25 seconds

# GOOD Output:
# a, b, c: 0, 500, 500
# a, b, c: 200, 375, 425
# a, b, c: 375, 200, 425
# a, b, c: 500, 0, 500
# Function combination() in model __main__ cost: 0.65625 seconds

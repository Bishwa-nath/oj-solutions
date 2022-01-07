import sys
def get_ints(): return map(int, sys.stdin.readline().strip().split())

n, m = get_ints()
i = 1
while m >= i:
    m -= i
    i += 1
    if i > n:
        i = 1
print(m)
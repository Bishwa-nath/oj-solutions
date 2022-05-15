import sys
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_ls(): return list(map(int, sys.stdin.readline().strip().split()))

def main():
    for _ in range(int(input())):
        s = input()
        n = len(s)
        total = 0
        for c in s:
            total += ord(c) - ord('a') + 1
        
        first = total - (ord(s[-1]) - ord('a')) - 1
        last = total - (ord(s[0]) - ord('a')) - 1
        first = first - (ord(s[-1]) - ord('a'))-1
        last = last - (ord(s[0]) - ord('a'))-1
        mx = max(first, last)
        if n == 1:
            print('Bob', total)
        else:

            if n%2 == 0: mx = total
            print('Alice', mx)

        

if __name__ == "__main__":
    main()
    
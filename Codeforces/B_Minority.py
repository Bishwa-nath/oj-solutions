import sys
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_ls(): return list(map(int, sys.stdin.readline().strip().split()))

def main():
    for _ in range(int(input())):
        s = input()
        zero = s.count('0')
        ones = len(s) - zero
        if ones == zero:
           print(ones-1)
        else:
            print(min(ones, zero))

if __name__ == "__main__":
    main()
    
import sys
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_ls(): return list(map(int, sys.stdin.readline().strip().split()))

def main():
    for _ in range(int(input())):
        x, y = get_ints()
        if y%x == 0:
            print(1,'',y//x)
        else:
            print('0 0')
        

if __name__ == "__main__":
    main()
    
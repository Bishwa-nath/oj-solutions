import sys
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_ls(): return list(map(int, sys.stdin.readline().strip().split()))

def main():
    for _ in range(int(input())):
        n = int(input())
        ls = get_ls()
        d = dict()
        for x in ls:
            if x not in d:
                d[x] = 1
            else:
                d[x] += 1
                
        mx = max(d.values())
        s = set(ls)
        len_s = len(s)-1
        if mx >= (len_s+2): len_s += 1
        print(min(mx, len_s))

        

if __name__ == "__main__":
    main()
    
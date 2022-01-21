import sys
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_ls(): return list(map(int, sys.stdin.readline().strip().split()))

def main():
    ca = 0
    cb=0
    cc =0
    vo = "aeiou"
    sa = input()
    sb = input()
    sc = input()
    for c in sa:
        if c in vo: ca += 1
    for c in sb:
        if c in vo: cb += 1
    for x in sc:
        if x in vo: cc += 1

    if ca == 5 and cb == 7 and cc == 5:
        print("YES")
    else: print("NO")

if __name__ == "__main__":
    main()
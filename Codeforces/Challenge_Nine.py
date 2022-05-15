import sys
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_ls(): return list(map(int, sys.stdin.readline().strip().split()))

def main():
    for k in range(int(input())):
        s = input()
        t = 0
        for c in s:
            t += int(c)
        rem = t%9
        rem = 9-rem
        if rem==0:
            print("Case #"+ str(k+1)+ ": " + s + str(rem))
        elif rem < int(s[0]):
            print("Case #"+ str(k+1)+ ": " + str(rem) + s)
        else:
            print("Case #"+ str(k+1)+ ": " + s + str(rem))
        

if __name__ == "__main__":
    main()
    
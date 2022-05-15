import sys
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_ls(): return list(map(int, sys.stdin.readline().strip().split()))

def main():
    for _ in range(int(input())):
        
        temp = []
        lower_alpha = "abcdefghijklmnopqrstuvwxyz"
        for i in lower_alpha:
            for j in lower_alpha:
                s = ''
                if i != j:
                    s += i
                    s += j
                    temp.append(s)
        
        ss = input()
        for i in range(650):
            if ss == temp[i]:
                print(i+1)
                break
        

if __name__ == "__main__":
    main()
    
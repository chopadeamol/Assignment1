def starPattern(star):
    for i in range(star):
        for j in range(star,i,-1):
            print("*", end='   ')
        print()

def main():
    print("Star pattern")
    no=int(input())
    s=starPattern(no)

if __name__=="__main__":
    main()
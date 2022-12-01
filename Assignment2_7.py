def numPattern(num):
    for i in range(1,num+1):
        for j in range(1,num+1):
            print(j, end='  ')
        print()

def main():
    print("Number pattern")
    no=int(input())
    num=numPattern(no)


if __name__=="__main__":
    main()
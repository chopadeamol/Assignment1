def Pattern(no):
    for i in range(1,no+1):
        for j in range(1,i+1):
            print(j, end='  ')
        print()

def main():
    print("Number Pattern")
    no=int(input())
    num=Pattern(no)

if __name__=="__main__":
    main()
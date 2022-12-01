def PosNegZero(num):
    if (num>0):
        print("Number positive")
    elif (num==0):
        print("Zero")
    else:
        print("Number negative")

def main():
    print("Please enter a number :")
    no=int(input())
    fun=PosNegZero(no)


if __name__=="__main__":
    main()
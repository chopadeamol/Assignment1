def AddFactors(no):
    num=0
    for i in range(1,no):
        if (no%i==0):
            num=num+i
    print("The addition of factors of a number is :", num)

def main():
    print("Function to display addition of factors of a number")
    no=int(input())
    fact=AddFactors(no)

if __name__=="__main__":
    main()
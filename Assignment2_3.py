def factors(num):
    num2=1
    for i in range(1,num+1):
        num2=num2*i
    print("Factorial of number is :", num2)

def main():
    print("Addition of factors of an input number")
    no=int(input())
    fact=factors(no)

if __name__=="__main__":
    main()

def ChkSum(num):
    if (num%2==0):
        print("Even number")
    else:
        print("Odd number")

def main():
    print("Function to check the input number is even or odd")
    print("Enter a number to check")
    no=int(input())
    ChkSum(no)

if __name__=="__main__":
    main()

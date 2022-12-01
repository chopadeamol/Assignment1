def divisible(num):
    print(bool(num%5==0))

def main():
    print("Enter a number to check if divisible by five")
    no=int(input())
    div=divisible(no)

if __name__=="__main__":
    main()

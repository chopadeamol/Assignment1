def Add(num2):
    addition=0
    for i in range(len(num2)):
        addition=addition+num2[i]
    print("addition of the numbers is :",addition)

def main():
    print("Function to check addition of input numbers")
    num=[]
    print("Please enter a count of number")
    num1=int(input())
    for i in range(num1):
        two=int(input())
        num.append(two)
    print("Entered number is :",num)
    Add(num)

if __name__=="__main__":
    main()

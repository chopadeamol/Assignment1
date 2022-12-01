def addDigit(digit):
    add=0
    for i in range(len(digit)):
        add=add+int(digit[i])
    print("Addition of digits are", add)

def main():
    print("Function to display addition of digits in the number")
    no=input()
    ad=addDigit(no)

if __name__=="__main__":
    main()
import Arithmetic

def main():
    print("Function to print Addition, Subtraction, Multiplication, Division")

    print("Enter first number :")
    no1=int(input())

    print("Enter second number :")
    no2=int(input())

    add=Arithmetic.Add(no1,no2)
    sub=Arithmetic.Sub(no1,no2)
    mult=Arithmetic.Mult(no1,no2)
    div=Arithmetic.Div(no1,no2)

if __name__=="__main__":
    main()
def prime(no):
    #if no>1:
        for i in range(2,no):
            if (no%i==0):
                print("No is not prime")
                break
        else:
            print("No is prime")
    #else:
        #return no
        #print("No is not a prime")

def main():
    print("Function to display a number prime or not")
    no=int(input())
    pri=prime(no)


if __name__=="__main__":
    main()